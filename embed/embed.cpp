#include "PEFile.h"

int main(int argc, char* argv[]) {
  if (argc < 3) return -1;
  // Open the input file
  char* infilePath = argv[1];
  char* outfilePath = argv[2];

  PEFile pe(infilePath);

  // Add functions to the import table
  char* functions[] = { "Trigger" };
  pe.addImport("payload.dll", functions, 1);

  // Add a new section named ".@dll" with size "0x1000" byte
  // pe.addSection(".@dll", 0x1000, false);

  // Save the modified file
  pe.saveToFile(outfilePath);
}