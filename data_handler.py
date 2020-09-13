import csv
import os

DATA_FILE_PATH = os.getenv(
    'DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'H:\Coding\CodeCool\Workbench\super_sprinter_3000\data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']

user_stories = [{'id': "0", 'title': "test", 'user_story': "I'm writing to check if everything works",
                 'acceptance_criteria': "must work without errors", 'business_value': "1500", 'estimation': "8",
                 'status': "in progress"},
                {'id': "1", 'title': "test_1", 'user_story': "I'm writing to check if everything works",
                 'acceptance_criteria': "must work without errors", 'business_value': "1500", 'estimation': "8",
                 'status': "in progress"}]


def get_id():
    temp = 0
    for story in user_stories:
        if int(story["id"]) > temp:
            temp = int(story["id"])
    return str(temp + 1)


def add_story(story):
    story["id"] = get_id()
    user_stories.append(story)


def get_all_user_story():
    result = []
    with open(DATA_FILE_PATH) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            result.append(line)

    return result


def save_story(story):
    result = get_all_user_story()
    result.append(story)
    with open(DATA_FILE_PATH, "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(result)
