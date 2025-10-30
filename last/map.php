<html>
    <head>
        <title>台中市交通事故發生地圖</title>
        <link rel="stylesheet" href="home.css">
    </head>
    <body style="background-color:#FFD2D2;">
    <button value="首頁" class="blue" onclick="location.href='home.php'">首頁</button>
    <button value="地圖" class="green" onclick="location.href='map.php'">地圖</button>
    <button value="統計分析" class="yellow" onclick="location.href='analysis.php'">統計分析</button>

        <div style="padding:20px; background-color:	#FFE4E6;">
            <?php
                if(isset($_COOKIE["year"]) && isset($_COOKIE["month"])){
                    $YEAR=$_COOKIE["year"];
                    $MONTH=$_COOKIE["month"];
                    $key=1;
                }else{
                    $YEAR=112;
                    $MONTH=3;
                    $key=0;
                }
                $filename="臺中市政府警察局".$YEAR."年".$MONTH."月份交通事故資料.html";
                echo "<center><h1>".$YEAR."年".$MONTH."月台中市交通事故發生地圖</h1></center>";
                if($key==1){
                    echo "<iframe src=".$filename." width="."100%"." height="."500px"."></iframe>";
                }else{
                    echo "<iframe src="."臺中市政府警察局112年3月份交通事故資料.html"." width="."100%"." height="."500px"."></iframe>";
                }
                ?>
                <!-- <iframe src="map.html" width="100%" height="500px"></iframe> -->
                

            
        
        

    