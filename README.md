# Tautan Heroku App

https://adam-pbp.herokuapp.com/

# Tugas 4 PBP

## CSRF Token

Salah satu serangan yang dapat terjadi ke sebuah web app adalah CSRF (Cross-Site Request Forgery). Serangan CSRF adalah serangan yang umumnya menggunakan hyperlink yang berisi HTTP request didalamnya. User ditipu untuk mengklik hyperlink ini, dan request yang tidak diinginkan pengguna terjadi. Dengan menggunakan CSRF token, serangan CSRF dapat dihindari, karena token berisi angka acak yang di-generate server-side, sehingga request palsu dapat diblokir oleh web app.

## Alur Data

Secara umum di HTML, informasi yang dimasukkan ke form dan dikirim ke server merupakan sebuah request POST. Setelah request dikirimkan, server menerima POST yang berisi informasi yang dikirimkan ke user.

# Tugas 3 PBP

## Perbedaan JSON, XML dan HTML

JSON, XML dan HTML merupakan tiga format language yang dapat digunakan untuk memindahkan atau menyimpan data.XML dan HTML adalah contoh dari markup language, yang berarti bahwa isi ditulis menggunakan simbol-simbol atau kata kunci untuk keperluan struktur dokumen. Simbol atau kata kunci digunakan untuk menandakan struktur yang digunakan. 

## Mengapa Data Delivery Penting dalam Pengembangan Aplikasi

Data delivery yang handal dapat dikatakan sudah menjadi sebuah keharusan dalam pengembangan sebuah aplikasi yang berbasis web. Web a

## Implementasi Untuk Tugas 3

# Tugas 2 PBP

## Virtual Environment

Sebuah aplikasi Django bisa saja dibuat tanpa menggunakan virtual environment. Namun penggunaan virtual environment sangat direkomendasikan untuk pengembangan aplikasi Django. Dengan menggunakan env, dapat lebih mudah untuk memisahkan antara proyek, karena setiap proyek bisa saja memiliki versi Django atau Python yang berbeda. Penggunaan env menghindari konflik versi ini karena setiap proyek berada di environment berbeda.

# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.