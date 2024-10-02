DHAFIN PUTRA NUGRAHA/2306221112/PBP-B

LINK PWS : https://pbp.cs.ui.ac.id/dhafin.putra/shoppiin

JAWABAN TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Pertama buatlah direktori baru dan mengaktifkan virtual environmentnya dengan perintah python -m venv env dan env\Scripts\activate
   Buatlah satu file yang berisi dependencies dengan nama requirements.txt dan dowloand dengan cara pip install -r requirements.txt
   Setelah itu buat project djangonya dengan cara django-admin startproject <nama_project> .
   Tambahkan "localhost", "127.0.0.1" pada ALLOWED_HOSTS di settings.py untuk keperluan deployment
   Jalankan server Django dengan perintah python manage.py runserver
   Buka http://localhost:8000 untuk melihat apakah berhasil atau tidak
   Membuat aplikasi main dalam Proyek dengan cara jalankan python manage.py startapp main
   Mendaftarkan aplikasi main pada INSTALLED_APPS di settings.py
   Buat direktori bernama templates didalam direktori main dan buat file main.html yang akan berisi template bagaimana tampilan web nanti
   Mengubah models.py sesuai dengan yang dibutuhkan atau diinginkan
   Membuat dan mengaplikasikan Migrasi Model dengan cara menjalankan perintah python manage.py makemigrations dan penerapan migrasi dengan python manage.py migrate
   Tambahkan code from django.shortcuts import render pada views.py di dalam aplikasi main
   Menambahkan fungsi show_main yang akan mengembalikan tampilan yang sesuai
   Konfigurasi url agar aplikasi main dapat diakses melalui web
   jalankan proyek
   Melakukan Deploy pada Adaptable
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![image](https://github.com/user-attachments/assets/b312eb51-92b7-4a95-8441-e326e585f86e)

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
   Git berguna untuk membantu para penggunanya mengecek perubahan apa saja yang telah dilakukan dan membantu pengguna untuk bekerja sama sebagai tim lebih mudah.
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Menurut saya karena Django dibangun mennggunakan python dan kami sebagai mahasiswa sudah mempelajari python dari semester 1, sehingga tidak perlu belajar syntax yang terlalu banyak dan lebih fokus ke pengembangan webnya
5. Mengapa model pada Django disebut sebagai ORM?
   Django disebut sebagai ORM karenan memungkinkan pengembang untuk bekerja dengan data di database menggunakan objek dalam bahasa pemrograman lain seperti Python dibanding menggunakan SQL.


JAWABAN TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   Data delivery sangat penting dalam pengimplementasian sebuah platform karena data delivery berguna untuk meningkatkan efisiensi dengan memastikan bahwa data yang diperlukan user atau aplikasi tersedia secara tepat waktu dan dalam format yang sesuai.
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   Keduanya memiliki fungsi yang sama-sama bermanfaat, namun JSON memiliki syntax dan tampilan yang lebih mudah untuk dibaca yang membuat JSON lebih populer dibanding XML yang lebih kompleks.
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
   Method is_valid() dapat digunakan untuk memvalidasi data yang diberikan pada form valid atau tidak. jika data valid maka akan mengembalikan nilai true sehingga bisa mengakses data yang sudah bersih. Jika data tidak valid maka akan mengembalikan nilai false dan bisa memberikan pesan kesalahan yang spesifik. Method ini berguna untuk memastikan setiap data yang masuk sudah sesuai dengan ketentuan yang diterapkan.
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
   csrf_token berguna untuk sekuritas dari segala bentuk serangan yang dapat terjadi. ini dapat di eksploitasi oleh penyerang untuk melakukan aksi tanpa sepengetahuan pengguna. penyerang bisa memalsukan permintaan ke server dan mengambil alih sesi pengguna.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Pertama buatlah file baru bernama forms.py di direktori main, dan mengisi dengan 2 variable yaitu model dan fields.
   Melakukan import pada bagian views.py
   Menambahkan beberapa fungsi pada views.py yang akan berukan untuk menyimpan data dan menampilkannya pada web nanti.
   Membuat file html baru yang ada pada subdirektori templates yang ada di direktori main.
   Menambahkan 4 fungsi pada views untuk melihat data yang sudah ditambahkan dalam bentuk XML, JSON, XML by ID, dan JSON by ID.
   Commit dan push ke github

JAWABAN TUGAS 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
   HttpResponseRedirect() merupakan subclass dari HttpResponse yang digunakan untuk mengirimkan respons pengalihan ke pengguna. Sedangkan redirect() merupakan fungsi pendek yang lebih mudah digunakan dan fleksibel untuk mengatur pengalihan.
2. Jelaskan cara kerja penghubungan model Product dengan User!
   Penghubungan model product dengan user dapat dilakukan dengan membuat foreign key pada model product yang dihubungkan ke model user. Dengan cara ini, setiap data pada model product akan terhubung dengan data pada model user.
3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    Authentication dan authorization merupakan dua konsep kunci dalam keamanan aplikasi web. Authentication memverifikasi identitas pengguna, contohnya saat login dengan username dan password. Authorization menentukan hak akses pengguna setelah terverifikasi, seperti apa yang bisa mereka lihat atau lakukan dalam sistem. Di Django, authentication diatur melalui form login dan backend otentikasi, sedangkan authorization dikelola melalui izin yang dapat diatur pada pengguna atau grup.
4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
   Django mengingat pengguna yang telah login dengan menggunakan session. Saat pengguna login, Django akan membuat session yang berisi informasi pengguna, seperti id dan username. Session ini akan disimpan di server dan dikirimkan ke pengguna dalam bentuk cookie. Pengguna akan menyimpan cookie ini di browser mereka dan mengirimkannya kembali ke server setiap kali mereka melakukan request. Django akan memeriksa cookie ini untuk mengidentifikasi pengguna yang telah login. Kegunaan lain dari cookies adalah untuk menyimpan informasi pengaturan pengguna. Tidak semua cookies aman digunakan. Cookies yang tidak dienkripsi atau tidak diotentikasi dapat disalahgunakan oleh penyerang untuk mencuri informasi sensitif pengguna atau melakukan serangan lainnya.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Pertama buatlah fungsi untuk register, login, dan logout di views.py. Khusus untuk register dan login buatlah satu buat file html baru di direktori templates yang berada di main dengan nama ragister.html dan login.html. untuk logout tinggal tambahkan logout button di main.html. setelah itu lakukan import ke urls.py dan masukan url path ke dalam urlspattern di urls.py
   Kedua menghubungkan model product dengan user dengan cara import user pada models.py dan menambahkan foriegn key pada class yang ada di models.py.
   Untuk menampilkan last login pada fungsi show main tambahkan 'last_login': request.COOKIES['last_login'] yang akan menampilkan kapan terakhir user login.
   
JAWABAN TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutannya adalah sebagai berikut :
a. Inline Styles, gaya yang langsung ditulis pada elemen HTML menggunakan atribut style merupakan prioritas paling tinggi
b. ID Selector, Selector yang menggunakan ID HTML memiliki prioritas lebih tinggi dibanding class.
c. Class, Pseudo-class, dan Attribute Selector, Selector yang menggunakan class , pseudo-class atau attribute selector berada di urutan berikutnya dalam hal prioritas

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Tentu sangat penting karena pada saat ini hampir semua orang setidaknya memiliki 2 device dengan ukuran yang berbeda dan responsive design ini harus ada supaya dapat digunakan di device manapun. Contoh aplikasi yang sudah menerapkannya seperti twitter (x) dan instagram. 

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin merupakan ruang di luar elemen yang mempengaruhi seberapa jauh elemen terebut dari elemen lain. Dapat di implementasikan dengan properti margin.
Border adalah ruang disekitar elemen yang membungkus padding Dapat di implementasikan dengan properti border.
Padding adalah ruang di dalam elemen itu sendiri. Dapat di implementasikan dengan properti padding.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox adalah metode layout CSS yang dirancang untuk menyusun elemen dalam satu dimensi. Flexbox memudahkan dalam mengatur posisi, ukuran, dan distribusi dalam sebuah kontainer

Grid Layout merupakan metode layout dua dimensi yang membuat kita dapat membuat tata letak lebih kompleks. Grid dapat membuat layout berbasis baris dan kolom secara bersamaan dengan kontrol penuh terhadap elemen-elemen di dalamnya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Pertama buatlah 2 fungsi baru untuk edit review dan juga delete review
Setelah itu membuat navbar yang dapat disesuaikan dengan design manapun
Melakukan kustomisasi terhadap bagian main, login, register, create review, dan edit review sesuai dengan konsep yang saya miliki menggunakan tailwind css
Menyesuaikan layout dan posisi agar terlihat rapih
