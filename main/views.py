import datetime
import json
from django.shortcuts import render, redirect
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    HttpResponseNotFound,
    JsonResponse,
)
from main.forms import ProductForm, Item
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Tugas 4: merestriksi halaman main (hanya dapat diakses oleh pengguna yang sudah login)\
# Tugas 4: membuat halaman utama main menjadi restricted dengan cara membuat akun untuk pengguna
# hrs login dulu buat akses main
@login_required(login_url="/login")
def show_main(request):
    # menyaring seluruh objek dengan hanya mengambil Item yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login
    items = Item.objects.filter(user=request.user)
    banyak_items = len(items)
    context = {
        "name": request.user.username,  # menampilkan username pengguna yang login pada halaman main
        "class": "PBP C",
        "items": items,
        "banyak_items": banyak_items,
        "last_login": request.COOKIES["last_login"],  # menambahkan last_login
    }

    return render(request, "main.html", context)


def profile(request):
    # items = Item.objects.filter(user=request.user)
    context = {
        "name": request.user.username,
        "class": "PBP C",
        "last_login": request.COOKIES["last_login"],
    }

    return render(request, "profile.html", context)


def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        """
        Jika form valid dan metode permintaan adalah POST:
        Objek Item baru dibuat dari data form
        Pengguna yang saat ini terotentikasi ditetapkan sebagai pemilik produk
        objek disimpan di basis data
        Pengguna diarahkan kembali ke halaman utama
        """
        product = form.save(commit=False)
        product.user = request.user
        # menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login
        product.save()
        return HttpResponseRedirect(reverse("main:show_main"))

    context = {"form": form}
    return render(request, "create_product.html", context)


# Tugas 6: Membuat Fungsi untuk Mengembalikan Data JSON
# Fungsi ini akan digunakan untuk menampilkan data produk pada HTML dengan menggunakan fetch
def get_product_json(request):
    item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", item))


# Tugas 6: fungsi ajax untuk menambahkan item/produk
@csrf_exempt
def create_ajax(request):
    """
    Fungsi ini menerima request POST untuk menambahkan item baru
    Data item baru (name, amount, description, dan user terkait) diambil dari request POST
    Sebuah objek Item baru dibuat menggunakan data tersebut dan disimpan ke basis data
    Fungsi mengembalikan respons HTTP dengan status 201 CREATED yang menunjukkan bahwa item telah berhasil dibuat
    """
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(request):
    data = Item.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def register(request):
    # membuat formulir registrasi
    form = UserCreationForm()

    if request.method == "POST":
        # form diperbarui dengan data dari POST yang dikirimkan oleh pengguna
        form = UserCreationForm(request.POST)
        # memeriksa apakah data dari pengguna valid/sesuai dengan aturan UserCreationForm
        if form.is_valid():
            # membuat dan menyimpan data ke basis data
            form.save()
            # menampilkan pesan jika register berhasil
            messages.success(request, "Your account has been successfully created!")
            # mengarahkan pengguna ke halaman login
            return redirect("main:login")
    """
    jika req method bukan POST atau data form tidak valid
    maka objek form dimasukkan ke dalam konteks
    context digunakan saat merender halaman 'register.html'
    """
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        # mendapatkan username dan password dari input pengguna
        username = request.POST.get("username")
        password = request.POST.get("password")
        # otentikasi pengguna berdasarkan usernama dan password dari request, jika berhasil -> objek pengguna akan disimpan ke variabel user
        # else, user = None
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # jika otentikasi berhasil
            login(request, user)  # pengguna login dan otentikasinya dijaga
            # mengarahkan pengguna yang berhasil login
            response = HttpResponseRedirect(reverse("main:show_main"))
            # cookie "last_login" untuk melihat kapan terakhir kali pengguna melakukan login
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            # jika otentikasi gagal -> menampilkan pesan kesalahan
            messages.info(
                request, "Sorry, incorrect username or password. Please try again."
            )
    context = {}
    return render(request, "login.html", context)


# menghapus sesi pengguna yang saat ini login
def logout_user(request):
    logout(request)
    # mengarahkan ke halaman login
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response


# Tugas 4: BONUS
def increase(request, id):
    # meningkatkan jumlah (amount) dari objek Item dengan id tertentu
    """
    Menerima request dan id sebagai parameter
    Mengambil objek Item dari basis data berdasarkan id yang diberikan
    Menambahkan nilai amount dari objek Item saat ini dengan 1
    Menyimpan perubahan tersebut ke basis data
    Mengarahkan pengguna kembali ke halaman utama ("main:show_main")
    """
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save()
    return redirect("main:show_main")


def decrease(request, id):
    # mengurangi jumlah (amount) dari objek Item dengan id tertentu
    # jika jumlah mencapai 0 atau kurang, objek Item akan dihapus
    """
    Menerima request dan id sebagai parameter
    Mengambil objek Item dari basis data berdasarkan id yang diberikan
    Mengurangi nilai amount objek Item dengan 1
    Jika nilai amount setelah pengurangan menjadi 0 atau negatif, objek Item dihapus dari basis data
    Jika nilai amount masih lebih besar dari 0, perubahan disimpan di dalam basis data
    Mengarahkan pengguna kembali ke halaman utama ("main:show_main")
    """
    item = Item.objects.get(pk=id)
    item.amount -= 1
    if item.amount <= 0:
        item.delete()
    else:
        item.save()
    return redirect("main:show_main")


def remove_all(request, id):
    # menghapus seluruh objek Item dengan id tertentu dari basis data
    """
    Menerima request dan id sebagai parameter
    Mengambil objek Item dari basis data berdasarkan id yang diberikan
    Menghapus objek Item dari basis data
    Mengarahkan pengguna kembali ke halaman utama ("main:show_main")
    """
    item = Item.objects.get(pk=id)
    item.delete()
    return redirect("main:show_main")


@csrf_exempt
def create_product_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user=request.user,
            name=data["name"],
            amount=int(data["amount"]),
            description=data["description"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
