def sonu(fun):
    def sunny():
        print("hi sunny")
        fun()
        print("hello sonu")

    sunny()

@sonu
def how():
    print("how are you both")