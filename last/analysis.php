<html>
    <head>
        <title>台中市交通事故發生統計分析</title>
        <link rel="stylesheet" href="home.css">
    </head>
    <body style="background-color:#FFD2D2;">
    <button value="首頁" class="blue" onclick="location.href='home.php'">首頁</button>
    <button value="地圖" class="green" onclick="location.href='map.php'">地圖</button>
    <button value="統計分析" class="yellow" onclick="location.href='analysis.php'">統計分析</button>

        <div style="padding:20px; background-color:	#FFE4E6;">
            <center><h1>112年3月台中市交通事故發生統計分析</h1></center>
            <center><strong>這個月</strong><center></br>
            <?php
            $result = exec('analysis.py ' ,$output);
            //這個月的表格
            echo "<center>";
            echo "<table border='2'>";
            echo "
                <td align="."center"." bgcolor ="."#FF9797"."><strong>事件數</strong></td>
                <td align="."center"." bgcolor ="."#FF9797"."><strong>死亡數</strong></td>
                <td align="."center"." bgcolor ="."#FF9797"."><strong>受傷數</strong></td>";
                echo "<tr>";
                echo "<td align="."center"."><strong>".$output[2]."</strong></td>
                <td align="."center"."><strong>".$output[0]."</strong></td>
                <td align="."center"."><strong>".$output[1]."</strong></td>";    
                echo "</tr>";
                echo "</table>";  
                echo "</center><br><br>";

            //上月差異表格
            echo "<center><strong>與上月相比</strong><center></br>";
            echo "<center>";
            echo "<table border='2'>";
            echo "
                <td align="."center"." bgcolor ="."#FF9797"."><strong>事件數</strong></td>
                <td align="."center"." bgcolor ="."#FF9797"."><strong>死亡數</strong></td>
                <td align="."center"." bgcolor ="."#FF9797"."><strong>受傷數</strong></td>";
                echo "<tr>";
                echo "<td align="."center"."><strong>".$output[5]."</strong></td>
                <td align="."center"."><strong>".$output[3]."</strong></td>
                <td align="."center"."><strong>".$output[4]."</strong></td>";    
                echo "</tr>";
                echo "</table>";  
                echo "</center><br><br>";
            //去年差異表格
            echo "<center><strong>與去年同月相比</strong><center></br>";
            echo "<center>";
            echo "<table border='2'>";
            echo "
                <td align="."center"." bgcolor ="."#FF9797"."><strong>事件數</strong></td>
                <td align="."center"." bgcolor ="."#FF9797"."><strong>死亡數</strong></td>
                <td align="."center"." bgcolor ="."#FF9797"."><strong>受傷數</strong></td>";
                echo "<tr>";
                echo "<td align="."center"."><strong>".$output[8]."</strong></td>
                <td align="."center"."><strong>".$output[6]."</strong></td>
                <td align="."center"."><strong>".$output[7]."</strong></td>";    
                echo "</tr>";
                echo "</table>";  
                echo "</center><br><br>";
            
            //折線圖
            echo "<center><strong>事件數一年內趨勢折線圖</strong><center></br>";
            echo "<center><strong>2022/04 - 2023/03</strong><center></br>";
            echo "<img src="."plot.png"." alt="."事件數一年間趨勢折線圖"."><br><br>";

            echo "<center><strong>死亡數一年內趨勢折線圖</strong><center></br>";
            echo "<center><strong>2022/04 - 2023/03</strong><center></br>";
            echo "<img src="."plot_d.png"." alt="."事件數一年間趨勢折線圖"."><br><br>";

            echo "<center><strong>受傷數一年內趨勢折線圖</strong><center></br>";
            echo "<center><strong>2022/04 - 2023/03</strong><center></br>";
            echo "<img src="."plot_h.png"." alt="."事件數一年間趨勢折線圖"."><br><br>";

            //直方圖
            echo "<center><strong>事件數地區直方圖</strong><center></br>";
            echo "<center><strong>2023/03</strong><center></br>";
            echo "<img src="."plot_place.png"." alt="."事件數地區直方圖"."><br><br>";

                
  