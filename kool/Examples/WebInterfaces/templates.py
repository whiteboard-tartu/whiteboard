#!/usr/bin/env python3

HEADER = """
<!DOCTYPE HTML>
<html>
<head>
<link rel="icon" type="image/png" href="assets/img/favicon.ico" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
<link rel="stylesheet" href="assets/css/styles.css" >
<title>Kool Project</title>
</head>
<body>
"""

NAVBAR = """
<nav class="navbar navbar-inverse bg-inverse navbar-toggleable-md">
  <div class="container">
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarsExampleContainer" aria-controls="navbarsExampleContainer" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <a class="navbar-brand" href="#">Kool</a>

    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <a class="nav-link" href="/">Logout</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
"""

START_CONTAINER = """<div class="container">"""
END_CONTAINER = """</div>"""


FOOTER = """
</body>
<footer>
<div class="text-center"><small>Kool Project. University of Tartu</small> <span class="badge badge-primary">Demo</span></div>
</footer>
</html>
"""

LOGIN_FORM = """
<div class="container">
  <div class="row justify-content-center">
    <div class="col-md-6">
    <div id="login" class="card">
    <h2>Login</h2>
    <form method="post" action="start">
      <div class="form-group">
        <label for="email">Email address</label>
        <input type="email" name="email" class="form-control" id="email1" placeholder="Enter email">
      </div>

       <div class="form-group">
        <label for="password">Password</label>
        <input type="password" name="pword" class="form-control" id="password" placeholder="Password">
      </div>

       <div class="form-check">
          <label class="form-check-label">
            <input type="radio" class="form-check-input" name="role" id="student" value="student" checked>
            Student
          </label>
        </div>

        <div class="form-check">
        <label class="form-check-label">
            <input type="radio" class="form-check-input" name="role" id="educator" value="educator">
            Educator
          </label>
        </div>
        <br>
      <input type="submit" class="btn btn-success" value="Sign In">
    </form>
    </div>
    </div>
  </div>
</div>
"""

EDUCATOR_FORM = """
<div class="card">
  <h2>Choose an option</h2>
  <form method="post" action="educator">
     <div class="form-check">
        <label class="form-check-label">
          <input type="radio" class="form-check-input" name="option" value="add_student" checked>
          Add Student
        </label>
      </div>

      <div class="form-check">
        <label class="form-check-label">
          <input type="radio" class="form-check-input" name="option" value="del_student">
          Delete Student
        </label>
      </div>

      <div class="form-check">
        <label class="form-check-label">
          <input type="radio" class="form-check-input" name="option" value="show_student_score">
          Show student grade
        </label>
      </div>

      <div class="form-check">
        <label class="form-check-label">
          <input type="radio" class="form-check-input" name="option" value="make_quiz">
          Make multiple choice quiz
        </label>
      </div>
      <br>
    <input type="submit" value="Submit" class="btn btn-success">
  </form>
</div>
"""

STUDENT_FORM = """
<div class="card">
<h2>Choose an option</h2>
<form method="post" action="student">

  <div class="form-check">
    <label class="form-check-label">
      <input type="radio" class="form-check-input" name="option" value="show_my_scores" checked>
      Show my scores
    </label>
  </div>

  <div class="form-check">
    <label class="form-check-label">
      <input type="radio" class="form-check-input" name="option" value="take_quiz">
      Take quiz
    </label>
  </div>

  <br>

  <input type="submit" value="Submit" class="btn btn-success">
</form>
</div>
"""

ADD_STUDENT = """
<div class="card">
  <h2>Add student</h2>
  <form method="post" action="add_student">

    <div class="form-group">
      <label for="fname">First name</label>
      <input type="text" name="fname" class="form-control" id="fname" placeholder="First name">
    </div>

    <div class="form-group">
      <label for="lname">Last name</label>
      <input type="text" name="lname" class="form-control" id="lname" placeholder="Last name">
    </div>

    <div class="form-group">
      <label for="email">Email</label>
      <input type="email" name="email" class="form-control" id="email" placeholder="Email">
    </div>

    <div class="form-group">
      <label for="pword1">Password</label>
      <input type="password" name="pword1" class="form-control" id="pword1" placeholder="Password">
    </div>

    <div class="form-group">
      <label for="pword2">Password (Confirm)</label>
      <input type="password" name="pword2" class="form-control" id="pword2" placeholder="Repeat password to confirm">
    </div>

    <br>

    <input type="submit" value="Submit" class="btn btn-success">
  </form>
</div>
"""

SHOW_STUDENT = """
<div class="card">
  <h2>Student</h2>
  <p>{}</p>
  <p>{}</p>
  <p>{}</p>
  <a href="/" class="btn btn-primary">Add another student</a>
</div>
"""

SHOW_STUDENT_SCORES = """
<div class="card">
<h2>Show student scores</h2>
<form method="post" action="display_student_scores">

  <div class="form-group">
    <select name="value" size="3">
     <option value="orenge@ut.ee">Antony Orenge orenge@ut.ee</option>
     <option value="benson.muite@ut.ee">Benson Muite benson.muite@ut.ee</option>
     <option value="kira.lurich@ut.ee">Kira Lurich kira.lurich@ut.ee</option>
    </select>
    </p>
  <div>

  <br>
  <input type="submit" value="Submit" class="btn btn-success">

</form>
</div>
"""

DELETE_STUDENT = """
<div class="card">
<h2>Select student record to delete from menu</h2>
<form method="post" action="complete_delete_student">

<div class="form-group">
  <select name="value" size="3">
    <option value="orenge@ut.ee">Antony Orenge orenge@ut.ee</option>
    <option value="benson.muite@ut.ee">Benson Muite benson.muite@ut.ee</option>
    <option value="kira.lurich@ut.ee">Kira Lurich kira.lurich@ut.ee</option>
  </select>
</div>
<br>
 <input type="submit" value="Delete" class="btn btn-danger">
</form>
</div>
"""

COMPLETE_DELETE_STUDENT = """
<div class="card">
<h2>Record deleted</h2>
    <form method="post" action="/">
    <p>
        <input type="submit" value="Return" class="btn btn-default">
    </p>
    </form>
</div>
"""

SHOW_MY_SCORE = """
<div class="card">
<h2>My quiz scores</h2>
<form method="post" action="/">
  <p>
    Placeholder for now - get scores from database and display them
    <table style="width:100%">
    <tr>
      <th>Quiz</th>
      <th>My score</th>
      <th>Total Score</th>
    </tr>
    <tr>
      <td>A</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <td>B</td>
      <td>17</td>
      <td>20</td>
    </tr>
    <tr>
      <td>D</td>
      <td>14</td>
      <td>15</td>
    </tr>
    </table>
    </p>
    </p>
  <p>
     <input type="submit" value="Return" class="btn btn-default">
  </p>
</form>
</div>
"""

DISPLAY_STUDENT_SCORES = """
         <div class="card">
          <h2>Student quiz scores</h2>
            <form method="post" action="/">
              <p>
                Placeholder for now - get scores from database and display them
                <table style="width:100%">
                <tr>
                  <th>Quiz</th>
                  <th>My score</th>
                  <th>Total Score</th>
                </tr>
                <tr>
                  <td>A</td>
                  <td>8</td>
                  <td>10</td>
                </tr>
                <tr>
                  <td>B</td>
                  <td>17</td>
                  <td>20</td>
                </tr>
                <tr>
                  <td>D</td>
                  <td>14</td>
                  <td>15</td>
                </tr>
                </table>
                </p>
              <p>
                 <input type="submit" value="Return" class="btn btn-default">
              </p>
            </form>
            </div>
"""

MAKE_QUIZ = """
<div class="card">
<h2>Make quiz</h2>
<form method="post" action="make_quiz">

  <div class="form-group">
    <label for="qname">New quiz name</label>
    <input type="text" class="form-control" name="qname" id="qname" placeholder="">
  </div>

  <div class="form-group">
    <label for="numquestions">Number of questions (1-100)</label>
    <input type="number" class="form-control" name="numquestions" id="numquestions" placeholder="">
  </div>

  <div class="form-group">
    <label for="numoptions">Multiple choice options per question (1-15)</label>
    <input type="number" class="form-control" name="numoptions" id="numoptions" placeholder="">
  </div>
  <br>

   <input type="submit" value="Add questions" class="btn btn-success">

</form>
</div>
"""


CHOOSE_QUIZ = """
<div class="card">
<h2>Choose unattempted quiz to take</h2>
  <form method="post" action="choose_quiz">
    <p>
      Placeholder sliding menu for now<br>
        <select name="quizchoice" size="5">
         <option value="A">A</option>
         <option value="B">B</option>
         <option value="C">C</option>
         <option value="D">D</option>
         <option value="E">E</option>
        </select>
      </p>
    <p>
       <input type="submit" value="Submit" class="btn btn-success">
    </p>
  </form>
</div>
"""

QUIZ_PAGE = """
<div class="card">
<h2>Quiz</h2>
<form method="post" action="grade_quiz">
<p>
Question 1<br>
  <input type="radio" name="option" value="A">Answer 1<br>
  <input type="radio" name="option" value="B">Answer 2<br>
  <input type="radio" name="option" value="C">Answer 3<br>
</p>
<p>
 <input type="submit" value="Submit" class="btn btn-success">
</p>
</form>
</div>
"""

QUIZ_OPTIONS_START = """
<div class="card">
<form method="post" action="quiz_created">
"""

NEW_QUESTION = """
<h3> Question text:<br> <input type="text" name="qtext"><br> </h3>
"""

QUIZ_OPTION = """
Option text:<br> <input type="text" name="otext">
<input type="radio" name="option" value="A">Correct answer<br>
"""

QUIZ_OPTIONS_END = """
  <input type="submit" value="Create quiz">
</form>
</div>
"""

DEL_STUDENT_RECORD = """
<div class="card">
<h2>Succefully deleted student record</h2>
<form method="post" action="educator_options">
     <input type="submit" value="Return to educator options">
</form>
</div>
"""

QUIZ_CREATED = """
<div class="card">
<h2>Succefully created quiz</h2>
<form method="post" action="educator_options">
     <input type="submit" value="Return to educator options">
</form>
</div>
"""

QUIZ_SCORE = """
<div class="card">
<h2>Quizscore</h2>
<form method="post" action="quizscoreaction">
  <p>
    Placeholder, need to add question number<br>
      Your answer to question 1 was right/wrong<br>
    </p>
  <p>
     <input type="submit" value="Next question">
     <input type="submit" value="Try again">
  </p>
</form>
</div>
"""

ERROR_MSG = """
<br>
<div class="alert alert-danger" role="alert">
  {}
</div>
"""
