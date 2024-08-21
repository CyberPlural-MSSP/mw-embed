%define NtCurrentPeb() gs:[0x60]
%define ProcessParameter 32
%define StandardOutput 40
%define NtCurrentProcess() -1

section .rdata
  Message db `Hello, world!\n\0`
  Length equ $-Message
section .text
  global main
[BITS 64]
NtWriteFile:
  int 7
NtTerminateProcess:
  int 36
main:
  sub rsp, 88
  mov rcx, NtCurrentPeb()
  mov rcx, ProcessParameter
  mov rcx, StandardOutput
  xor edx, edx
  lea rax, 72[rsp] ; IoStatusBlock
  mov qword 32[rsp], rax
  mov qword 40[rsp], Message
  mov qword 48[rsp], Length
  mov qword 56[rsp], 0
  mov qword 64[rsp], 0
  call NtWriteFile

  mov rcx, NtCurrentProcess()
  xor edx, edx
  call NtTerminateProcess
  xor ecx, ecx
