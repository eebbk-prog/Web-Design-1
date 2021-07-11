from bottle import route, get, post 
from bottle import run, debug
from bottle import request, response, redirect, template
from bottle import static_file
import dataset
import json
from bottle import default_app


#http://localhost:8090



@route("/")
def get_midterm():
    todo_list_db = dataset.connect('sqlite:///todo_list.db')
    todo_table = todo_list_db.get_table('todo')
    items = todo_table.find()
    items = [ dict(x) for x in list(items) ]
    return template("Midterm", items=items)



@route("/static/png/<filename:re:.*\.png")
@route("/image/<filename:re:.*\.png")
def get_picture():
    return static_file(filename="the_boat.png", root="static", mimetype="image/png")


@route("/static/<filename:path>")
def get_static(filename):
   return static_file(filename=filename, root="static")




@route("/delete/<id>")
def get_delete(id):
    id = int(id)
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        print(f"We need to delete id# {id}...")
        todo_table.delete(id=id)
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return template("deleted", id=id)


@get("/insert")
def get_insert():
    return template("insert")

@post("/insert")
def post_insert():
    course_number = request.forms.get('course_number')
    print("course_number=", course_number)
    course_name = request.forms.get('course_name')
     
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        todo_table.insert({
            'course_number' : course_number.strip(),
            'course_name' : course_name.strip(),
            'done' : 1
            
        })
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return redirect('/')

@get("/edit/<id>")
def get_edit(id):
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        items = list(todo_table.find(id=id))
        if len(items) != 1:
            response.status="404 Not Found:"+str(id)
            return
        items = [ dict(x) for x in items ]
        print(items)
        print(items[0])
    except Exception as e:
        print(e)
        response.status="409 Bad Request:"+str(e)
        return

    return template("edit", item=items[0])  # put something here

@post("/edit")
def post_edit():
    id = request.forms.get('id')
    id = int(id)
    course_number = request.forms.get('course_number')
    course_name = request.forms.get('course_name')
    print("course_number=", course_number)
    try:
        todo_list_db = dataset.connect('sqlite:///todo_list.db')
        todo_table = todo_list_db.get_table('todo')
        todo_table.update({
            'id' : id,
            'course_number' : course_number.strip(),
            'course_name' : course_name.strip()
        }, ['id'])
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return redirect('/')





if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8090)
else:
    application = default_app()