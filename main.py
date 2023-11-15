flags = []

def flagoji_encode(plain: str) -> str:
    byte_array = plain.encode()
    # 8 bit chunks --> 2^8 = 256
    encoded = []
    for byte in byte_array:
        encoded.append(flags[byte])
    return "".join(encoded)

def flagoji_decode(encoded: str) -> str:
    decoded_bytearray = bytearray()
    encoded_list = [encoded[i:i+2] for i in range(0, len(encoded), 2)]
    for flag in encoded_list:
        index = flags.index(flag) # returns int
        decoded_bytearray.append(index) # technically only accept byte
    return decoded_bytearray.decode("utf-8")

if __name__ == "__main__":
    with open("flagoji-seed-sanitized.txt", "r", encoding="utf-8") as f:
        flags = f.read().splitlines()
    
    plain = input("Enter a string to encode: ")
    print(plain)
    encoded = flagoji_encode(plain)
    print(encoded)
    decoded = flagoji_decode(encoded)
    print(decoded)

