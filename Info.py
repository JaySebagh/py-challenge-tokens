class Info:

    def __init__(self):
        self.address = ""
        self.auth = ""
        self.token1 = ""
        self.token2 = ""
        self.token3 = ""

    def Setup(self):
        self.address = str(input("\t> address: "))
        if len(self.address) == 0:
            raise Exception("address missing")

        self.auth = str(input("\t> auth (include Basic): "))
        if len(self.auth) == 0:
            raise Exception("auth missing")

        self.token1 = str(input("\t> token 1: "))
        if len(self.token1) == 0:
            raise Exception("token 1 missing")

        self.token2 = str(input("\t> token 2: "))
        if len(self.token2) == 0:
            raise Exception("token 2 missing")

        self.token3 = str(input("\t> token 3: "))
        if len(self.token3) == 0:
            raise Exception("token 3 missing")
