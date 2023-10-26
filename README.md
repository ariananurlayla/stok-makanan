## Tugas Individu PBP

# [stok-makanan](https://stok-nyamnyam.adaptable.app/)

<details>
<summary> Tugas 6 </summary>

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming menjalankan tugas satu per satu secara berurutan dan menunggu setiap tugas selesai sebelum melanjutkan ke tugas berikutnya. Asynchronous programming memungkinkan beberapa tugas berjalan bersamaan tanpa harus menunggu tugas sebelumnya selesai. Ini membuat program tetap responsif dan efisien saat menangani operasi-operasi yang membutuhkan waktu lama, seperti I/O atau panggilan jaringan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma event-driven programming adalah pendekatan dalam pengembangan perangkat lunak di mana program merespons peristiwa atau kejadian yang terjadi. Dalam konteks JavaScript dan AJAX, program merespons peristiwa-peristiwa tertentu, seperti klik tombol atau pembaruan data dari server, tanpa harus menunggu operasi selesai secara sinkron.

```
        function addItem() {
            fetch("{% url 'main:create_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshItems)

            document.getElementById("form").reset()
            return false
        }

        document.getElementById("button_add").onclick = addItem <----- event listener onclick pada button dengan id button_add yang akan memanggil function addItem() bila ada event ditekan
```

## Jelaskan penerapan asynchronous programming pada AJAX.

AJAX (Asynchronous JavaScript and XML) memungkinkan browser berkomunikasi dengan server secara asynchronous, artinya halaman web dapat mengirim atau menerima data dari server tanpa harus me-refresh atau menghentikan eksekusi kode JavaScript utama. Dengan menggunakan teknik ini, aplikasi web dapat tetap responsif dan interaktif, memungkinkan pengguna berinteraksi dengan halaman web tanpa harus menunggu waktu lama untuk pemrosesan data dari server. Hal ini meningkatkan pengalaman pengguna dengan membuat aplikasi web terasa lebih cepat dan responsif.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

### Perbandingan Fetch API dan jQuery AJAX

| Kriteria           | Fetch API                                                         | jQuery AJAX                                                                               |
| ------------------ | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Sintaksis**      | Modern, menggunakan Promise dan async/await.                      | Lebih ringkas dan mudah dipahami.                                                         |
| **Ringan**         | Ringan, hanya membutuhkan beberapa baris kode.                    | Memuat library tambahan, cenderung lebih berat.                                           |
| **Fleksibilitas**  | Dapat mengelola berbagai jenis request dan response.              | Terbatas pada fitur dasar AJAX.                                                           |
| **Dukungan**       | Didukung di semua browser modern.                                 | Memiliki penanganan perbedaan browser, namun tidak semua fitur didukung di semua browser. |
| **Kompatibilitas** | N/A                                                               | Menangani perbedaan antar browser dengan baik.                                            |
| **Kelebihan**      | Fleksibel, modern, dan efisien.                                   | Sintaksis mudah dipahami, kompatibilitas baik.                                            |
| **Kekurangan**     | Membutuhkan penanganan lebih lanjut untuk perbedaan browser lama. | Lebih berat jika hanya digunakan untuk AJAX requests saja.                                |
| **Popularitas**    | Semakin populer di komunitas pengembang JavaScript.               | Sudah lama populer, banyak sumber dan dokumentasi.                                        |

**Pendapat:** Pemilihan antara Fetch API dan jQuery AJAX tergantung pada kebutuhan proyek dan preferensi pengembang. Fetch API menawarkan pendekatan yang lebih modern dan efisien, sementara jQuery AJAX menyediakan sintaksis yang lebih ringkas dan mudah dipahami, terutama untuk pengembang yang sudah terbiasa dengan jQuery.

## Cara Implementasi

Mengimplementasikan AJAX GET:

- Membuat fungsi `getItems` untuk melakukan fetch pada berkas `main.html` yang memanggil suatu fungsi di `views.py`.
- Mengambil item pengguna tersebut dan mengembalikannya dalam format JSON di `views.py`.
- Membuat fungsi untuk memperbarui tampilan kartu. Fungsi ini akan memanggil fungsi `getItems` dan memindahkan kode pembuatan kartu HTML ke dalam fungsi `refreshItems`. Fungsi ini membuat kartu untuk setiap item.
- Routing semua fungsi baru di `views.py` pada `urls.py`.

views.py

```
...
def get_item_json(request):
    item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item))

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
...
```

urls.py

```
...
from main.views import  get_item_json, create_ajax
...
urlpatterns = [
...
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax')
]
```

Mengimplementasikan AJAX POST:

- Membuat formulir modal dan membuat tombol untuk membuka modal tersebut.
- Membuat fungsi `create_ajax` yang berfungsi untuk menambahkan item di `views.py`. Fungsi ini mengambil data dari modal, membuat objek Item baru dengan data yang diperoleh, dan menyimpannya ke database.
- Routing untuk fungsi tersebut pada `urls.py`.
- Menghubungkan formulir ke fungsi `create_ajax` dengan membuat suatu fungsi menggunakan JavaScript. Fungsi ini adalah `addItem` dan akan melakukan fetch terhadap `create_ajax` dengan mengirimkan permintaan HTTP menggunakan metode POST dan tubuh berupa data-data yang dikirimkan dari modal. Kemudian memanggil fungsi `refreshItems` untuk memperbarui daftar item berikutnya dan mengosongkan kolom input pada modal.

Mengumpulkan berkas statis (seperti pada Tutorial 2):

- Menambahkan `STATIC_ROOT = os.path.join(BASE_DIR, 'static')` pada berkas `settings.py` (path direktori di mana semua berkas statis yang dikumpulkan oleh `collectstatic` akan disalin).
- Menjalankan perintah `python manage.py collectstatic` di terminal.

Menjawab pertanyaan Tugas Individu 6.

</details>

<details>
<summary> Tugas 5 </summary>

## Manfaat dari setiap element selector dan waktu yang tepat untuk menggunakannya

- Element selector memungkinkan kita untuk mengubah properti untuk semua elemen dengan tag yang sama. Tepat digunakan jika ingin menerapkan style/gaya umum dari semua elemen dengan jenis yang sama. Contoh, memodifikasi semua `<h1>` atau judul level 1.

```
h1 {
    font-size: 24px;
    color: #ff0000;
}
```

- ID selector digunakan untuk memilih elemen tertentu dengan atribut ID yang bersifat unik sehingga memungkinkan pemilihan elemen yang spesifik.

```
#header {
  background-color: #f0f0f0;
  margin-top: 0;
  padding: 20px 20px 20px 40px;
}
```

- Class selector memungkinkan kita untuk memilih elemen berdasarkan class tertentu. Contohnya dapat digunakan untuk mengelompokkan elemen dengan karakteristik serupa untuk menerapkan gaya secara bersamaan.

```
.content_section {
  background-color: #3696e1;
  margin-bottom: 30px;
  color: #000000;
  font-family: cursive;
  padding: 20px 20px 20px 40px;
}
```

## HTML5 Tag

- `<title>` -> untuk judul web
- `<body>` -> untuk bagian isi dari web
- `<header>` -> untuk mengelompokkan elemen-elemen yang berada di bagian atas halaman atau bagian dari suatu konten.
- `<tr>` -> mendefinisikan setiap baris dalam tabel
- `<td>` -> mendefinisikan sel data yang merupakan konten utama dalam tabel. Sel berada di dalam baris
- `<button>` -> untuk membuat tombol
- `<h1> <h2> <h3> dst` -> untuk membuat header
- `<p>` -> untuk membuat paragraf
- `<br>` -> memasukan satu break line

## Perbedaan Margin dan Padding

- Margin: digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya. Margin tidak mempunyai warna background dan atribut visual lain.
- Padding: digunakan untuk mengatur jarak antara isi konten dengan batas tepi elemen. Padding dapat memiliki warna latar belakang yang sama dengan elemen tersebut, sehingga bagian padding akan berwarna sesuai dengan elemen tersebut.

## Perbedaan antara framework CSS Tailwind dan Bootstrap

Bootstrap tepat digunakan jika ingin mempercepat proses dan konsistensi desain yang telah didefinisikan sebelumnya, tetapi kurang fleksibel. Jika dibutuyhkan fleksibilitas lebih dalam proses design, Tailwind mungkin lebih baik untuk dipilih. Bootstrap memiliki banyak komponen built in yang siap untuk digunakan. Di sisi lain, Tailwind menyediakan komponen yang lebih mendasar sehingga mungkin akan memerlukan kustomisasi dalam pemanfaatannya.

## Cara Implementasi Kostumisasi Desain

Saya melakukan proses desain pada HTML sesuai kebutuhan dari masing-masing file. Saya menggunakan CSS biasa dengan internal style sheet. Kemudian, saya membuat navbar dengan melakukan penyesuaian sesuai kebutuhan saya, saya menggunakan template navbar dari website Bootstrap yang disediakan pada tutorial.

</details>

<details>
<summary> Tugas 4 </summary>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

`UserCreationForm` adalah formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Form ini meng-handle informasi yang dibutuhkan dalam proses pembuatan _user_ sehingga _programmer_ tidak perlu membuat kode dari awal. Kelebihan dari `UserCreationForm` adalah menyediakan formulir bawaan yang memudahkan pembuatan _user_ baru dengan validasi otomatis sehingga akan menghemat waktu pemrograman. Namun, kekurangannya adalah kurangnya fleksibilitas untuk disesuaikan sepenuhnya dengan kebutuhan formulir registrasi yang kompleks.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

`Autentikasi` adalah proses verifikasi identitas pengguna yang mencoba mengakses sistem. Contoh: proses _login_.

`Otorisasi` adalah proses pengecekan izin terhadap sumber daya yang dapat diakses oleh pengguna yang sedang diotentikasi. Contoh: perbedaan sumber daya yang dapat diakses oleh roles Asdos dan Mahasiswa dalam sebuah server Discord suatu mata kuliah karena ada batasan yang telah ditentukan.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah penyimpanan data informasi dari aplikasi web. Informasi yang disimpan, seperti sesi, preferensi, atau identifikasi pengguna. Identifier unik dari pengguna ini akan disimpan dan diolah oleh Django menggunakan cookies. Cookies akan mengirimkan identifier ke perangkat yang digunakan oleh pengguna saat mereka mengakses aplikasi web. Identifier digunakan untuk mengaitkan pengguna dengan data sesi yang mereka miliki pada server.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan cookies belum tentu aman secara default. Cookies disimpan/dikirimkan ke perangkat pengguna sehingga pihak yang memiliki akses terhadap perangkat tersebut juga dapat mengakses cookies yang ada di dalamnya. Cookies dapat dicuri atau disadap jika tidak dienkripsi dengan baik. Selain itu, terdapat ancaman lain yang mungkin muncul dari penggunaan cookies dalam pengembangan web. Salah satunya adalah CSRF (_Cross-Site Request Forgery_).

## Cara Implementasi

1. Mengaktifkan _virtual environment_: `env\Scripts\activate.bat`

2. Membuat form dan fungsi register, login, serta logout pada `views.py`. Kemudian, melakukan _routing_ pada `urls.py` dengan mengimpor fungsi-fungsi yang digunakan dan menambahkan path url.

3. UserCreationForm membantu membuat formulir registrasi dan akun pengguna dalam aplikasi web ketika data form di-submit. Dilakukan validasi _input_ form tersebut. Jika sesuai, maka data yang diperoleh dari form akan disimpan dan mengarahkan pengguna ke halaman login.

4. Membuat `register.html` dan `login.html` seperti yang diajarkan pada tutorial.

5. Pada proses _login_, program meminta _input_ username dan password untuk kemudian dilakukan autentikasi. Jika autentikasi berhasil, akan dilakukan proses _login_ dan mengarahkan pengguna ke halaman main. Saya juga menambahkan restriksi agar halaman main hanya bisa diakses oleh pengguna yang sudah _login_ dengan _decorator_ `login_required`.

6. Pada proses _logout_, data cookie `last_login` pengguna akan dihapus dan pengguna dikembalikan ke halaman login.

7. Menambahkan tombol-tombol pada `main.html`, seperti tombol _logout_, _add new item_, mengurangi kuantitas item, menambah kuantitas item, dan menghapus suatu item.

8. Untuk menampilkan detail informasi, saya menambahkan `response.set_cookie('last_login', str(datetime.datetime.now()))` dalam _dictionary context function_ `show_main` yang di-pass ke `main.html` untuk informasinya dirender. Saya juga mengubah _value_ dari `name` dalam _dictionary context function_ `show_main` untuk mengirimkan _username_ dari pengguna yang sedang _login_.

9. Menjalankan server dengan `python manage.py runserver` dan membuat akun dengan username 'Ariana'. Kemudian, menghubungkan model `Item` dan `User`.

10. Melakukan migrasi dan mencoba mengakses halaman web yang telah dibuat.

11. Menjawab pertanyaan-pertanyaan pada Tugas 4.

</details>

<details>
<summary> Tugas 3 </summary>

## Perbedaan antara _form_ `POST`dan `GET` dalam Django

Method `POST` merupakan method protokol HTTP untuk mengirimkan data ke server. Pada method `POST`, data dikirim sebagai dari body request sehingga tidak terlihat dalam URL. Method ini sesuai untuk mengirimkan data yang lebih besar jika dibandingkan dengan method `GET`, seperti _upload file_.

Method `GET` merupakan method protokol HTTP untuk mengambil data dari server. Berbeda dengan `POST`, method `GET` tidak cocok untuk mengirimkan data sensitif sebab data yang dikirimkan melalui method `GET` terlihat dalam URL (data ditambahkan sebagai parameter query). Kapasitas data method `GET` lebih kecil dibandingkan method `POST`. Oleh karena itu, method ini lebih sesuai untuk mendapatkan data yang relatif kecil, seperti saat _membuka halaman web yang bersifat publik_.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data

#### XML (eXtensible Markup Language)

XML digunakan untuk mengorganisir data dalam hierarki yang terstruktur, seperti mengorganisir berkas dalam folder dan subfolder komputer. Tag pembuka dan penutup yang mendefinisikan elemen dan atribut (sintaks XML dapat dianalogikan seperti HTML yang menyimpan data dalam bentuk tree node), memungkinkan fleksibilitas dalam mendefinisikan format data yang sesuai dengan kebutuhan aplikasi.

- XML biasanya digunakan untuk data yang perlu diorganisir dengan struktur yang kompleks karena menggunakan tag pada setiap elemen data. Contoh penggunaannya, seperti konfigurasi aplikasi atau pertukaran data antarsistem yang berbeda.

#### JSON (JavaScript Object Notation)

JSON digunakan untuk menyimpan data dalam format objek dengan pasangan `key-value`, seperti format daftar kontak di ponsel. Fomat yang relatif singkat dan intuitif tersebut memudahkan manusia dalam membaca dan memahaminya.

- JSON cocok untuk pertukaran data dalam pengembangan web karena sederhana, ringkas, dan relatif mudah di-parsing. JSON menggunakan `dictionary` dan `list` sebagai _container_ sehingga mudah dibaca oleh mesin juga. Data dikirim dalam bentuk JavaScript sehingga lebih mudah dimanipulasi sehingga JSON sering digunakan.

#### HTML (HyperText Markup Language)

HTML digunakan untuk mengirimkan tampilan halaman web, dapat diibaratkan seperti membangun struktur rumah dengan kamar, pintu, dan jendela. `HTML` lebih cocok jika client-nya adalah manusia, bukan aplikasi yang mengambil data (karena diperlukan parsing). Proses parsing akan memakan waktu dan kurang efisien.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

`JSON` sering digunakan karena penyajian data yang lebih sederhana dari `XML` sehingga lebih efisien. Ditambah, format ini lebih mudah dibaca oleh manusia dan mesin, seperti yang telah disebutkan sebelumnya.

## Cara Implementasi

1. Mengaktifkan _virtual environment_: `env\Scripts\activate.bat`

2. Membuat direktori `templates` di _root folder_. Di dalam folder tersebut, saya menambahkan `base.html` sebagai template.

3. Membuat `forms.py` di `main` yang mengimplementasikan `django._form_s` untuk membantu penyusunan struktur _input_ _form_ yang akan dibuat. Kode yang saya gunakan mirip dengan yang telah diajarkan saat tutorial. Perbedaanya terdapat pada nama model yang sekarang menjadi `Item` dan sebuah field `amount` yang menggantikan field `price`.

```
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```

4. Memodifikasi `views.py` dengan menambahkan fungsi-fungsi yang dibutuhkan. Fungsi dalam `views.py`

- `show_main` --> menampilkan data `Item` melalui _form_
- `create_product` --> mengelola pembuatan produk
- `show_html` --> menampilkan data dalam bentuk HTML
- `show_xml` --> menampilkan data dalam bentuk XML
- `show_json` --> menampilkan data dalam bentuk JSON
- `show_xml_by_id` --> menampilkan data dalam bentuk XML berdasarkan id tertentu
- `show_json_by_id` --> menampilkan data dalam bentuk JSON berdasarkan id tertentu

5. Melakukan routing dengan mengimpor fungsi-fungsi yang ada pada `views.py` dalam `urls.py` yang terdapat pada `main` folder. Kemudian, menambahkan _path url_ untuk setiap fungsi dalam `urls.py`. Hal ini bertujuan untuk mengakses fungsi-fungsi yang sudah diimport sebelumnya.

6. Membuat berkas `create_product.html` di `main/templates`, seperti pada tutorial.

7. Memodifikasi `main.html` pada `main/templates` untuk menampilkan data produk dalam bentuk table dan menambahkan tombol `Add New Product` yang akan _redirect_ ke halaman _form_.

## Screenshots Postman

### HTML

![](/img_tugas3/html-1.png)
![](/img_tugas3/html-2.png)
![](/img_tugas3/html-3.png)

### XML

![](/img_tugas3/xml.png)

### JSON

![](/img_tugas3/json.png)

### XML by ID

![](/img_tugas3/xml_id1.png)
![](/img_tugas3/xml_id2.png)

### JSON by ID

![](/img_tugas3/json_id1.png)
![](/img_tugas3/json_id2.png)

</details>

<details>
<summary> Tugas 2 </summary>

## 1. Cara Implementasi

1. Memilih direktori lokal yang akan menyimpan proyek Git dan melakukan inisiasi repositori baru dengan berintah `git init`.

- Menghubungkan keduanya dengan perintah `git remote add origin <url_repo_github>`.
- Membuat virtual environment untuk projek baru ini dengan `python -m venv env` dan mengaktifkannya `env\Scripts\activate.bat`.
- Pada direktori yang sama, saya menambahkan berkas `requirements.txt` yang berisi dependencies sebagai berikut:
  ```
  Django
  Gunicorn
  Whitenoise
  psycopg2-binary
  requests
  urllib3
  ```
- Memasang dependencies dengan perintah `pip install -r requirements.txt`
- Membuat proyek Django baru Bernama `stok_makanan` dengan perintah `django-admin startproject stok_makanan .`
- Menambahkan file `.gitignore`
- Mengatur akses aplikasi web dengan menambahkan `\*` pada `ALLOWED_HOST` pada `settings.py`
- Mendaftarkan `main` dalam proyek _stok makanan_:
  - Membuat aplikasi `main` dalam proyek `stok_makanan` dengan `python manage.py startapp main`
  - Menambahkan `main` ke `INSTALLED_APPS` dalam `settings.py`
- Menambahkan direktori `template` pada direktori `main`
- Menambahkan file `main.html` dalam direktori `templates` pada aplikasi `main` yang nantinya akan menampilkan data aplikasi
- Menambahkan fungsi `show_main` pada `views.py` yang ada pada direksori aplikasi `main` yang berfungsi mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
- Melakukan routing URL
  - Mengonfigurasi routing URL aplikasi main agar dapat diakses melalui peramban web
    - Membuat berkas `urls.py` dalam direktori `main`, seperti yang telah diberikan saat tutorial
  - Mengonfigurasi routing URL proyek untuk menghubungkannya ke tampilan `main`
    - Menambahkan rute URL pada `urls.py` dalam direktori proyek `stok_makanan`, seperti yang telah diberikan saat tutorial
- Mengubah berkas `models.py` dalam aplikasi `main` sesuai kebutuhan
  - Menambahkan `Item` dengan atribut `name`, `amount`, dan `description`
    - name sebagai nama item dengan tipe CharField.
    - amount sebagai jumlah item dengan tipe IntegerField.
    - description sebagai deskripsi item dengan tipe TextField.
- Menambahkan unit test `tests.py` pada direktori aplikasi `main`, seperti yang diberikan pada tutorial
- Melakukan deployment proyek pada Adaptable.io, seperti yang dicontohkan pada tutorial dengan melakukan penyesuaian yang dibutuhkan dan start command `python manage.py migrate && gunicorn stok_makanan.wsgi`

## 2. Bagan

![Bagan](bagan.png)

Penjelasan bagan:

1. Client memerintahkan peramban web untuk mengunjungi situs berbasis django.
2. Peramban akan mengirimkan `HTTP Request` dari client ke server situs yang dikunjungi. Request akan dihandle oleh `urls.py`.
3. Setelah pattern ditemukan, function dalam `views.py` yang sesuai (fungsi yang terikat dengan url tersebut) akan memproses request client. `models.py` menyimpan data dan logika aplikasi. `views.py` memproses request dengan menampilkan data dari model (models.py) dan menghubungkannya dengan template (.html).
4. Setelah itu, peramban web akan mengirimkan halaman web yang diminta client berupa `html`. Peramban client merender `html` sebagai `HTTP Response` dari server django.

## 3. Virtual Environment

### Mengapa menggunakan virtual environment?

Penggunaan virtual environment pada proyek django lebih disarankan dibandingkan tanpa menggunakannya.Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan dependencies lain yang ada pada komputer. Jika dibayagkan, pada tiap proyeknya kita akan memiliki python yang berbeda. Hal ini membantu kita dalam mengelola dependencies proyek sehingga dapat menghindari terjadinya konflik.

### Apakah aplikasi web berbasis Django dapat dibuat tanpa menggunakan virtual environment?

Ya. Proyek django tetap dapat dibuat tanpa menggunakan virtual environment selama python sistem kita memiliki depedensi yang akan digunakan.

## 4. MVC, MVT, dan MVVM

Konsep arsitektur dalam pengembangan web untuk memisahkan komponen-komponen utama sebuah aplikasi. Hal ini akan memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.

### MVC (Model View Controller)

<img src=https://ristek.link/mvc-pic>

Model: bagian yang mengelola data dan logika aplikasi
View: bagian yang mengatur tampilan data dari model
Controller: bagian yang bertugas mengatur _flow_ interaksi `model` dan `view`. Meneruskan hasil manipulasi data dari `model` ke `view` yang akan ditampilkan pada layar pengguna

### MVT (Model View Template)

<img src=https://miro.medium.com/v2/resize:fit:1400/0*8ZFh-CsrMi7bQG0O.jpg>

Model: bagian yang mengelola data dan logika aplikasi
View: bagian yang menampilkan data dari `model` dan menghubungkannya dengan `template`
Template: bagian yang mengatur tampilan antarmuka pengguna (serupa dengan `Controller` pada `MVC`)

### MVVM (Model View ViewModel)

<img src=https://media.geeksforgeeks.org/wp-content/uploads/20221012200730/gfgmvvm.png>

Pola desain yang membedakan UI dengan logika dari aplikasi. `Viewmodel` serupa dengan `Controller`. Konsep ini memungkinkan pengembang melakukan pemisahan kerja yang lebih baik antara UI dengan logika.

Model: bagian yang mengatur data dan logika aplikasi
View: bagian yang mengatur tampilan antarmuka pengguna, tetapi tidak mengolah data
ViewModel: bagian yang menghubungkan `model` dan `view`, meneruskan data yang akan ditampilkan ke `view`

## Perbedaan

Pada konsep MVC, pemisahan kerja lebih tegas dibanding konsep lainnya. Bagian yang serupa dengan `Controller pada MVC` adalah `Template pada MVT` dan `ViewModel pada MVVM`. Meski demikian, terdapat perbedaan di antara ketiga konsep, seperti yang telah disampaikan sebelumnya.

</details>
