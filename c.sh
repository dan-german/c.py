compile_and_run() { 
    clang main.c -o main_c
    ./main_c
}

compile_c_to_asm() { 
    clang -Xclang -ast-dump -fsyntax-only main.c
}

compile_c_to_asm
echo $?