import logging
import os


os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")


def average_score(file_name):
    total = 0
    count = 0

    with open(file_name, 'r') as file: 
        for line in file:
            try:
                name, score = line.strip().split(",")
                score = int(score)  # May raise ValueError
                total += score
                count += 1
                logging.info(f"Processed record: {name} scored {score}")   

            except ValueError:
                logging.error(f"Invalid score for record: {line.strip()}")

            except Exception as e:
                logging.error(f"Unexpected error: {e}")     
    
    if count == 0:
        return 0

    return total / count    


if __name__ == "__main__":
    avg = average_score("score.csv")
    print(f"Average score: {avg}")
  



    
