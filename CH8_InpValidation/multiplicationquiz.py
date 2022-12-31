import pyinputplus as pyip
import time, random

def main():
    num_of_questions = 10
    correct_answers = 0

    for question_number in range(num_of_questions):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        prompt = f"#{question_number+1}: {x} x {y} = "
        try:
            # Right answers are handled by allowRegexes.
            # Wrong answers are handled by blockRegexes, with a custom message.
            pyip.inputStr(prompt, allowRegexes=['^%s$' % (x * y)],
                                blockRegexes=[('.*', 'Incorrect!')],
                                timeout=8, limit=3)
        except pyip.TimeoutException:
            print("Out of time!")
        except pyip.RetryLimitException:
            print("Out of tries!")
        else:
            # This block runs if no exceptions were raised in the try block.
            print('Correct!')
            correct_answers += 1

        time.sleep(1)

    print(f"{correct_answers}/{num_of_questions}")

main()