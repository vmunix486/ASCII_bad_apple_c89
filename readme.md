# ASCII Art Video : Bad Apple

## Play Bad Apple!

```
gcc -O3 -flto -std=c89 run.c -o run
./run
```

## Dependencies

* To re-generate the ascii art video source which is ```play.txt```, the following Python dependencies are needed:

> OpenCV with python package installed and well configured.  
> pip package: ```image```

## Notes

 - Original python version can be faster than the C version, due to the reason it uses the `clear` command from the system. This is meant to be portable, not as much fast.
 - Can technically use any video you want, because it uses `video.mp4` and changes that into the cool ASCII video. Something you might have to change, though is the resolution and the length in both `genvid.py` and `run.c`. I might think about extending this out into a video format ;)
