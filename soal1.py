def tambah_aktivitas(nama,tanggal,kategori):
    global kegiatan
    
    if nama.lower() in [nama_k.lower() for nama_k in kegiatan]:
        return 'Kegiatan sudah pernah diinput. Tidak boleh double claim!'
    else:
        kegiatan[nama] = [tanggal,kategori,daftar_poin_kegiatan[kategori]]
        return 'Kegiatan berhasil ditambahkan.'



kegiatan = {}

daftar_poin_kegiatan = {
    'Prestasi':30,
    'Organisasi':10,
    'Kepanitiaan':5,
    'Rekognisi':2
}



belum_keluar = True

while belum_keluar:
    print('******* Kredit Keaktifan Mahasiswa ******\n(Student Activities Credit)')

    choices = ['Menambahkan Kegiatan', 'Menampilkan Jumlah Poin', 'Keluar']

    for i, choice in enumerate(choices,start=1):
        print(f'{i}. {choice}')

    print('-'*30)

    pilihan = choices[int(input('Silahkan Masukan Pilihan Anda: '))-1]

    if pilihan == choices[0]:
        nama_aktivitas = input('Nama Kegiatan: ')
        tanggal_aktivitas = input('Tanggal Kegiatan: ')
        print('Pilihan Kategori Kegiatan:')
        for poin in daftar_poin_kegiatan:
            print(f' - {poin}')
        kategori_kegiatan = input('Masukan Kategori Kegiatan: ').title()
        print('')
        print(tambah_aktivitas(nama_aktivitas,tanggal_aktivitas,kategori_kegiatan))
        print('')
    elif pilihan == choices[1]:
        print('')
        print('-'*30,end='')
        print('Nama Kegiatan\tTanggal\tKategori\tPoin')
        total_poin = 0
        for i, kegiatan_terdaftar in enumerate(kegiatan,start=1):
            print(f'{i}. {kegiatan_terdaftar}',end='\t')
            print(*kegiatan[kegiatan_terdaftar],sep='\t')
            total_poin += kegiatan[kegiatan_terdaftar][-1]
        print(f'JUMLAH TOTAL POIN\t: {total_poin}')
        print('')
    else:
        print('Sistem Berhenti...')
        belum_keluar = False

