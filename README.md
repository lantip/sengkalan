Sengkalan Generator
===
Sengkalan atau Candra Sengkala adalah cara orang Jawa "menyembunyikan" atau mengubah angka tahun menjadi kalimat.
Contohnya adalah tahun runtuhnya kerajaan Majapahit, didapat dari candra sengkala "Sirna Ilang Kertaning Bumi".


Bagaimana Cara Kerjanya?
---
Untuk menyusun Candra Sengkala, langkah yang harus dilakukan adalah:
1. Membalik urutan angka tahun. Jadi, semisal tahun 2019, maka dibalik menjadi 9102
2. Menggganti masing-masing angka dengan kata yang memiliki watak angka tersebut.
3. Menggabungkan kembali kata-kata tadi, sehingga didapat kalimat yang memiliki makna tersendiri.

Requirements
---
- Python 3

Installation
---
- `git clone https://github.com/lantip/sengkalan.git`
- `cd sengkalan`
- If you have `pipenv` in your python package, simply run `pipenv install`
- If you don't have `pipenv`, just use the script rightaway.

Usage
---

    Untuk membuat sengkalan, masukkan angka tahun. Hasilnya akan didapat 3 pilihan kalimat.
    $ python sengkalan.py -t 2019

Thanks To
---
- Mas Bekel Setya Amrih Prasaja -- atas requestnya hehe

TO DO
---
- memakai word embeddings Bahasa Jawa untuk mendapatkan nearest neighbor tiap kata. 