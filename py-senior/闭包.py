def test(num):
    print("---1---")
    def test_in(num_in):
        print("---2---")
        print(num+num_in)
        def test_in_in(num_in_in):
            print("---4---")
            print(num+num_in+num_in_in)

        return test_in_in
    print("---3---")
    return test_in

test(10)(100)(1000)