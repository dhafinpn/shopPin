DHAFIN PUTRA NUGRAHA/2306221112/PBP-B

LINK PWS : https://pbp.cs.ui.ac.id/dhafin.putra/shopPiin

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
