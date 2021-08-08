<!DOCTYPE html>
<html>
<head>
%include header
</head>
<body>
%include banner
<center>
<form action="/edit" method="post">
Courese Number <input type="text" name="course_number" value="{{item['course_number']}}"/><br>
Course Name <input type="text" name="course_name" value="{{item['course_name']}}"/><br>

complte<input type="radio" name="complte"  value = "1" checked="complte">1
  <input type="radio" name="complte"  value = "0">0

 <br> one for done zero for not
<hr/>
<button onclick="window.location='/'; return false">Cancel</button>&nbsp
<a href='/'>Cancel</a>&nbsp
<input type="submit" value="Submit"/>

<input type="text" name="id" value="{{item['id']}}" readonly hidden/>
</form>
</center>
<hr/>
</body>
</html>