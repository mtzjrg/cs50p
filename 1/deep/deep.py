# Deep Thought: Implement a program that prompts the user for the answer to the
#               Great Question of Life, the Universe and Everything, outputting
#               Yes if the user inputs 42, forty-two or forty two
#               (case and space insensitively)

match input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
