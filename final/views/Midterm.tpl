<html>
<head>
<title>Midterm Website</tittle>
%include header
%include style
</head>

<body>
%include banner

%if message:
    %include('alert.tpl', message=message)
%end

%include('navigation.tpl', status=status)



<table class="table table-striped table-hover">
  <tr>
    <th>Course Number</th>
    <th>Course Name</th>
    <th>Completed</th>
    <th>Edit</th>
    <th>Delete</th>
   
  </tr>
  %for item in items:
    <tr>
      <td>{{item['course_number']}}</td>
       <td>{{item['course_name']}}</td>
      <td>
      %if item['done']:
        <span class="material-icons-outlined">check_circle</span>
      %else:
        <span class="material-icons-outlined">unpublished</span>
      %end
      </td>
      <td><a href="/edit/{{item['id']}}"><span class="material-icons">
edit
</span></a></td>
      <td><a href="/delete/{{item['id']}}"><span class="material-icons">
delete
</span></a></td>
    </tr>
  %end
</table>
<hr/>
<a href="insert">Add a new task...</a>
<hr/>


<div id="message1" class="msg container bg-warning my-0 p-0">
  <span><strong>Note</strong> This is a message 1</span>
  <button type="button" class="btn btn-primary" onclick="$('#message').hide()">OK</button>
</div>
<div id="message2" class="msg container bg-warning my-0 p-0">
  <span><strong>Note</strong> This is a message 2</span>
  <button type="button" class="btn btn-primary" onclick="$('#message').hide()">OK</button>
</div>
<div id="message3" class="msg container bg-warning my-0 p-0">
  <span><strong>Note</strong> This is a message 3</span>
  <button type="button" class="btn btn-primary" onclick="$('#message').hide()">OK</button>
</div>
<button type="button" class="btn btn-primary" onclick="$('#message').show()">Show</button>
<script>
$(document).ready(function() {
  $('.msg').hide()
});
</script>


%include drawing

<h1 id="id_attribute_1">About me</h1>
<h6 id="id_attribute_2">My name is Yuxiang Zhou and I am from china. I am a CS student in <a href="https://www.kent.edu" target="_blank">Kent State University</a>. </h6>
<img src="/static/follower.jpeg" class="float-right">


</body>


</html>