import openai
import os
import sys
import csv
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import common.config as config

openai.api_key = config.OPENAI_API

class CommandExecutor:

    def __init__(self):
        self.engine_id = "text-davinci-002"
        self.new_row = []

    def generate_solution(self, input_data):
        self.prompt = "Solution to the following problem:\n" + input_data + "\n\nSolution:"
        self.new_row.append(input_data)
        model = self.engine_id
        response = openai.Completion.create(
            engine=model,
            prompt=self.prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        solution = response.choices[0].text.strip()
        return solution

    def main(self, input_data):
        solution = self.generate_solution(input_data)
        print(solution)
        self.new_row.append(solution)

    def add_csv(self):
        csv_path='../settings/history.csv'
        with open(csv_path, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.new_row)

    def out_csv(self):
        in_csv_path='../settings/history.csv'
        out_csv_path='../settings/list.csv'
        with open(in_csv_path, 'r') as csvfile:
            last_row = None
            for row in csv.reader(csvfile):
                if row:
                    last_row = row
        with open(out_csv_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            row_number = len(data) + 1
            last_row.insert(0, row_number)
        with open(out_csv_path, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            row_number = len(data) + 1
            writer.writerow(last_row)

    def check_history(self):
        csv_path='../settings/history.csv'
        with open(csv_path, mode="r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row:
                    print(row[0])
                    print(row[1])
                    print()

    def check_list(self):
        csv_path='../settings/list.csv'
        with open(csv_path, mode="r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row:
                    print(row[0], row[1])
                    print(row[2])
                    print()

    def delete_element(self, number):
        csv_path='../settings/list.csv'
        rows = []
        deleted_row = None
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if row[0] == number:
                    deleted_row = i + 1
                else:
                    rows.append(row)

        if deleted_row is not None:
            for row in rows:
                row[0] = str(int(row[0]) - 1) if int(row[0]) > deleted_row else row[0]

        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    def clear_history(self):
        csv_path='../settings/history.csv'
        with open(csv_path, 'w', newline='') as f:
            f.truncate()
