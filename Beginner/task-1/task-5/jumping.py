completed = 0

for i in range(10):

    completed += 10

    print("You completed", completed, "jumping jacks.")

    if completed == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ")

    if tired.lower() == "yes" or tired.lower() == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ")

        if skip.lower() == "yes" or skip.lower() == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break

    else:
        print("Remaining:", 100 - completed)