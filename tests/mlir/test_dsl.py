import heterocl as hcl


def test_dsl():

    A = hcl.placeholder((32, 32), "A")
    B = hcl.placeholder((32, 32), "A")

    def kernel(A, B):
        with hcl.for_(0, 32, 1, "i") as i:
            with hcl.for_(0, 32, 1, "j") as j:
                B[i, j] = A[i, j] + 1
        return B

    target = hcl.Platform.xilinx_zc706
    target.config(compiler="vivado_hls", mode="csyn", project="gemm.prj")

    s = hcl.create_schedule([A, B], kernel)
    mod = hcl.build(s, target=target)
    print(mod.src)


if __name__ == "__main__":
    test_dsl()
