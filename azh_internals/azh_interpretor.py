_max_binary_output_size = 8

_binary_value_to_insert = 1
_stack = []

_binary_outputs_array = []
_decrypted_outputs_array = []
_operators_array = []


def _invert_binary_value_to_insert():
    global _binary_value_to_insert
    if _binary_value_to_insert == 1:
        _binary_value_to_insert = 0
    else:
        _binary_value_to_insert = 1


def _read_stack_element(_stack_element):
    global _binary_value_to_insert
    binary_output = ""
    idx = 0
    max_idx = len(_stack_element) - 1

    for _stack_element_character in _stack_element:
        if idx >= max_idx and binary_output != "":
            _binary_outputs_array.append(binary_output)
            binary_output = ""

        if len(binary_output) == _max_binary_output_size:
            _binary_outputs_array.append(binary_output)
            binary_output = ""

        if _stack_element_character == "a":
            binary_output += str(_binary_value_to_insert)
        elif _stack_element_character == "b":
            _invert_binary_value_to_insert()
        elif _stack_element_character == "c":
            _operators_array.append("+")
        elif _stack_element_character == "d":
            _operators_array.append("-")

        else:
            return "ERROR | " + _stack_element_character + " is not supported dumbass"
        idx += 1


def _validate_binary_outputs():
    filling_binary_output_times = 0
    array_idx = 0

    for _binary_output in _binary_outputs_array:
        if len(_binary_output) < _max_binary_output_size and _binary_output != "":
            filling_binary_output_times = _max_binary_output_size - len(_binary_output)
            for loop in range(filling_binary_output_times):
                _binary_outputs_array[array_idx] = (
                    f"{_binary_outputs_array[array_idx][:0]}{str(_binary_value_to_insert)}{_binary_outputs_array[array_idx][0:]}"
                )
        array_idx += 1


def _decrypt_binary_ouputs_array():
    for _binary_output in _binary_outputs_array:
        if _binary_output != "":
            _decrypted_outputs_array.append(int(_binary_output, 2))
            print(f"{int(_binary_output, 2)}")


def do_math():
    result = 0
    idx = 0

    for b_output in _decrypted_outputs_array:
        if idx == 0:
            result += b_output
        elif _operators_array[idx] == "+":
            result += b_output
        elif _operators_array[idx] == "-":
            result -= b_output

        idx += 1

    return result


# STEP 1: Lire la stack, interpréter ligne par ligne
def interpret_stack():
    # A. Initialiser les variables nécessaires:

    # B. CHECK 1 | Si la stack est vide alors on renvoi une erreur
    if len(_stack) <= 0:
        print("ERROR | Stack empty, cannot proceed")
        return

    for _stack_element in _stack:
        # C. CHECK 2 | Si le premier caractère de l'élément de stack est "b", on renvoi une erreur (azh ne veut pas, c'est pas logique selon lui)
        if _stack_element[0] == "b":
            print(
                "ERROR | azh doesn't allow a stack element that starts with 'b' (not logic)"
            )
            return
        # D. Si le CHECK 2 est passé alors on lit l'élément de la stack
        _read_stack_element(_stack_element)

    # E. Valide les bits (les mets à une longueur de 8 octets si besoin)
    print("")
    print(f"BINARY OUTPUTS BEFORE VALIDATION -> {_binary_outputs_array}")
    print("Validating binary outputs...")
    _validate_binary_outputs()
    print(f"Binary outputs validated! -> {_binary_outputs_array}")
    print(f"Operators listed: {_operators_array}")

    # F. Decrypte les bits en chiffres
    print("")
    print("Decrypting binary outputs...")
    _decrypt_binary_ouputs_array()

    # G. Maths?????
    if len(_operators_array) > 0:
        print("")
        print("Doing some math...")
        print(do_math())


def add_data_to_stack(_data_added):
    _stack.append(_data_added)
    print(f"STACK | Current state -> {_stack}")
