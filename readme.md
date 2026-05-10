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
