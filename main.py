from compiler.compiler import compile_to_gpt_patois
import json

def main():
    user_input = input("Enter your instructions for the GPT model: ")
    gpt_patois_string = compile_to_gpt_patois(user_input)
    print("Here is your input compiled to GPT-Patois format:\n")
    print(gpt_patois_string)

if __name__ == "__main__":
    main()