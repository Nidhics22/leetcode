class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff  # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        if b > 0:
            return (a & mask)
        else:
            return a

    # step 1:
    # do or operation (a ^ b)

    # step 2:
    # do and operation & shift it by 1 for carry (a & b) << 1

    # step 3:
    # do or operaton of step1 & step2 answers

    # step 4
    # do and operaton of step1 & step2 answers snd shift it by 1 on left

    # step 5
    # do or operation of final answers og step 3 and step 4



