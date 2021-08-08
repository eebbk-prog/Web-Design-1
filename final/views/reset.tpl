<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

       "http://www.w3.org/TR/html4/loose.dtd">
   <html>
   <head>
   <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
   <title>User Login</title>
   </head>

<body>
<center>
Reset Password<br/><br/>
<form action="/reset/{{username}}/{{reset_token}}" method="post">

     
     <p> User Name: {{ username }} </p><br/>
     Password<br/>
     <input type="password" name="password"/><br/>
     Repeat Password<br/>
     <input type="password" name="repeat_password"/><br/>

     <hr/>
     <input type="submit" value="Reset Password"/>
     
      <input type="hidden" name="csrf_token" value="{{csrf_token}}"/>

</form>
</center>
</body>
</html>