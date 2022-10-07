# Tautan Heroku App

https://adam-pbp.herokuapp.com/

# Tugas 5 PBP

## Inline, Internal, External CSS

Inline, internal dan CSS external adalah tiga cara berbeda yang dapat digunakan untuk mengimplementasikan CSS di sebuah halaman web. Ketiga implementasi ini dapat digabungkan dan digunakan secara bersamaan

**Inline** berarti bahwa formatting yang dilakukan CSS ditulis langsung di dokumen .HTML, di samping element yang ingin ditambahkan style modifikasi. Formatting dilakukan di tag awal HTML. Contohnya:

```html
<p style="color:blue;">Contoh dari tulisan.</p>
```

CSS ditambahkan menggunakan argumen style dengan attribute color blue, sehingga tulisan akan ditampilkan dengan warna biru di browser.

**Internal** Di implementasi internal, style dari css dimasukkan kedalam `<style> CSS </style>` di bagian head, sehingga tidak perlu untuk memformat setiap element yang ada di file HTML.

```html
<head>
<style>
body {
  background-color: yellow;
}
h1 {
  color: green;
}
</style>
</head>
```

Contoh style di atas akan menerapkan warna background kuning dan semua warna Heading 1 menjadi hijau.

**External** Di implementasi ini style sheet tidak berada di file HTML, melainkan berada di file lain yang berextension .CSS . Ini memudahkan modifikasi.

## HTML Tags

Pada dasarnya, syntax dari HTML, yang merupakan bahasa markup, menggunakan tag-tag yang dikelilingi oleh simbol <> dan tag penutup </>. Text diantara dua tag merupakan bagian yang akan diproses oleh browser sesuai tagnya.

### Contoh-contoh Tag HTML

Tag selalu dikelilingi tanda `<TAG>`

1. **head** digunakan untuk menandai section head di file
2. **body** menandai bagian isi utama di file HTML
3. **h1, h2, h3, p** menandai tulisan heading 1,2,3 dan paragraf
4. **div**  merupakan pemisah untuk melakukan containerization dari kumpulan element
5. **br** memasukkan line break di text
6. **b, i** Membuat file menjadi bold atau italics
7. **style** memuat CSS yang digunakan di suatu file

## Contoh CSS Selector

Terdapat 5 CSS selector yang dapat digunakan untuk memilih elemen yang akan di-style

1. Element Selector
2. Group Selector
3. Class Selector
4. Id Selector
5. Universal Selector

## Implementasi pada Tugas 5

Implementasi dari CSS pada tugas 5 ini menggunakan framework Bootstrap yang menggunakan sumber external dari CDN yang dimiliki oleh Bootstrap. Link stylesheet diletakkan pada /templates/base.html di directory utama project Django. Bootstrap merupakan framework yang salah satu fiturnya adalah responsive, sehingga fitur ini dapat langsung diimplementasikan.