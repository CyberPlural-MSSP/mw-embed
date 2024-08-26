ifeq ($(OS),Windows_NT)
    CC = gcc
else
    CC = x86_64-w64-mingw32-gcc
endif

payload.dll: payload.c
	$(CC) -shared -o payload.dll payload.c