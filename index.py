import requests
import sys


def get_definition(word: str, lang: str="en_US"):
    res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/{lang}/{word}")
    if res:
        return res.json()


def main():
    given_word = sys.argv[1]
    defs = get_definition(given_word)
    i = 0

    for d in defs:
        print(d["word"])
        print(d["phonetics"][0]["text"])
        print()

        for m in d["meanings"]:
            print(m["partOfSpeech"])
            for dd in m["definitions"]:
                i += 1

                print(str(i) + ".", dd["definition"] + "\n")

                if "example" in dd.keys():
                    print("Example:", dd["example"])

                if "synonyms" in dd.keys():
                    print("Synonyms:", " ".join(dd["synonyms"]))

                print()


def print_usage_error(code=1):
    print("usage: define [word]")
    quit(code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_error()
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print_usage_error(0)

    main()

