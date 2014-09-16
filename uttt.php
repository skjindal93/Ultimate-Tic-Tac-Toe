<?php
    include('header.php');
    $code ="";
          printf ( "<script>location.href='index.php'</script>" );
    if (!$session->is_logged_in()) {
      printf ( "<script>location.href='login.php'</script>" );
    }
     $id = $session->user_id;
    if (isset($_POST['submit'])){
        
        $code = $_POST['code'];


        if (strlen($code)==0 || strlen($id)==0){
          echo "You have missed some field";
        }
        file_put_contents('submissions/'.$id.'.py', stripslashes($code));
        //shell_exec("bash utic/run.sh ".$id.".py ".$id."");//insert code into python file and executes python command.Generates the output file.
	//exec ('python utic/part1.py');
    
        
        exec('bash run.sh submissions/'.$id.'.py '.$id.'',$output);
	//var_dump($output);
	//$err=file_get_contents('submissions/error.tmp');	            
	
	$move1=file_get_contents('submissions/'.$id.'.lost');
	if (strlen($move1)==0){
		$move1=file_get_contents('submissions/'.$id.'.win');
	}
        trim($move1);
        $score = file_get_contents('submissions/'.$id.'.score');
        $con=mysqli_connect("localhost","trystiit_uttt","uttt@vindy2014","trystiit_ultimate");
// Check connection
	if (mysqli_connect_errno())
  	{
  		echo "Failed to connect to MySQL: " . mysqli_connect_error();
  	}
	$sql="update user set score=".$score." where userid=".$id." and score<".$score."";
	mysqli_query($con,$sql);
	mysqli_close($con);

        
    }
?>
<html>
<link rel="stylesheet" href="codemirror/lib/codemirror.css">
<script src="codemirror/lib/codemirror.js"></script>
<script src="codemirror/addon/edit/matchbrackets.js"></script>
<script src="codemirror/lib/codemirror.js"></script>
<script src="jquery.js"></script>
<script src = "codemirror/mode/python/python.js"></script>

<style>
#instr,#announcement{
margin-top:6%;
padding:1%;
color:white;
font-family: 'Lato', Arial, sans-serif;
line-height: 1.3;
letter-spacing: 1px;
font-weight: 300;
}
.score{
color:lemonchiffon;
margin-left:17%;
}
.myButton{
  float: left;
  margin-right: 5px;
  background: #10689a;
border: none;
color: #fff;
width: auto;
cursor: pointer;
text-transform: uppercase;
display: inline-block;
padding: 10px 15px;
font-size: 1.1em;
border-radius: 2px;
letter-spacing: 1px;
}

.CodeMirror {
    width:50%;
    height:350px;
    border-radius: 5px;
    border-right: 2px solid #000000;
    border-bottom: 2px solid #000000;
    border-top: 2px solid #000000;
}
    .container2{
        margin-top : 5%;
    }
    td
    {
        text-align: center;
    }
    .main1{
        margin-top:5%;
        float: left;
        margin-left: 5%;
        margin-right:5%;
    }
    td{

    }
    table {
        border-width: 1px;
        border-color : black;
        border-collapse: collapse;
    }
    .tables td{
        width : 50px;
        height : 50px;
        border-width: 1px;
        border-style: solid;
        border-color: black;
    }
    #table_00,#table_02,#table_11,#table_20,#table_22{
        background-color: #e8edff;
    }
    #table_01,#table_10,#table_12,#table_21{
        background-color: #e8edff;
    }
    .player1{
	background-color:#FF9B82 !important;
    }
    .player2{
	background-color:#B8FF70 !important;
    }
    

</style>
    <body style="background: #34495e;">
    <div class="container2">
    <div style="text-align:center;" id="announcement"><b>Please DO NOT submit the sample code itself as your final submission. We will not be considering such entries.<br>Deadline extended by 12 hours!!! Hurry up. New deadline: 1st March 11:55 AM</b></div>
    <div class="score"><?php echo "Your score is ".$score.""?></div>
        <table class="main1">
            <!-- Top row -->
            <tr>
            <td class="tables" id = "table_00">
                <table>
                    <tr>
                      <td id = "cell_00" name="cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table> 
            </td>

            <td class="tables" id = "table_01">
                <table >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table>
            </td>
        
            <td class="tables" id = "table_02">
                <table >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table>
            </td>
        </tr>
        <!-- Middle Row -->
            <tr>
            <td  class="tables" id = "table_10">
                <table  >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table> 
            </td>

            <td  class="tables" id = "table_11">
                <table >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table>
            </td>
        
            <td  class="tables" id = "table_12">
                <table >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table>
            </td>
        </tr>
    
        <!-- Bottom row -->
        <tr>
            <td  class="tables" id = "table_20">
                <table  >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table> 
            </td>

            <td  class="tables" id = "table_21">
                <table >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table>
            </td>
        
            <td  class="tables" id = "table_22">
                <table >
                    <tr>
                      <td id = "cell_00"></td>
                      <td id = "cell_01"></td>
                      <td id = "cell_02"></td>
                    </tr>
                    <tr>
                      <td id = "cell_10"></td>
                      <td id = "cell_11"></td>
                      <td id = "cell_12"></td>
                    </tr>
                    <tr>
                      <td id = "cell_20"></td>
                      <td id = "cell_21"></td>
                      <td id = "cell_22"></td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    <h2 style="color:lemonchiffon;">Write Your code here! </h2>
    <form style="margin-top:3%;color:white;" action = "uttt.php" method="post">
        <textarea id="code" name="code"></textarea>
        <br>
        <input class="myButton" type="submit" name="submit" value="Submit Code"></input>
	
        
    </form>
	<input class = "myButton" type="button" value="Sample Code" onclick="window.open('snippet.py')">
	<script>
	var id = <?php echo $id; ?>;
	var link ='submissions/'+id+'.error';
		console.log(link);
	</script>

	<input class = "myButton" type="button" value="Error" onclick="window.open(link);">

	


    <?php
      if (isset($_POST['submit'])){
        echo '<div id="buttons">
                <!--button class="myButton" id="pause">Pause</button--!>
                <button class="myButton" id="play">Play</button>
              </div>';
      }
    ?>

</div>
    <script type="text/javascript">
        var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
            mode: {name: "python",
            version: 2,
            singleLineStringErrors: false},
            lineNumbers: true,
            indentUnit: 4,
            tabMode: "shift",
            matchBrackets: true
    }); 
</script>
<script type="text/javascript">
$(document).ready(function(){
  var move1 = <?php echo "'".$move1."'"; ?>;
  
  console.log(id);
  var arr = move1.split(',');

  var i = 0;
  var inc = 0;
  function myloop()
  {
      console.log(i);
      var daddymatrix = arr[i].substring(0,2);
      var babycell = arr[i].substring(2,4);
      if (babycell=="XX"){

      	$("#table_"+daddymatrix).addClass("player1");
      }
      else if (babycell=="OO"){

      	$("#table_"+daddymatrix).addClass("player2");
      }
      else {
	      if (inc==0) {inc = 1 ;}
	      else {inc = 0 ;}
	      var matrixid = "#table_"+daddymatrix;
	      var cellid = " #cell_"+babycell;
	      console.log(matrixid);
	      console.log(cellid);
	      var c =$(matrixid+cellid);
	      var time = 400;
	      //console.log(c);
	      if (inc == 1){
	      	c.html("X");
	      }
	      else {
	      	c.html("O"); 
	      }
    }

    var Timeout;
  
    
      Timeout=setTimeout(function () {
        i++;
        if (i < arr.length)
          myloop();
        
      },500);
    
  $("#pause").click(function(){
    clearTimeout(Timeout);
  });
  }

$("#play").click(function(){
  if (i < arr.length)
          myloop();
  else {
        $.each($(".tables tr td"), function () {
        	$(this).html("");
    	});
	$.each($(".main1 tr td"),function(){$(this).removeClass("player2");});
	$.each($(".main1 tr td"),function(){$(this).removeClass("player1");});
       	i=0;
       	myloop();
  }
  
});
  // for (var i=0;i<arr.length;i++){
  //   console.log(i);
  //   var daddymatrix = arr[i].substring(0,2);
  //     var babycell = arr[i].substring(2,4);
  //     var matrixid = "#table_"+daddymatrix;
  //     var cellid = " #cell_"+babycell;
  //     console.log(matrixid);
  //     console.log(cellid);
  //     var c =$(matrixid+cellid);
  //     var time = 200;
  //     //console.log(c);
  //   if (i%2==0){
  //     setInterval(function(){c.html("O");},);
  //   }
  //   else {
  //     setInterval(function(){c.html("X");},time*i); 
  //   }
  // }


});
</script>
<div id = "instr">
<p><b>Important Instuctions:</b></p>
<ul>
<li>Your function definition should be - "def getMove(self,State,PlayerList=[]):"
<li>For more details on the various functions available to you along with the input output specifiaction, please read the rules carefully from <a style = "color:white;" href = "rules.php">here</a>.
<li>Please ensure that your code is well indented and there are no syntax errors.
<li>You can also locally test your code before submiiting here. Download the zipfile from <a style = "color:white;" href="code.zip" id="button-download">here</a>.
<li>The output you will be shown is for the case when you lose the game against our AI.
<li>The score genreated is for 10 matches between our AI and your bot.
<li>Click on Error button to view if there was any error during your last execution of code.
<li>Do not press play button more than once when the animation is playing
</ul>
</div>
    </body>
</html>