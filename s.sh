compile_and_run() {
    as -arch arm64 -o main.o main.s
	ld -o main main.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _main -arch arm64 
    ./main
}

compile_and_run
echo $?