## Multithread Kullanarak Samurai Sudoku Çözümü

### Problem Tanımı:

  - Projede multithread yapısı kullanılarak verilen samurai sudoku üzerinden çözüm bulunmuştur.
  - Sudoku başlangıç değerleri `sudoku.txt` uzantılı dosyada bulunmaktadır.
  - Verilen değerler dinamik olarak uygulamaya aktarılmıştır.
  - Samurai sudoku 5 tane 9x9’luk sudokudan oluşmaktadır.
<br>
<div align="center">
<img src="https://user-images.githubusercontent.com/24686636/147285948-550ff9c4-13fe-4b19-9687-c403d542b22c.jpeg" width="550">
</div>
<br>

  - Sudoku başlangıç değerleri sudoku.txt dosyasından okunup matrise atanmıştır.

<br>
<div align="center">
<img src="https://user-images.githubusercontent.com/24686636/147285981-427805c9-71e4-456a-b5ed-cb92b3ba58a7.jpeg" width="550">
</div>
<br>

  - Verilen samurai sudoku içindeki her bir sudoku için bir başlangıç noktası seçilerek 5 thread ile çözüme ulaşılmıştır.
  - Sudoku parçalarının çözüm süreleri yazdırılmıştır.
  - Her sudoku parçasının çözüm adımları `txt` klasörü içerisinde oluşturulan .txt uzantılı dosyalarda tutulmuştur.
  - Samurai sudoku üzerinde yapılan değişiklikler koordinat bilgileriyle birlikte `database.txt` dosyasına yazdırılmıştır.

<br>
<div align="center">
<img src="https://user-images.githubusercontent.com/24686636/147286006-5391d5dc-34d3-4161-bc11-4bd73d4ae2b3.jpeg" width="550">
</div>
<br>

  - Son olarak Samurai sudokunun çözümü ekrana yazdırılmıştır.
  - Programın çalışma süresi hesaplanıp yazdırılmıştır.
