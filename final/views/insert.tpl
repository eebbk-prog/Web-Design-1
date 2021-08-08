<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

       "http://www.w3.org/TR/html4/loose.dtd">
   <html>
   <head>
   <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
   <title>Insert Data</title>
   </head>

<body>
<center>
<form action="/insert" method="post">
Course Number <input type="text" name="course_number"/><br>
Course Name <input type="text" name="course_name"/><br>

complte<input type="radio" name="complte"  value = "1" checked="complte">1
  <input type="radio" name="complte"  value = "0">0

 <br> one for done zero for not
<hr/>
<button onclick="window.location='/'; return false">Cancel</button>&nbsp
<a href='/'>Cancel</a>&nbsp
<input type="submit" value="Submit"/>
</form>
</center>
<hr/>
</body>
</html>