embed.o: embed.cpp
	x86_64-w64-mingw32-g++ -c embed.cpp -o embed.o

PEFile.o: PEFile.cpp
	x86_64-w64-mingw32-g++ -c PEFile.cpp -o PEFile.o

embed.exe: PEFile.o embed.o
	x86_64-w64-mingw32-g++ PEFile.o embed.o -static -o embed.exe
