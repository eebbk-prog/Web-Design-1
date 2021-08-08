import dataset

if __name__ == "__main__":
    todo_list_db = dataset.connect('sqlite:///todo_list.db')
    todo_table = todo_list_db.get_table('todo')
    todo_table.drop()
    todo_table = todo_list_db.create_table('todo')
    todo_table.insert_many([
        {'user' : 'Mike', 'course_number' : 'CS23001', 'course_name': 'Computer Science II', 'done' : 1},
        {'user' : 'Mike', 'course_number' : 'CS33901', 'course_name': 'Software Engineering', 'done' : 1},
        {'user' : 'Mike', 'course_number' : 'CS44001', 'course_name': 'Computer Science III', 'done' : 1},
        {'user' : 'Mike', 'course_number' : 'CS44105', 'course_name': 'Web programming I', 'done' : 0},

        {'user' : 'John', 'course_number' : 'CS2300111', 'course_name': 'Computer Science II', 'done' : 1},
        {'user' : 'John', 'course_number' : 'CS3390111', 'course_name': 'Software Engineering', 'done' : 1},
        {'user' : 'John', 'course_number' : 'CS4400111', 'course_name': 'Computer Science III', 'done' : 1},
        {'user' : 'John', 'course_number' : 'CS4410511', 'course_name': 'Web programming I', 'done' : 0},
    ])