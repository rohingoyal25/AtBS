import time, random

def main():
    num_of_questions = 10
    correct_answers = 0

    for question_number in range(num_of_questions):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        guess = -1
        prompt = f"#{question_number+1}: {x} x {y} = "
        error_count = 0
        while guess != sum and error_count < 3:
            try:
                guess = int(input(prompt))
            except ValueError:
                print("Input is not a number")
            if guess == x+y:
                correct_answers += 1
                break
            else:
                error_count += 1
        time.sleep(1)

    print(f"{correct_answers}/{num_of_questions}")

main()