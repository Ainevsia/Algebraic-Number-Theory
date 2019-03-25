# BigIngeterCalculation
Some code i wrote to implement the key algorithms that the Prof. Chen taught while learning the Number Therom this semester.

# Why to re-build the wheel?

Ask Google and it will tell you that there already exists an owesome tool to do fast and reliable big integer calculation called `GMP`. `GNU MP` is a portable library written in C for arbitrary precision arithmetic on `integers`, `rational numbers`, `and floating-point numbers`. It aims to provide the **fastest possible arithmetic** for all applications that need **higher precision** than is directly supported by the basic C types.

I just only want to implement a small set of it, with respect to the operations used in my class **Mathematical Basis for Information Security**, such as prime, modulo, etc.

# Deployment & Development

1. first locate an appropriate folder and run:
`git clone git@github.com:Ainevsia/BigIngeterCalculation.git`

2. second build the `integer.cpp` into `a.out`:
`cd BigIngeterCalculation && g++ integer.cpp -o a.out`

3. finnaly, run it:
`./a.out`

> please feel free to contribute any idea or suggestions you have!
We are looking forward to hear your voice
