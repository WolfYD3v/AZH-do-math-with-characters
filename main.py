from azh_internals import azh_interpretor
from project_files import project_main


def main():
    azh_interpretor.add_data_to_stack("aabababbabc")
    azh_interpretor.add_data_to_stack("abbaac")
    azh_interpretor.add_data_to_stack("dbbaaabaa")

    azh_interpretor.interpret_stack()

    project_main.main()


if __name__ == "__main__":
    main()
