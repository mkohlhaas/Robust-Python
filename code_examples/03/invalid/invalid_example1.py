def read_file_and_reverse_it(filename: str) -> str:
    with open(filename) as f:
        return f.read().encode("utf-8")[::-1]


read_file_and_reverse_it("run_tests.sh")
