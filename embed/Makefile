ifeq ($(OS),Windows_NT)
    CXX = g++
else
    CXX = x86_64-w64-mingw32-g++
endif

embed.o: embed.cpp
	$(CXX) -c embed.cpp -o embed.o

PEFile.o: PEFile.cpp
	$(CXX) -c PEFile.cpp -o PEFile.o

embed.exe: PEFile.o embed.o
	$(CXX) PEFile.o embed.o -static -o embed.exe
