import os
import string
from typing import List


def find_max_in_lines(file_name: str) -> List[int]:
    result = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers = list(map(int, line.split(",")))
                    result.append(max(numbers))
        return result
    except FileNotFoundError:
        raise FileNotFoundError("File Not Found")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")


def clean_word(word: str) -> str:
    return word.translate(str.maketrans("", "", string.punctuation)).lower()


def anagram_finder(file_name: str, output_path: str = None) -> None:
    try:
        base_name = os.path.basename(file_name)
        if output_path is None:
            output_file_path = os.path.join(
                os.path.dirname(file_name), f"anagrams_{base_name}"
            )
        else:
            output_file_path = os.path.join(
                output_path, f"anagrams_{base_name}"
            )

        with open(file_name, "r") as file, open(
            output_file_path, "w"
        ) as output_file:
            for line in file:
                words = [clean_word(word) for word in line.strip().split()]
                anagram_pairs = []

                for i in range(len(words)):
                    word1 = "".join(sorted(words[i]))
                    for j in range(i + 1, len(words)):
                        word2 = "".join(sorted(words[j]))
                        if word1 == word2 and words[i] != words[j]:
                            anagram_pairs.append(f"{words[i]},{words[j]}")

                if anagram_pairs:
                    output_file.write(f"{' '.join(anagram_pairs)}\n")
                else:
                    output_file.write("-\n")

    except FileNotFoundError:
        raise FileNotFoundError("File Not Found")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")


def log_file_categorizer(file_name: str, output_path: str = None) -> None:
    try:
        if output_path is None:
            output_path = os.path.join("test_data", "log_file")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        error_file_name = os.path.join(
            output_path, f"error_{os.path.basename(file_name)}"
        )
        info_file_name = os.path.join(
            output_path, f"info_{os.path.basename(file_name)}"
        )
        warning_file_name = os.path.join(
            output_path, f"warning_{os.path.basename(file_name)}"
        )

        with open(file_name, "r") as input_file, open(
            error_file_name, "w"
        ) as error_file, open(info_file_name, "w") as info_file, open(
            warning_file_name, "w"
        ) as warning_file:

            for line in input_file:
                line = line.strip()
                if line.startswith("ERROR"):
                    error_file.write(f"{line}\n")
                elif line.startswith("INFO"):
                    info_file.write(f"{line}\n")
                elif line.startswith("WARNING"):
                    warning_file.write(f"{line}\n")

    except FileNotFoundError:
        raise FileNotFoundError("File Not Found")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
