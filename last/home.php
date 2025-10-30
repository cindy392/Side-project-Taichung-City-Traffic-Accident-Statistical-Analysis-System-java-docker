<html>
    <head>
        <title>台中市交通事故統計分析系統</title>
        <link rel="stylesheet" href="home.css">
    </head>
    <body style="background-color:#FFD2D2;">
    <button value="首頁" class="blue" onclick="location.href='home.php'">首頁</button>
    <button value="地圖" class="green" onclick="location.href='map.php'">地圖</button>
    <button value="統計分析" class="yellow" onclick="location.href='analysis.php'">統計分析</button>

        <div style="padding:20px; background-color:	#FFE4E6;">
            <center><h1>台中市交通事故統計分析系統</h1></center>
            <center><form action="home_confirm.php" method="post" style="width: 80%;" enctype="multipart/form-data">
            <strong>年份</strong></br>
            <select name="year" required>
                <option>112</option>
                <option>111</option>
                <option>110</option>
                <option>109</option>
                <option>108</option>
                <option>107</option>
            </select><br><br>
            <strong>月份</strong></br>
            <select name="month" required>
                <option>1</option>
                <option>2</option>
                <option>3</option>
                <option>4</option>
                <option>5</option>
                <option>6</option>
                <option>7</option>
                <option>8</option>
                <option>9</option>
                <option>10</option>
                <option>11</option>
                <option>12</option>
            </select><br><br>
                <input type="submit"><br><br>
            </form></center>
        <?php
            if(isset($_COOKIE["year"]) AND isset($_COOKIE["month"])){
                $YEAR=$_COOKIE["year"];
                $MONTH=$_COOKIE["month"];
                
                echo "<center><font size=\"4\" color=\"#FF2D2D\"><strong>感謝～回到本系統～</strong></center></font>";
                //echo "<center><strong><h3>感謝</h3></strong><center><h3>".$UID."</h3></center><center><strong><h3>～回到本系統～</h3></strong></center>";
            }else{
                $_COOKIE["year"]='112';
                $_COOKIE["month"]='3';
                echo "<center><strong>～歡迎初次來本系統～</strong></center>";
            }
            ?>
            
        
        

    