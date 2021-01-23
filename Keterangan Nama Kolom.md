## Keterangan Nama Kolom

| Nama Kolom            | Keterangan                                                |
|---------------------  |---------------------------------------------------------- |
| Date                  | Tanggal jalannya perdagangan                              |
| Previous              | Harga penutupan hari bursa sebelumnya                     |
| openPrice             | Harga pembukaan pada hari tersebut                        |
| firstTrade            | -                                                         |
| high                  | Harga tertinggi pada hari tersebut                        |
| low                   | Harga terendah pada hari tersebut                         |
| close                 | Harga penutupan pada hari tersebut                        |
| change                | Perubahan harga pada hari tersebut                        |
| volume                | Volume perdagangan (dalam satuan lembar)                  |
| value                 | Total nilai perdagangan pada hari tersebut                |
| frequency             | Frekuensi perdagangan pada hari tersebut                  |
| indexIndividual       | -                                                         |
| offer                 | Nilai penawaran harga jual pada hari tersebut             |
| offerVolume           | Volume penawaran harga jual pada hari tersebut            |
| bid                   | Nilai penawaran harga beli pada hari tersebut             |
| bidVolume             | Volume penawaran harga beli pada hari tersebut            |
| listedShares          | Jumlah saham yang beredar di masyarakat                   |
| tradebleShares        | Jumlah saham yang dapat diperjualbelikan oleh masyarakat  |
| weightForIndex        | -                                                         |
| foreignSell           | Total penjualan oleh asing (dalam satuan lembar)          |
| foreignBuy            | Total pembelian oleh asing (dalam satuan lembar)          |
| delistingDate         | Tanggal penghapusan pencatatan saham di BEI               |
| nonRegularVolume      | Volume pada pasar non-reguler                             |
| nonRegularValue       | Total nilai perdagangan pada pasar non-reguler            |
| nonRegularFrequency   | Total frekuensi transaksi pada pasar non-reguler          |

## Catatan

### Saham disuspend

Apabila suatu saham disuspend maka kolom berikut akan bernilai 0:
1. High
2. Low
3. Change
4. Volume
5. Value
6. Frequency
7. Offer
8. OfferVolume
9. Bid
10. BidVolume

### Kolom tanpa keterangan

Saya tidak yakin untuk apa kolom tersebut hadir. Dengan demikian saya memutuskan agar pengguna yang dapat memutuskan sendiri apa fungsi kolom tersebut.

Pengguna dapat mengajukan pull requests apabila pengguna yakin untuk apa fungsi dan keterangan kolom tersebut.
