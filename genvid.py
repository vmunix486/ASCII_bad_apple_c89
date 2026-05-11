from PIL import Image
import cv2
import os

video_length = 218  # seconds

ASCII_CHARS = (
    '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
)


def scale_image(image, new_width=100, new_height=30):
    """
    Resize image while preserving aspect ratio.
    """

    original_width, original_height = image.size
    aspect_ratio = original_height / float(original_width)

    if new_height == 0:
        new_height = int(aspect_ratio * new_width)

    return image.resize((new_width, new_height))


def convert_to_grayscale(image):
    return image.convert("L")


def map_pixels_to_ascii_chars(image):
    """
    Map grayscale pixels to ASCII characters.
    """

    pixels_in_image = list(image.getdata())

    # 255 / len(ASCII_CHARS)
    range_width = 255 / (len(ASCII_CHARS) - 1)

    pixels_to_chars = [
        ASCII_CHARS[min(int(pixel_value / range_width), len(ASCII_CHARS) - 1)]
        for pixel_value in pixels_in_image
    ]

    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, new_width=100, new_height=30):
    image = scale_image(image, new_width, new_height)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [
        pixels_to_chars[index:index + new_width]
        for index in range(0, len_pixels_to_chars, new_width)
    ]

    return "\n".join(image_ascii)


def handle_image_conversion(image_filepath):
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print(f"Unable to open image file {image_filepath}.")
        print(e)
        return ""

    return convert_image_to_ascii(image)


if __name__ == "__main__":

    vidcap = cv2.VideoCapture("video.mp4")

    if not vidcap.isOpened():
        print("Could not open video.mp4")
        exit(1)

    time_count = 0
    frames = []

    while time_count <= video_length * 1000:

        print(f"Generating ASCII frame at {time_count} ms")

        # Seek to timestamp in milliseconds
        vidcap.set(cv2.CAP_PROP_POS_MSEC, time_count)

        success, frame = vidcap.read()

        if success:

            # Convert OpenCV BGR image to RGB for PIL
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert NumPy array to PIL Image
            pil_image = Image.fromarray(frame_rgb)

            ascii_frame = convert_image_to_ascii(
                pil_image,
                new_width=100,
                new_height=30
            )

            frames.append(ascii_frame)

        else:
            print(f"Failed to read frame at {time_count} ms")

        time_count += 100

    vidcap.release()

    with open("play.txt", "w", encoding="utf-8") as f:
        f.write("SPLIT".join(frames))

    print("Done!")
