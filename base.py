import base64
import itertools

def decode_base64(input_str):
    try:
        return base64.b64decode(input_str).decode('utf-8')
    except Exception:
        return None

def decode_base32(input_str):
    try:
        return base64.b32decode(input_str).decode('utf-8')
    except Exception:
        return None

def decode_base16(input_str):
    try:
        return base64.b16decode(input_str).decode('utf-8')
    except Exception:
        return None

def decode_string(input_str, encodings):
    decode_functions = {
        'base64': decode_base64,
        'base32': decode_base32,
        'base16': decode_base16
    }
    
    decoded_results = []
    current_str = input_str

    for encoding in encodings:
        decode_func = decode_functions[encoding]
        result = decode_func(current_str)
        if result is None:
            return None  # If decoding fails, stop this sequence
        decoded_results.append((encoding, result))
        current_str = result

    return decoded_results


def main():
    input_str = input("Enter the encoded string: ")
    possible_encodings = ['base64', 'base32', 'base16']
    max_depth = 3

    for depth in range(1, max_depth + 1):
        for encodings_sequence in itertools.product(possible_encodings, repeat=depth):
            result = decode_string(input_str, encodings_sequence)
            if result:
                print("Decoding sequence:", " -> ".join([x[0] for x in result]))
                print("Decoded result:", result[-1][1])
                print("----------------------")

if __name__ == "__main__":
    main()
