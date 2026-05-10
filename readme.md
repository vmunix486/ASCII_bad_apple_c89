# ASCII Art Video : Bad Apple

## Play Bad Apple!

```
gcc -O3 -flto -std=c89 run.c -o run
./run
```

## Dependencies

* To simply run the demo with sound effects, you need ```mplayer``` installed.

* To re-generate the ascii art video source which is ```play.txt```, the following Python dependencies are needed:

> OpenCV with python package installed and well configured.  
> pip package: ```image```

## Notes

 - Default play.txt is 100x30. I am planning on making a new version that is 80x25 for VGA text mode so it can render on normal linux/bsd/elks terminals without x11/wayland
