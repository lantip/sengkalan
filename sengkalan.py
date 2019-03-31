#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2019/03/31"
__description__ =   "Sengkalan Generator"
""" 

import random
import argparse
import datetime

def watak(angka):
    if angka == 0:
        choices = [
            ['byoma', 'musna', 'nis', 'mlethik', 'langit'],
            ['sirna', 'ilang', 'kombul', 'awang-awang'],
            ['mesat', 'muluk', 'gegana', 'nglès'],
            ['tumenga', 'nenga', 'luhur'],
            ['suwung', 'sonya', 'muksa', 'doh', 'tebih'],
            ['swarga', 'tanpa', 'barakan'],
            ['tan', 'rusak', 'brastha', 'swuh'],
            ['walang', 'kos', 'pejah', 'akasa'],
            ['tawang', 'wiyat', 'oncat','windu','widik-widik'],
            ['nir', 'wuk', 'sat', 'surud', 'sempal']
        ]
    elif angka == 1:
        choices = [
            ['tunggal', 'gusti', 'sujanma', 'semedi'], 
            ['badan', 'nabi', 'rupa', 'maha', 'buddha'], 
            ['niyata', 'luwih', 'pamasé'], 
            ['wong', 'buweng','rat', 'lèk', 'iku'], 
            ['surya', 'candra', 'kartika', 'bumi'], 
            ['wiji', 'urip', 'ron', 'éka'], 
            ['prabu', 'kenya', 'nekung'], 
            ['raja','putra', 'sasa', 'dhara'], 
            ['peksi', 'dara', 'tyas', 'wungkul', 'sudira', 'budi'], 
            ['wani', 'hyang', 'jagad', 'nata']
        ]
    elif angka == 2:
        choices = [
            ['asta', 'kalih', 'ro', 'nembah', 'ngabekti'], 
            ['nétra', 'kembar', 'myat', 'mandeng', 'nayana'], 
            ['swiwi', 'lar', 'sikara', 'gandhèng'],
            ['paksa', 'apasang', 'sungu'], 
            ['athi-athi', 'talingan', 'dresthi'], 
            ['carana', 'tangan', 'karna'], 
            ['bau', 'suku', 'caksuh'], 
            ['mata', 'paningal', 'locana'],
            ['ama', 'nebah', 'karnan', 'ngrengga', 'pengantèn', 'dwi'],
            ['kanthi', 'buja','bujana']
        ]
    elif angka == 3:
        choices = [
            ['bahni', 'tiga','ujwala', 'kaèksi'],
            ['katon','murub', 'dahana', 'payudah'],
            ['katingalan', 'kaya', 'bentèr'],
            ['nala', 'uninga', 'kawruh'],
            ['lir', 'wrin', 'wéda', 'naut', 'nauti'],
            ['teken', 'siking', 'pawaka'],
            ['kukus', 'api', 'apyu'],
            ['brama', 'rana', 'rananggana'],
            ['utawaka', 'uta', 'ujel', 'kobar', 'agni'],
            ['wignya', 'guna', 'tri', 'jatha']
        ]
    elif angka == 4:
        choices = [
            ['catur', 'warna', 'wahana', 'pat', 'warih'],
            ['waudadi', 'dadya', 'keblat', 'papat'],
            ['toya', 'suci', 'udaka', 'we'],
            ['woh', 'nadi', 'jladri', 'sindu'],
            ['yoga', 'gawé', 'tlaga', 'hèr', 'wening'],
            ['udan', 'bun', 'tirta', 'marta'],
            ['karya', 'sumber', 'sumur'],
            ['masuh', 'marna', 'karti', 'karta'],
            ['jalaniddhi', 'samodra', 'udaya', 'tasik'],
            ['tawa', 'segara', 'wédang']
        ]
    elif angka == 5:
        choices = [
            ['pandhawa', 'lima', 'wisikan', 'gati'],
            ['indri', 'indriya', 'warastra', 'wrayang'],
            ['astra', 'lungid', 'sara', 'saré'],
            ['guling', 'raseksa', 'diyu'],
            ['buta', 'galak', 'wil','yaksa', 'yaksi'],
            ['saya', 'wisaya', 'bana'],
            ['jemparing', 'cakra', 'hru'],
            ['tata', 'hanata', 'bayu', 'bajra'],
            ['samirana', 'pawaka', 'maruta', 'angin'],
            ['panca', 'marga', 'margana']
        ]
    elif angka == 6:
        choices = [
            ['rasa', 'nenem', 'rinaras', 'artati'],
            ['lona','tikta', 'madura', 'sarkara'],
            ['amla', 'kayasa', 'karaséng'],
            ['oyag', 'obah', 'nem', 'kayu'],
            ['wreksa', 'glinggang', 'prabatang', 'oyig'],
            ['sad', 'anggas', 'anggang-anggang'],
            ['mangsa', 'naya', 'retu'],
            ['wayang', 'winayang', 'anggana'],
            ['ilat', 'kilat', 'lidhah', 'lindhu', 'carem','manis'],
            ['tahen', 'osik', 'karengya']
        ]
    elif angka == 7:
        choices = [
            ['sapta', 'prawata', 'acala', 'giri'],
            ['ardi', 'gora', 'prabata', 'himawan'],
            ['pandhita', 'pitu', 'kaswarèng'],
            ['resi', 'sogata', 'wiku'],
            ['yogi', 'swara', 'dwija', 'suyati'],
            ['wulang', 'weling', 'wasita'],
            ['tunggang', 'turangga', 'gung'],
            ['swa', 'aswa', 'titihan', 'kuda'],
            ['ajar', 'arga', 'sabda', 'nabda', 'angsa', 'muni'],
            ['suka', 'biksu', 'biskuka']
        ]

    elif angka == 8:
        choices = [
            ['astha', 'basu', 'anggusthi', 'basuki'],
            ['slira', 'murti', 'bujangga', 'manggala'],
            ['taksaka', 'menyawak', 'tekèk'],
            ['dwipa', 'dwipangga', 'bajul'],
            ['gajah', 'liman', 'dwirada', 'èsthi'],
            ['éstha', 'matengga', 'brahma'],
            ['brahmana', 'wewolu'],
            ['baya', 'bebaya', 'kunjara'],
            ['tanu', 'sarpa', 'samaja', 'madya', 'mangèsthi'],
            ['panagan', 'ula', 'naga']
        ]
    elif angka == 9:
        choices = [
            ['bolong', 'nawa', 'dwara', 'pintu', 'kori'],
            ['bedhah', 'lawang', 'wiwara', 'gapura'],
            ['rong','song', 'wilasita', 'anglèng'],
            ['trustha', 'trusthi', 'trus', 'butul'],
            ['déwa', 'sanga', 'jawata', 'manjing'],
            ['arum', 'ganda', 'kusuma'],
            ['muka', 'rudra', 'masuk'],
            ['rago', 'angrong', 'guwa', 'menga'],
            ['babahan', 'lèng', 'ambuka', 'gatra', 'anggangsir'],
            ['nanda', 'wangi', 'wadana']
        ]
    else:
        choices = []

    return random.choice(choices[random.choice(range(len(choices)))])


def generate_sengkalan(angka):
    lst = [a for a in str(angka)]
    lst.reverse()
    hsl = []
    for ls in lst:
        hsl.append(str(watak(int(ls))).capitalize())

    return ' '.join(hsl)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('-t', '--tahun', type=int, default=int(datetime.datetime.now().year), help="Masukkan angka Tahun (Input year)", required=True)

    args = parser.parse_args()

    year = args.tahun
    
    print('Untuk sengkalan tahun' + str(year)+', kamu bisa memilih satu di antara tiga pilihan berikut:')
    print(generate_sengkalan(year))
    print()
    print(generate_sengkalan(year))
    print()
    print(generate_sengkalan(year))





