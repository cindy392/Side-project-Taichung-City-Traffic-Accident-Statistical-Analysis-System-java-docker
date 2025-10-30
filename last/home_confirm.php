<body style="background-color:	#FFECEC;"> 
    <?php
    #require("DBconnect.php");

    #用cookie紀錄年份跟月份
    $year=$_POST["year"];
    $month=$_POST["month"];
    setcookie("year",$year,time()+17280);
    setcookie("month", $month,time()+17280);

    #執行python程式去爬蟲跟生成地圖
    $result = exec('search.py ' . $year . ' ' . $month);
    $result2 = exec('map.py ' . $year . ' ' . $month);
    $file="臺中市政府警察局".$year."年".$month."月份交通事故資料.csv";

    //如果檔案存在
    if(file_exists($file)){
            echo "<script type='text/javascript'>";
            echo "alert('載入地圖')";
            echo "</script>";
            echo "<meta http-equiv='Refresh' content='0; url=map.php'>";
    }else{
        echo "<script type='text/javascript'>";
        echo "alert('查無資料，請重新查詢或選擇其他月份')";
        echo "</script>";
        echo "<meta http-equiv='Refresh' content='0; url=home.php'>";
    }

    
   
?>
    

