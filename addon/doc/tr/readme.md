# Anında Çeviri #

* Yazarlar: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto
  Buffolino ve diğer NVDA gönüllüleri.
* [kararlı sürümü][1] indir
* [geliştirme sürümünü][2] indir

Bu eklenti, seçili ve/veya pano metnini bir dilden diğerine çevirmek için
kullanılır. Bu, Google Çeviri hizmeti kullanılarak yapılır.

## Dillerin ayarlanması ##
Kaynak, hedef ve takas dilini yapılandırmak için şuraya gidin: NVDA Menüsü >> Tercihler >> Ayarlar iletişim kutusu >> Anında Çeviri kategorisi.\n

"Kaynak dil" ve "Hedef dil" etiketli iki seçim kutusu ve çevirinin panoya
kopyalanıp kopyalanmayacağını bbelirlemek için bir onay kutusu bulunur.

Ek olarak, "Kaynak dil" seçim kutusundan otomatik seçeneği (ilk tercih)
seçtiyseniz, "Değişim için kullanılacak dil" etiketli bir seçim kutusu ve
otomatik takas hakkında bir onay kutusu da gösterilir.

İlk iki seçim kutusunun ve kopyalamayla ilgili  onay kutusunun anlamı bariz,
ancak geri kalanı hakkında bazı açıklamalar gerekebilir. Aşağıdaki
açıklamaların otomatik seçeneğinde ayarlanan kaynak dili varsaydığını daima
unutmayın.

"Değişim için dil" seçim kutusu, kaynak ve hedef dili komut dosyası
aracılığıyla değiştirdiğinizde (aşağıya bakın) kullanışlıdır; aslında,
otomatik seçeneğinde ayarlanan bir hedef dilin bir anlamı yoktur, bu nedenle
eklenti onu yukarıdaki seçim kutusundaki  değere ayarlar.

Öyleyse, şu durumu farzedin: genellikle türkçe'ye (ana diliniz) çeviri
yaparsınız, ancak bazen (örneğin, bir belge yazarken) İngilizce'ye'ya
(diyelim ki ikinci diliniz) çevirmeniz gerekebilir; "değişim için
kullanılacak dil" seçim kutusunu İngilizce'ye ayarlayabilirsiniz, böylece
eklenti ayarlarına tekrar girmeksizin Türkçe'den İngilizce'ye çeviri
yapabilirsiniz. Açıkçası, bu işlevin daha sık ihtiyaçlarınıza göre büyük
veya küçük bir faydası vardır.

Şimdi, otomatik takas onay kutusu: Yalnızca "Kaynak dil" seçim kutusunda
otomatik seçeneğini ayarlamışsanız gösterilir ve "takas için dil" seçim
kutusunda belirlediğiniz dil kullanılır. Etkinleştirirseniz, eklenti, kaynak
ve hedef yapılandırmanızdan otomatik olarak hedefin kaynak dil olduğu ve
"takas için dil" seçim kutusunda seçilen dilin yeni hedef dil olacağı bir
konfigürasyona geçiş yapmaya çalışır; Çevirmek istediğiniz metnin dili hedef
olarak belirlemiş olduğunuz dille aynıysa  son derece kullanışlı olabilir.

Basit bir örnek: daha önce farzedilen durumu tekrar hatırlayın; Bir metni
İngilizce'den farklı bir dilden çeviriyorsanız sorun olmaz, İngilizce'de
doğru çeviriyi alırsınız. Ancak İngilizce'den bir metni çevirmeniz
gerekiyorsa, normalde orijinal metinle aynı olan İngilizce'ye bir çeviri
alırsınız ve bu biraz işe yaramaz. Ancak otomatik değiş tokuş işlevi
sayesinde, metninizin İtalyancaya nasıl geldiğini bilmek istediğinizi
varsayarsak, eklenti hedef dili otomatik olarak İtalyancaya çevirir, böylece
geçerli bir çeviri döndürür sonuç olarak.

Neyse, bu geçici bir yapılandırmadır; bu seçeneğin bir etkisi yoksa
(deneyseldir), aşağıda açıklanan takas hareketini kullanarak manuel olarak
kararlı bir yapılandırmaya geçmeyi deneyin. Deneyseldir, çünkü bazı
durumlarda (genellikle kısa metinlerle), Google gerçek kaynak dili doğru
tanımaz ve kaynak dili önceki hedef dil olmaya zorlamak için dilleri komut
dosyası aracılığıyla manuel olarak değiştirmeniz gerekir (örneğimizde
İngilizceye).

En azından konuşma ayarları kategorisinde (NVDA Menüsü >> Tercihler >> ayarlar iletişim kutusu), "destekleniyorsa konuşma dilini otomatik olarak değiştir" seçeneğini işaretlemek isteyebilirsiniz. Bu şekilde, çok dilli bir sentezleyici kullanıyorsanız çeviri, sentezleyicinin hedef dil sesi kullanılarak söylenir.\n

## kullanarak ##
Bu eklentiyi üç şekilde kullanabilirsiniz:

1. Seçim komutlarını kullanarak bir metin seçin (örneğin, shift tuşuyla
   birlikte ok tuşlarını kullanın) ve çevirmek için ilgili tuşa
   basın. çeviri sonucu kullandığınız sentezleyici ile okunacaktır.
2. Panodaki metni de çevirebilirsiniz.
3. Son söylenen metni çevirmek için ilgili kısayol tuşuna basın.

## Kısayollar ##
Aşağıdaki tüm komutlar "NVDA+Shift+t" tuşları ile komut katmanını açtıktan
sonra kullanılabilir:

* T: Seçili metni çevir,
* Shift+t: Panodaki metni çevir,
* S: kaynak ve hedef dilleri değiştir,
* A: mevcut konfigürasyonu söyle,
* C: son sonucu panoya kopyala,
* I: seçilen metnin dilini tanımla,
* L: son konuşulan metni çevir,
* O: çeviri ayarları iletişim kutusunu aç
* H: mevcut tüm katman komutlarını duyurur.

## Changes for 4.4.3 ##
* Added the ability to replace underscores with spaces, may provide better
  translation results depending on context (thanks to Beka Gozalishvili)
* Added compatibility for NVDA 2022.1

## 4.4.2 için değişiklikler ##
* Dil algılama ve otomatik dil değiştirme restore edildi (Düzeltme için
  Cyrille'a teşekkürler)
* çeviri için güncellenmiş diller (Cyrille'e teşekkürler)

## 4.4 için değişiklikler ##
* Anında çeviri artık NVDA 2019.3 ile (NVDA'nın Python 3 sürümleri) uyumlu

## 4.3 için değişiklikler ##
* nvda uyumluluk düzeltmesi Şimdi anında çeviri, en son nvda derlemeleriyle
  uyumlu olacak.
* google'ı tekrar bir çeviri hizmeti olarak kullanmanın bir yolu bulundu.

## 4.2 için değişiklikler ##
* Daha yeni nvda sürümleriyle çalışması sağlandı.
* Otomatik dil algılama özelliği  restore edildi

## 4.1 için değişiklikler ##
* Anında Çeviri, artık Google yerine Yandex çeviri hizmetiyle yeniden
  çalışıyor.

## 4.0 için değişiklikler ##
* Çeviri, takas sonrasında otomatik olarak gerçekleştirilir.
* Önbellek hatası düzeltildi.

## 3.0 için değişiklikler ##
* Kısayolların kullanım şekli değişti, şimdi "NVDA+Shift+t" anında Çeviri
  komut katmanı Kısayol tuşuna ve ardından çeşitli işlemleri gerçekleştirmek
  için ilgili komut tuşuna basabilirsiniz ("girdi hareketleri " bölümündeki
  tüm Komutlara bakın).
* Takas dil seçeneği eklendi.
* Değiştirilen yapılandırma biçimi, şimdi salt okunur bölmesinde ise anında
  çeviri ayarları değiştirilebbilir, ancak bunun için NVDA'nın yeniden
  başlatılması gerektiğini unutmayın.
* Çevrilebilecek metin miktarıyla ilgili sınır kaldırıldı.
* Anında Çeviri Ayarlar menü öğesi eklendi kısayol t
* Otomatik seçeneği yalnızca kaynak dil seçim kutusunda bulunuyor.
* Çeviri sonuçlarının kopyalanmasıyla ilgili bir onay kutusu eklendi.
* Yapılandırma dosyasını konfigürasyon dizininin kökünde bulundur
* Kaynak ve hedef diller, Google Çeviri'nin şu anda sundukları ile
  senkronize edildi (22 Nisan 2015).


## 2.1 için değişiklikler ##
* NVDA + shift + y basılınca Şimdi eklenti panodaki metni çevirebilir.

## 2.0 için değişiklikler ##
* kaynak ve hedef dil seçebileceğiniz gui yapılandırıcı eklendi.
* Tercihler menüsü altına eklenti menü öğesi eklendi.
* Ayarlar şimdi ayrı bir yapılandırma dosyasına yazılıyor.
* Çeviri sonuçları artık otomatik olarak gelecek kullanımlar için panoya
  kopyalanır.

## 1.0 için değişiklikler ##
* İlk sürümü.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
