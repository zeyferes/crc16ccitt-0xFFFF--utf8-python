# Calculating CRC 16 ISO/IEC 1329 with CCITT implementation

def main():
    input = "00020101021229300012D156000000000510A93FO3230Q31280012D15600000001030812345678520441115802CN5914BEST TRANSPORT6007BEIJING64200002ZH0104最佳运输0202北京540523.7253031565502016233030412340603***0708A60086670902ME91320016A0112233449988770708123456786304"
    print(calculate_crc(input))  # prints A13A


def calculate_crc(input: str) -> str:
        crc: int = 0xFFFF
        polynomial: int = 0x1021
        bytes = input.encode(encoding="UTF-8")
        for b in bytes:
            for i in range(8):
                bit: bool = ((b >> (7 - i) & 1) == 1)
                c15: bool = ((crc >> 15 & 1) == 1)
                crc <<= 1
                if c15 ^ bit:
                    crc ^= polynomial
        crc &= 0xFFFF
        return f'{crc:04X}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
