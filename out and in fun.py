def outf():
    var=10
    def intf():
        var=20
        print("inner var",var)
    innf()
    print("outer var",var)
outf()
