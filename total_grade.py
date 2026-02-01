import logging
import os


os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/apps.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")


def total_grade(file_name):
    total= 0
    count= 0

    with open(file_name, 'r') as file:
        for line in file:
            try:
             name, grade = line.strip().split(',')
             grade = int(grade)
             total += grade
             count += 1
             logging.info(f"processed record: {name} grade is {grade}")
             
            except ValueError:
                logging.error(f"Invalid score for record: {line.strip()}")

            except Exception as e:
                logging.error(f"Unexpected error: {e}")
            
    return total
    
if __name__ == "__main__":
    total = total_grade('grade.csv')
    print(f"Total grade: {total}")    

             

