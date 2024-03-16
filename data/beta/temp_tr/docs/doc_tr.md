#TCA-Media Downloader 3 Kılavuzu

TCA-Media Downloader 3, Python 3'te yazılmış ve ekran okuyucularla tamamen erişilebilir bir uygulamadır.  

Multimedya içeriğini indirmemize izin veren YT-DLP kitaplığına dayanmaktadır.
[Buradan resmi olarak desteklenen yüzlerce siteyi kontrol edebilirsiniz](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md):



Ek olarak, TCA-Media Downloader 3, YT-DLP ile birlikte bir kütüphane olan FFMPEG'i kullanır.  
FFMPEG, İndirmelerimizi farklı biçimlere dönüştürmemizi sağlar.  

TCA-Media Downloader 3 öncelikle YouTube'a odaklanmıştır. Ancak belirtildiği gibi daha fazla siteyle uyumludur ve bazı resmi olmayan siteler için destek ekler.  
Resmi olmayan sitelerden medya indirmeye çalışıldığı zaman, YT-DLP'nin kaynak alındığı sayfadan gerekli bilgileri alıp alamayacağına bağlı olarak indirme işleminin gerçekleşip gerçekleşemeyeceği bilgisi sunulacaktır.  

Bu kılavuz TCA-Media Downloader 3'ün ilk sürümündeki arayüzünün kullanımını açıklamak için hazırlanmıştır.  
Farklı güncellemelere eklenen yenilikler [Değişiklik günlüğü](#Değişiklik günlüğü) bölümüne yansıtılacaktır, bu bölümde yeni seçenekler ve açıklamaları yer alacaktır, bu nedenle ana kılavuz yalnızca ilk sürümü detaylandıracaktır.

Benzer şekilde, bir güncelleştirme aldığımızda, bu güncelleştirmenin içerdiği yeni özelliklerin ayrıntılı bir açıklamasını sağlamaya çalışacağız.  

TCA-Media Downloader 3, program güncellemelerini otomatik olarak indirecek dahili bir güncelleyici ile birlikte gelir.  
Bu güncellemeler Kütüphane, özellikler ve Tümü olmak üzere 3 bölüme ayrılacaktır.  

1. Kitaplık dalındaki güncelleştirmeler: Bu dal, küçük kitaplık güncelleştirmeleri ve hata düzeltmeleri alır.
2. Özellikler dalında güncellemeler: Bu dal, uygulamaya eklenen yeni işlevlerin güncellemelerini alacaktır. Halihazırda uygulanmakta olan işlevlere yönelik genişletmeler veya geliştirmeler Kütüphane'de yer alacaktır; bu dalda yalnızca yeni işlevler yer alacaktır.
3. Tam daldaki güncellemeler: Bu dal, uygulama için tam güncellemeler alacaktır. Bu dal, uygulamanın tüm bileşenlerini tamamen güncelleyecek ve yeni özellikler, büyük hata düzeltmeleri veya kritik kütüphanelerle güncelleme yapmak için kullanılacaktır.

Güncellemeleri denetlerken, açıklama güncellemenin hangi dala ait olduğunu belirtir ve güncellenen sürümün isimlendirmesi ile her zaman öğrenebilirsiniz.  

TCA-Media Downloader ilk sürümünde 3.0.0.0 olacak.  
İlk 0 Tam dalına, ikincisi Özellik dalına ve sonuncusu Kütüphane dalına ait olacaktır.  

Bu kılavuz, uygulamanın ana özelliklerini açıklayacak ve kullanıcının diğer seçenekleri kendi kendine keşfetmesine olanak tanıyacaktır.  
Böylece, TCA-Media Downloader 3'ün keyfini çıkarmamız için sağlamaya çalıştığı tüm potansiyel keşfedilmiş olacaktır.  

Bir önizleme olarak, TCA-Media Downloader bu sürümde yeni indirme formatları, daha fazla indirme seçeneği, kişiselleştirmek için yeni olanaklar ve varsa çok azının sahip olduğu bir şey içeriyor.  

Önceki sürümlerde olduğu gibi videoları arayabiliyoruz. Ancak artık Oynatma Listesi ile Kanalları da kolay bir şekilde arayabilir ve bu sonuçlarla etkileşime girebiliyoruz.  

Ayrıca, bu sürümde, uygulamayı kullanmaya devam ederken anlık oynatma yeteneğinin yanısıra, aynı anda çoklu indirme de yapmak mümkündür.  

Halihazırda geliştirilmekte olan ve bazıları düşünülen birçok yeni seçeneğin eklenmesi amaçlanmaktadır.  

Bu ilk sürümde, TCA-Media Downloader 2'nin sahip olduğu özellikleri vermeye çalıştık. Ancak son sürümü olabildiğince kararlı hale getirmek için uğraşırken, aynı zamanda yeni özellikler de ekledik.  

Son sürüm stabil hale geldiğinde, herkesin beğeneceğine inandığımız yeni özellikler eklenecektir.  

##Arayüz açıklaması

Bu ilk sürümde uygulamanın 3 bölüme ayrıldığını söyleyebiliriz:

1. Sekmeler.
2. Oynatıcı.
3. kontroller.

###Sekmeler

Bu ilk sürümde 3 sekmemiz var: Bağlantı (Alt+1), Arama (Alt+2) ve İndirilenler (Alt+3).  

Alt+1, alt+2 ve alt+3 tuşlarının yanı sıra:  
CTRL+Sekme ile sonraki ve CTRL+Shift+sekme ile de önceki sekme sayfasına gidebiliriz.  
CTRL+Boşluk çubuğu ile de hangi sekmede olduğumuz bilgisine erişebiliriz.

####Bağlantı (Alt+1)

Bu sekmeye girdiğimizde, bizi bir bağlantı yazma alanına odaklayacaktır.  

Yalnızca girdiğimiz terimin bir internet adresi olduğunu tespit ederse çalışır, aksi takdirde hiçbir şey yapmaz.  

Belirtildiği gibi, bu uygulama esas olarak YouTube'a odaklanmıştır, bu nedenle bir YouTube Bağlantısı eklersek, ne tür bir Bağlantı olduğunu algılar.  

#####video, Oynatma Listesi veya Kanal.

Girdiğimiz bağlantı, Bir YouTube Bağlantısı değilse ve başka bir uyumlu web sitesinden geliyorsa veya medyayı indirip indiremeyeceğimizi test etmek istiyorsak, bize diğer indirme seçeneklerini verecektir.  

Bir Bağlantı girdiğinizde, enter tuşuna basarsanız, bu Bağlantı ile ilgili seçeneklerin bulunduğu bir içerik menüsü görüntülenir. Seçenekler girilen Bağlantı türüne bağlı olarak değişir.  

Bir YouTube video Bağlantısında aşağıdaki seçeneklere sahip olacağız:

* Normal indirme: Bu seçenek, videoyu seçtiğimiz seçeneklerle indirmemize izin verir (daha sonra açıklanacaktır). Video özelliği ve biçim ile indirmeyi ekler (daha sonra açıklanacaktır). İndirmeyi İndirilenler sekmesinde(ALT+3) görebiliriz.
* İndirmeyi Özelleştir: Bu seçenek, bize bir biçim seçme ve özelliklerini görme olanağı vereceği bir iletişim kutusu açar; bu, ses ve video kodlayıcılarını bilen ileri düzey kullanıcılar içindir.
* Video Bilgileri: Bu, ilgili bilgileri ve söz konusu video için çeşitli bilgileri panoya kopyalama, indirme ve bilgilere başvurma gibi seçenekleri görebileceğimiz bir iletişim kutusu açacaktır.
* Oynat: Videoyu TCA-Media Downloader 3'e dahil edilmiş oynatıcıda oynatmamıza izin verecektir (daha sonra açıklanacaktır).

Bir YouTube oynatma listesi bağlantısında aşağıdaki seçeneklere sahip olacağız:

* Tüm Oynatma Listesini indir: Oynatma listesinde bulunan bütün videoları seçtiğimiz seçenekler doğrultusunda toplu şekilde indirecektir.
* İndirilecek videoları seçin: Dilediğimiz videoları işaretleyebileceğimiz ve sadece seçili olanları indirebileceğimiz bir iletişim kutusu açar.

Bu iletişim kutusunda, videolar listesinde aşağıdaki tuşlara da sahibiz:

* Boşluk çubuğu: Seçili öğeyi işaretler veya işaretini kaldırır.
* Ctrl +R: Üzerinde bulunduğumuz videoyu oynatmaya başlar.
* Ctrl + D: Daha önceden belirlediğimiz seçeneklerle, üzerinde bulunduğumuz videoyu indirir.
* Ctrl + I: Oynatma listesinde bulunduğumuz konum hakkında bize bilgi verir.
* Ctrl + F: Bir sayı yazmak ve listede hızlıca o konuma gitmek için bir iletişim kutusu açacaktır. (Bu, çok fazla video içeren oynatma listeleri için iyidir.)
* Oynatma Listesi Bilgileri: Oynatma listesiyle ilgili bilgileri görüntüleyebileceğimiz bir iletişim kutusu açılacak, bize söz konusu oynatma listesinde yer alan videoları göstereceği bir alanımız olacak ve söz konusu oynatma listesi için seçeneklerimiz olacak.

Oynatma Listesi videolarıyla ilgili bu iletişim kutusunda, her videoda enter tuşuna basabiliriz ve videolara karşılık gelen seçeneklerin bulunduğu bir içerik menüsü alırız. Ayrıca bu listedeki her öğe üzerinde kullanabileceğimiz birkaç tuşumuz var:

* Ctrl +R: İlgili videoyu oynatmaya başlar.
* Ctrl + D: Daha önceden belirlediğimiz seçeneklerle, üzerinde bulunduğumuz videoyu indirir.
* Ctrl + I: Oynatma listesinde bulunduğumuz konum hakkında bize bilgi verir.
* Ctrl +F: Bir sayı yazmak ve listede hızlıca o konuma gitmek için bir iletişim kutusu açacaktır. (Bu, çok fazla video içeren oynatma listeleri için iyidir.)


Bir YouTube kanal Bağlantısında aşağıdaki seçeneklere sahip olacağız:

* Tüm Kanalı İndir: Bu, seçtiğimiz seçeneklerle kanalın içerdiği tüm videoları indirmelere ekleyecektir.
* İndirilecek videoları seçin: İndirmek istediğimiz videoları işaretleyebileceğimiz ve istemediklerimizin işaretini kaldırabileceğimiz bir iletişim kutusu açılır. Bu iletişim kutusu açıldığında bize oynatma listesinde video olmadığını bildirebilir, bunun nedeni kanalın telif hakkı ile korunan videolara sahip olması, videoların gizli olması, YouTube tarafından engellenmesi, şifre ile engellenmesi veya kanalın videolarının kanalın ana bölümü yerine oynatma listesinde olması olabilir.  
Kanalda telif hakkı ile korunan videolar var, videolar gizli, YouTube tarafından engellenmiş, şifre ile engellenmiş veya kanalın videoları kanalın ana bölümü yerine oynatma listesinde gibi.  

Bu iletişim kutusunda ayrıca video listesindeki birkaç tuşu kullanma imkanımız da var:

* Boşluk çubuğu: Seçili öğeyi işaretleyin veya işaretini kaldırın.
* Ctrl +R: İlgili videoyu oynatmaya başlar.
* Ctrl + D: Daha önceden belirlediğimiz seçeneklerle, üzerinde bulunduğumuz videoyu indirir.
* Ctrl + I: Oynatma listesinde bulunduğumuz konum hakkında bize bilgi verir.
* Ctrl +F: Bir sayı yazmak ve listede hızlıca o konuma gitmek için bir iletişim kutusu açacaktır. (Bu, çok fazla video içeren oynatma listeleri için iyidir.)
* Kanal Bilgileri: Kanal hakkında bilgi içeren ve içerisinde iki sekme bulunan bir iletişim kutusu açar. Bu sekmelerde, Videolar ve Oynatma Listesinin  ne kadar izlendiği, hangi videoları içerdiği ve kanalın varsa diğer oynatma liste bilgilerini görebiliriz.  

Bu iki alandan herhangi birinde bir öğe üzerinde enter tuşuna basabilir, videolara ve oynatma listesine karşılık gelen seçenekleri görebiliriz. Ayrıca video alanında oynatmak için Ctrl+r, indirmek için Ctrl+d, hangi konumda olduğumuzu bulmak için Ctrl+i ve istediğimiz öğeye hızlı bir şekilde gitmek için Ctrl+f'yi kullanabiliriz.  

Ayrıca bu iletişim kutusunda, panoya kopyalayabilmek veya kanalı indirebilmek için farklı düğmelere sahip olacağız.  

YouTube'a ait olmayan bir Bağlantı eklersek, enter tuşuna bastığımızda uygulama multimedya içeriğini bulmaya çalışacaktır.  

Girilen Bağlantıda indirilecek multimedya içeriği bulursa, bize iki seçenek sunacaktır.  
Bu seçenekler:  
Daha önce seçili olan seçeneklerle Normal İndir ve  
multimedya dosyasını orijinal biçimde indirmeye çalışacak olan orijinal indirmeyi dene.  
Seçenekleridir.  

Multimedya içeriğinin bulunamaması durumunda bize mesaj ile bilgi verecektir.  

Bağlantı sekmesine (Alt + 1) ile gittiğimizde, otomatik olarak Bağlantı yazma alanına odaklanır.
CTRL+B ile de Bağlantı alanı temizlenir.  

Bağlantı sekmesinin aşağıdaki seçenekleri, Bağlantı ve Arama sekmelerinde aratıp yapacağımız Normal İndirme işlemlerinde varsayılan olarak kullanılacaktır.  

Bağlantı sekmesinde, TAB ile ilerlediğimizde, Biçim Seçin (Alt + B) adlı bir seçim kutusuna erişiriz.  

Bu açılır seçim kutusunda, hem video hem de ses için uygulama tarafından desteklenen farklı biçimleri seçebiliriz.  
Buna ek olarak, kutudaki son seçenek, indirmeyi seçtiğimiz her şey için bize yeni indirme seçenekleri sağlayacak olan Gelişmiş seçeneğidir.  

Eğer seçim kutusunda, Gelişmiş seçeneğini seçer ve tab tuşu ile ilerlemeye devam edersek karşımıza:  
Gelişmiş bir kişisel biçim seçeneği belirleyin(ALT+Ç) adlı seçim kutusu gelir.  

Bu seçim kutusu bize 412 seçenek sunacaktır.  
Bunların hepsi indirmek istediğimiz tüm videolarda veya ses dosyalarında çalışmaz.  
Bu seçenekler test etmek içindir ve her şeyden önce bu bölüm ileri düzey kullanıcılar içindir.  
Normal kullanıcıların bu bölüme girmemesi tavsiye edilir.  

Her seçeneğin, indirme sırasında nelerin deneneceğine dair bir açıklaması vardır.  

Bu açılır seçim kutusunda 2 kısayol tuşumuz var:

* Ctrl + I: Bu bize içinde bulunduğumuz Seçim kutusundaki konum hakkında bilgi verir.
* Ctrl + F: Bu, tüm listeden bir seçeneğe hızlıca geçmek için bir iletişim kutusu açar.

Yok, diğer biçimlerden herhangi birini seçer ve Tab ile ilerlersek:  

Ses kalitesini seçin(ALT+K) açılabilir seçim kutusu karşımıza gelir.  

Ses kalitesinde indirme sesi için istediğimiz Bit Hızını seçebiliriz, bu her zaman indirmeye çalıştığımız içeriğin buna izin verip vermemesine bağlıdır, aksi takdirde yüksek bir bit hızı ayarlarsak, her zaman en iyi ses kalitesini indirmeye çalışır.  


Sekme tuşu ile gezinmeye devam ettiğimizde:  
Çıktı ad bileşimini seçin (ALT+A)   
Adlı bir seçim kutusu karşılar bizi.  
Bu seçim kutusunda, indirilen dosyaların isimlerinin nasıl görüneceğini seçebiliriz.  

Mevcut seçenekler:

* Numaralandırma yok (Varsayılan)
* Numaralandırma yok ve alt dizin oluştur.
* Numaralandırma ile.
* Numaralandırma ile ve alt dizin oluştur.

Şeklinde sıralanıyor.  

Bu seçim kutusunun ardından:
Konum Seçin (ALT+K)  
Onay kutusu gelir.  

Bu onay kutusu varsayılan olarak işaretli değildir. İndirilen dosyaları Müzikler klasöründe TCAMediaDownloader adlı klasörde saklar.  
Eğer ilgili klasörler mevcut değilse, otomatik olarak oluşturulur.  
Onay kutusunu işaretli hale getirirsek, indirmelerimizi kaydetmek istediğimiz konumu seçebileceğimiz bir pencere açılacaktır.  
Eğer işareti boşluk çubuğ ile temizlersek, indirme klasörü varsayılan konuma dönecektir.  

Bağlantı sekmesinde şimdilik yukarıdaki seçenekler bulunur.

####Arama (Alt+2)

Bu sekmenin yalnızca iki bileşeni vardır:

Aranacak bir terim girin (Alt+R): Bu yazma alanına, aratmak istediğimiz herhangi bir kelimeyi yazabilir ve Enter tuşuna basarak ilgili seçeneklere erişebiliriz.  

Yazma alanı boşken enter tuşuna basarsak, bize tek bir seçenek verecektir:  
Gösterilecek sonuç sayısını seç  
Alt menüsü olan bu menüde, 10 sonuç, 25 sonuç, 50 sonuç, 100 sonuç, 250 sonuç ve 500 sonuç gösterim seçeneklerinden dilediğiizi seçebiliriz.  
Seçtiğimiz sonuç sayısı, başka bir seçim yapana kadar kayıtlı kalır.  

Bir metin girip enter tuşuna basarsak, bize video, oynatma listesi veya kanal arama seçeneklerinin yanı sıra istediğimiz sonuç sayısını değiştirmek için önceki seçeneği de verecektir.  
Bu seçenekler, bağlamsal bir menüde gösterilir.  

İlk 3 seçenekten herhangi birini seçersek, arama kutusuna girdiğimiz terimi arayacaktır.  

Arama kutusundayken, CTRL+B tuşlarına basarak yazdığımız terimi ve sonuç listesini hızlıca temizleyebiliriz.  
Ayrıca, Geri silme tuşu ile arama yazma alanını temizleyebilir ve dilersek, Enter tuşuna basarak açılacak menüden hem sonuçları temizleyebilir hem de gösterilecek sonuç sayısını değiştirebiliriz.  

Menüler, yaptığımız eyleme bağlı olarak değişkendir.  

Peki, Arama Sonuçları (Alt + R) adlı listeye sekme tuşu ile gelirsek: Bu listede sonuçlardan herhangi birinin üzerinde enter tuşuna basabilir ve bize her arama için Bağlantı sekmesinde daha önce açıklanan seçeneklerin aynısını verir.

Arama videoyla ilgiliyse bazı ek seçenekler vardır.  

Bir videoyu hızlı bir şekilde oynatmak için Ctrl + R'yi, indirmek için Ctrl + D'yi kullanabilir ve ayrıca söz konusu videoda enter tuşuna bastığımızda menüde aşağıdaki yeni seçeneğe sahip oluruz:  

Arama için çoklu indirici: Bu seçenek, tüm arama sonuçlarının görüntüleneceği bir iletişim kutusu açar ve indirmek istediğimiz videoları seçmemize izin verir.  

Bu iletişim kutusu, istediğiniz her şeyi bir kerede seçmek ve tek tek indirmek zorunda kalmamak için idealdir.  

Bu diyalogdaki video listesinde, işaretlemek veya işareti kaldırmak için boşluk, oynatmak için Ctrl + R, odak noktasındaki öğeyi indirmek için Ctrl + D tuşlarını kullanabiliriz.  
Ayrıca, enter tuşuna basarsak, yukarıda da açıklanan videolar menüsündeki seçenekleri de verecektir.

Tab ile ilerlediğimizde, çoklu indirme için ad girmemiz gereken bir düzenleme kutusuna düşeriz.  
Bu ad, indirmeyi tanımlamanın yanı sıra, indirilecekler için de alt dizin oluşturur ve bu alt dizinde, bu iletişim kutusunda seçtiğimiz her şeyin çoklu indirmesi olacaktır.  

Arama sekmesi için bu kadar seçenek bulunur.

####İndirilenler (Alt+3)

Bu sekmede iki bölüm bulunur ve basittir.  

(Alt+L) ile hızlı bir şekilde erişebileceğimiz indirmelerin yer alacağı bir liste ve sekme ile ilerlediğimizde durum (Alt+D) adlı salt okunur bir alan var.  
Durum alanında, seçtiğimiz indirmenin durumunu gösterecek bir ilerleme çubuğu bulunuyor.  

İndirme listesinde bulunan öğelerin adı, türü (Oynatma listesi, Kanal veya Video gibi.) ve biçim bilgisi gösterilecektir.  
Biçim bilgisi: Bağlantı sekmesinde "Biçim Seçin" seçim kutusundan seçtiğimiz biçime göre görüntülenecektir.  

Bir indirme işleminde enter tuşuna basarsak, bize seçenekler içeren bir menü verecektir. Bu menü öğeleri indirme türüne göre değişken seçenekler gösterebilir.  

İndirme devam ediyorsa, aşağıdaki seçenekler gösterilir:

* Oynat (yalnızca video indirmelerinde)
* İndirme bağlantısını Web'de aç.
* İndirme bağlantısını panoya kopyala

İndirme bittiğinde, bize aşağıdaki seçenekleri de sunacaktır:

* İndirme klasörünü aç
* Ek olarak, bitmiş indirmeler varsa, adı Genel İşlemler ve alt menüsü de olan bir seçenek daha sunacaktır.
* Biten indirmeleri temizle.
* Seçilen indirme bir hata verirse, hatayı görüntüleme ve içeriğini kopyalama imkanı verecektir.

Ayrıca, hata yoksa, Biten indirmeleri temizle seçeneği de bulunur.  

Sekme tuşuna bastığımızda, seçtiğimiz öğe ile ilgili bilgilerin kısa bir bilgisini veren ve Durum adlı salt okunur bir alan karşılar bizi.  

İndirilenler sekmesinde, şimdilik bu kadar seçenek bulunur.

###Oynatıcı

Bu alanda sekme tuşuna basarsak eğer oynatılan bir öğe yoksa, diğer alana atlar. (Çünkü, oynatma kontrolleri sadece bir öğe oynatılıyorsa aktif olur).  

Bu düğmeler:

* Geri Sar (F1)
* Oynat / Duraklat (F2) mevcut duruma bağlı.
* İleri Sar (F3)
* Durdur (F4)

Hem Geri Sarma düğmesinde (F1) hem de İleri Sarma düğmesinde (F3) uygulama tuşuna, Shift F10 veya Ctrl + M tuşlarına basarak oynatmakta olduğumuz parçayı geri sarma veya ileri sarma zamanını seçmemizi sağlayacak bir menü elde edebiliriz.  

Bu menüde seçtiğimiz seçenek, tekrar değiştirilene kadar tanımlanan seçenek olacaktır.  

Oynatıcı, yukarıda belirtilen kısayol tuşlarıyla, Ayarlar ve Güncelleme iletişim kutusu dışında uygulamanın herhangi bir bölümünden veya iletişim kutusundan çalıştırılabilir.  


Oynatıcının çalıştırılamadığı bu iki iletişim kutusu açıldığında, iletişim kutuları kapatılana kadar oynatmayı duraklatır.  

Bu iletişim kutularının eylemlerinden herhangi birinin uygulamayı yeniden başlatması gerekirse, oynatmanın duracağını ve dilersek tekrar devam ettirmemiz gerekeceğini unutmamalıyız.

###kontroller

Bu bölümde, aşağıdaki seçenekleri göreceğiz:

####Ses Seviyesi: (F5 / F6):
Bu tuşlar, (Alt + V) tuşuna bastığımızda ya da kontrol odakta olduğunda, sol / sağ ok, yukarı / aşağı okla, sırasıyla ses seviyesini düşürmek veya yükseltmek için kullanılır.

####Hız: (F7 / F8):
Bu kontrole odaklanmak için de (Alt + V) basabiliriz. Bu kombinasyon hangi kontrole odaklanıldığına bağlı olarak ses ve hız arasında geçiş yapacaktır.

* F6 / F7, sol / sağ ok veya aşağı / yukarı ok ile oynatma hızını azaltabilir veya artırabiliriz. Dikkatli olmalıyız çünkü çok fazla hızlandırır ya da yavaşlatırsak, oynatma arabelleğinde veri bitebilir ve hata verebilir, bu tüm videolarda olmaz ve ayrıca sahip olduğumuz internet bağlantısına da bağlıdır.

####Ses çıkış aygıtları
Çıktı, adlı bu açılabilir seçim kutusuna (Alt + Ç) ile hızlı bir şekilde odaklanılabilir, Bu seçeneğe yalnızca oynatma paneli etkinse, öğe oynatılıyorsa veya duraklatılmışsa erişilebilir.  
Hangi cihazdan ses almak istiyorsak, ilgili cihazı seçebiliriz.  
Oynatma durdurulduğunda, yapılan seçimin varsayılana döndüğü unutulmamalıdır.  
Bu nedenle bir sonraki oynatma için başka bir cihaz istiyorsak, bunu tekrar seçmemiz gerekecektir.  
Bu seçenek şu anda teknik nedenlerden dolayı kaydedilememektedir.  
İleriki zamanlarda, bir çözüm bulunursa yapılan seçimin kaydedilebilmesi mümkün kılınacak ve kullanıcıya bilgi verilecektir.

####Video ekranı (F11):

Oynatma etkinse, oynatılıyor veya duraklatılmışsa, kontrole (Alt + P) ile hızlı bir şekilde erişebiliriz.  
Bu kontrol bir onay kutusudur, boşluk çubuğuyla işaretlediğimizde videoyu tam ekran olarak görüntülüyebilir ve içeriğini görebiliriz.  
Varsayılan olarak video görüntüsü devre dışıdır ve sadece ses oynatılır.  
Ancak Ayarlar ve Güncelleme iletişim kutuları dışında herhangi bir zamanda ve herhangi bir iletişim kutusundan F11 ile video ekranını etkinleştirebiliriz.  
Video ekranı ayrıca geri sarmak için F1, oynatmak/duraklatmak için F2, ileri sarmak için F3, durdurmak için F4 (ekran kapanır), sesi azaltmak için F5, artırmak için F6, oynatma hızını azaltmak için F7, arttırmak için F8 ve aşağıda açıklanan tuşları destekler.  
Bu ekranın ESC tuşu ile veya odak değiştirildiğinde kapanacağı ve sesin oynatılmaya devam edeceği unutulmamalıdır.  
ALT+TAB tuşlarına da bastığımızda odak değişeceği için Video ekranı kapanır.

###Menü düğmesi (Alt + M):

Bu menü, çeşitli araçlar, farklı genel seçenekler ve eylemler içerir. Bu ilk sürüm aşağıdaki seçenekleri içerir:

####Güncellemeleri Denetle:
Güncellemeler denetlenecek ve eğer bir şey bulamazsa mesaj ile bilgi verilecektir.  
Eğer yeni bir indirme bulunursa, bulunan indirme hakkında bilgi ve indirme seçeneğinin bulunduğu yeni bir iletişim kutusu açılacaktır.

####Seçenekler:
Uygulama seçeneklerini içeren bir iletişim kutusu açılacaktır (sonraki bölümde içeriği açıklanmıştır)

####Kılavuz:
Bu yardım belgesi varsayılan Web tarayıcımızda açılacaktır.

####Web sitesine Git:
Blogun ana sayfasını açacaktır.

####Hakkında...:
Bize uygulamanın derlendiği program sürümü, kitaplık sürümü ve Python sürümü hakkında bilgi verecektir.

####Çık:
Önce aktif indirmelerimiz olup olmadığını kontrol ederek uygulamadan çıkacak, bu durumda gerçekten çıkmak isteyip istemediğimizi seçmemiz gereken bir iletişim kutusuyla bilgilendirileceğiz. Ana arayüzden de Alt + F4 ile çıkış yapabiliriz.

###seçenekler iletişim kutusu:

Bu ilk sürümdeki iletişim kutusunda birkaç farklı seçenek vardır.  

Açıldığında, seçenekler karşımıza bir liste alanında gelir ve bu listede aşağı / yukarı ok tuşları ile hareket edebiliriz.  

Program yeni özellikler içerdiğinde bu iletişim kutusuna yeni bölümler ve seçenekler eklenecektir.  

İstediğimiz seçeneğin üstüne geldiğimizde sekme tuşuna basarsak o seçeneğin tercihlerine  erişiriz ve onlar arasında sekme ile hareket edebiliriz.  

Bu ilk sürüm bize aşağıdaki bölümleri sunar:

####Genel:
Bu alan genel seçenekleri içerir, kullanılabilir seçenekler şunlardır:

#####Uygulama dilini değiştir:
Bu düğmeye basıldığında uygulama tarafından desteklenen dilleri içeren bir menü açılacaktır.  
Uygulama 85 dili desteklemektedir. Lakin, şu anda sadece Türkçe, İspanyolca ve İtalyanca resmi olarak kullanılmaktadır.  
Geri kalan diller bir çevirmen tarafından otomatik olarak oluşturulmaktadır.  
Bu belgenin bir sonraki bölümünde nasıl çalıştığını, dilerseniz nasıl dil ekleyebileceğinizi ve dilinizi uygulama için nasıl resmi hale getirebileceğinizi açıklayacağız.  
Daha sonra diller hakkında çevirmenler için daha fazla teknik bilgi de vereceğiz.

#####Uygulama Başladığında Gösterilecek Sekmeyi Seçin:
Bu açılabilir seçim kutusunda, uygulamayı başlattığımızda hangi sekme ile açılacağını seçebiliriz.

#####Ana Pencere Simge Durumuna Küçültüldüğünde Sistem Tepsisinde Göster:
Bu onay kutusunu işaretledikten sonra pencereyi simge durumuna küçültürsek, pencere simge durumuna küçültülmek yerine sistem tepsisinde gizlenecek ve TCA-Media Downloader adı ve sürümü ile yeni bir simge görünecektir.  
Simge üzerinde Enter tuşuna basarsak, Geri yükle ve Çık adında iki seçeneğin bulunduğu bir menü açılır.  
Geri Yükle seçeneğği, uygulama ana penceresini tekrar ekrana getirir.  
Çık seçeneği ise, uygulamayı kapatır.  
Gelecek sürümlerde bu menü içeriği yeni seçeneklerle zenginleştirilecektir.  
Her iki durumda da sistem tepsisindeki simge kaybolur.  
Sol fare tıklaması ile de bu içerik menüsüne erişilebilirken, sağ fare tıklaması uygulama penceresini etkin hale getirecektir.

####İndirilenler:
Burada indirmelere atıfta bulunulan seçenekleri ekleyeceğiz.  

Aslında elimizde:

#####Tamamlanmamış indirmelere devam et (deneysel):
Bu kutuyu işaretlersek, bu işlevin nasıl çalıştığını açıklayan bir uyarı iletişim kutusu açılacaktır.  
ancak özetlemek gerekirse:  
İndirme işlemi tamamlanmadan uygulamayı kapatırsak, yeniden başlattığımızda kaldığı yerden indirme işlemine devam etmeye çalışacaktır.  
Ayrıca, indirilmekte olan bir kanal, oynatma listesi veya videoyu aynı bağlantı ile yeniden indirmeye çalışırsak, uygulama bu durumu algılayacak ve indirmeleri kaldıkları yerden indirmeye devam etmeye çalışacaktır.  
Bu durumda, indirme dizininde geçici dosyalar oluşacak ve indirme işlemi tamamlandığında silinecektir.

Bu seçeneğin deneysel olduğu ve doğru çalışmama olasılığı unutulmamalıdır.

####Oynatıcı:
Burada Oynatıcı seçeneklerinden söz edeceğiz.  

Şu anda, aşağıdaki seçenekler bulunur:

#####En İyi Kalitede Oynat (oynat düğmesine basıldığında kaliteyi seçmek için menü gösterilmez):
Varsayılan olarak bu kutu işaretlidir.  
O nedenle bir video oynattığımızda, bize her zaman ilgili videoyu bulabildiği en iyi kalitede gösterecektir.  
Bu kutunun işaretini kaldırırsak, Oynat butonuna tıkladığımızda:  
Düşük, orta ve en iyi kalite seçeneklerinden dilediğimizi seçebileceğimiz bir menü açılacaktır.  

Bu işaretleme kutusu, yavaş internet bağlantılarında kaliteyi düşürerek sorunsuz izlemek isteyenler için eklenmiştir.

#####Oynatma Sırasında Video Ekranını Göster:
Varsayılan olarak bu kutu işaretli değildir.  

İşaretlenirse bir video oynatılmaya başladığında video ekranı otomatik olarak açılacaktır.  

Bu ekranda F1'den F12'ye kadar olan oynatma tuşlarını kullanabiliriz.  

Video ekranı odağını kaybederse kapanır ve içeriği görsel olarak görüntülemeye devam etmek için tekrar açmamız gerekir.

####Ses:
Burada, çeşitli işlemler için atanmış sesleri özelleştirebilir, dilediğimizi etkinleştirebilir ve istemediklerimizi devre dışı bırakabiliriz.  

Şu anda aşağıdaki sesleri etkinleştirebilir veya devre dışı bırakabiliriz:

* Başlangıç ​​sesini çal (Uygulama başlatılırken yavaş yüklendiğinde ses oynatılacaktır)
* Bekleme sesini çal (bekleme diyaloglarında ses oynatılacaktır)
* Yeni indirme için ses çal (yeni bir indirme eklerken ses oynatılacaktır)
* İndirme başarıyla tamamlandığında ses çal
* Hatalı bir indirmenin sonunda ses çal
* Eylem bilgisi mesajlarını ekran okuyucuya gönder

Yukarıda sözü edilen onay kutuları işaretliyse sesler oynatılır, işaretlenmemişse oynatılmaz. Tümü varsayılan olarak işaretlenmiştir.  


Eylem bilgisi mesajlarını ekran okuyucuya gönder seçeneğinin onay kutusu işaretli olduğunda:  
Uygulamanın, Silindi, temizlendi, oynatılıyor gibi mesajları ekran okuyucu tarafından seslendirilir.  
İşareti kaldırılırsa, bu tür bilgi mesajları seslendirilmez.  

Ayrıca, Ses seviyesi, hız, geri sarma ve ileri sarma bilgileri de bu onay kutusunun işaretlenmesine bağlı olarak seslendirilir.  

Onay kutusunun işaretini temizlemiş olsak dahi okuyucuya gönderilecek olan üç tuş kombinasyonu vardır. Bunlar şunlardır:

* F9: Oynatıcıda aktif olan içeriğin geçen ve toplam süresini bize söyleyecektir. Eğer bir şey oynatılmıyorsa, Hiçbir şey oynatılmıyor bilgisini verecektir.
* F10: oynatılan içeriğin adını söyler. Oynatılmıyorsa, Hiçbir şey oynatılmıyor bilgisini söyleyecektir.
* Ctrl + O: Bu kısayol, Bağlantı sekmesinde oluşturduğumuz indirme seçenekleri hakkında bize hızlı bilgi verecektir.

Bu tuşlar, Ayarlar ve Güncellemeler dışında uygulamanın herhangi bir yerinde çağrılabilir ve kullanılabilir.  

Ayrıca, onay kutularından sonra, yine sesler için bir açılabilir seçim kutusu bulunur:

#####Örnek Sesler (bir ses seçin ve oynatmak için ctrl+r tuşlarına basın):
Bu kutuda, seçtiğimiz sesi CTRL+R tuşlarına basarak dinleyebilir ve bu şekilde uygulama tarafından tanımlanmış sesleri öğrenebiliriz.  

Sson olarak, bu seçenekler iletişim kutusunda Tamam ve İptal düğmeleri bulunur.  

Tamam, yaptığımız değişiklikleri onaylar ve İptal ise değişiklikleri gerçekleştirmeden ilgili iletişim kutusunu kapatır.  

Dil değişikliğinin uygulamanın yeniden başlatılmasını gerektirdiğini ve yalnızca etkin indirme yoksa dili değiştirmenize izin vereceğini unutmayın.

##Önemli Kısayol Tuşları:

###Oynatıcı için:

* F1: Geri Sar.
* F2: Oynat/Duraklat.
* F3: İleri Sar.
* F4: Durdur.
* F5: Ses Seviyesini Azalt.
* F6: Ses Seviyesini Arttır.
* F7: Oynatma Hızını Azalt.
* F8: Oynatma Hızını Arttır.
* F9: Geçen süre / toplam süreyi söyler.
* F10: Oynatılan içeriğin adını söyler.
* F11: Video Görüntüsünü Tam ekranda gösterir veya kapatır.
* F12: Ekran okuyucu tarafından söylenen mesajları açma veya kapatma.
* Ctrl + M: Yalnızca Geri Sar ve İleri Sar düğmelerinde  süreyi seçebileceğimiz bir menü açar.

###Video listelerinde:

* Ctrl + R: Oynat.
* Ctrl + D: İndir.
* Ctrl + I: Listede bulunulan konumu söyler.
* Ctrl + F: Listede bir konuma gitmek için iletişim kutusu açar.
* Enter: Üzerinde bulunulan öğeye göre değişebilen farklı eylemleri sunan bir menü açar.
* Boşluk Çubuğu: Seçilebilir öğe bulunan listelerde, işaretleme ve işareti kaldırma için kullanılır.

###Video olmayan diğer tüm listelerde ve metin alanlarında:

* Ctrl + B: Metin alanlarını temizle.
* Enter: Bulunduğumuz alana bağlı olarak çeşitli eylemlerin bulunduğu bir menü açar.

###Gelişmiş bir kişisel biçim seçeneği seçin iletişim kutusu:

* Ctrl + I: Açılan kutudaki konumu bildirir.
* Ctrl + F: Açılan kutuda gitmek istediğimiz konumu seçmek için iletişim kutusunu gösterir.

###Bekleme iletişim kutusu:

Her eylem gerçekleştirdiğinizde görünen bekleme iletişim kutusunda özel bir panik tuş kombinasyonu vardır.  

Bu kombinasyon:  

Shift + Ctrl + Alt + K  

Bu kombinasyon deneyseldir ve yalnızca bekleme iletişim kutusunun çok uzun sürmesi ve uygulamanın istediğimiz eylemi gerçekleştirmemesi durumunda kullanılmalıdır.  

Yalnızca belirli durumlarda ve söz konusu kutunun çok uzun süre kaldığı durumlarda kullanın.  

###Diğerleri:

* Ctrl + O: Sesli olarak bize biçim, kalite, isim ve konum bilgisini verecektir.

Bu seçenekler Bağlantı sekmesinde tanımladığımız ve indirmeler için oluşturulmuş seçeneklerdir.

* Ctrl + S: İndirme durum bilgileri.

İndirme olup olmadığını Ekran Okuyucu aracılığıyla bir mesajla bize bildirecektir.  

Varsa, bize aktif, tamamlanmış ve hatalı indirmelerin sayısını söyleyecektir.  

Bu tuş, güncelleme iletişim kutusu, ayarlar, bekleme ve konum seçme iletişim kutusu dışında uygulamanın herhangi bir yerinde çalışır.

##Uygulama dilleri hakkında bilgi:

Daha önce de belirttiğimiz gibi, bu ilk sürümde yalnızca İspanyolca, İtalyanca, Rusça, Ukraynaca ve Türkçe resmidir. Geri kalan 82 dil bir çevirmen tarafından otomatik olarak oluşturulur.  

Birisi resmi bir dile katkıda bulunmak istiyorsa, aşağıdaki adımları takip etmelidir.  

DATA/LOCALE dizininde tüm diller bulunur. Sadece kendi dilinize gidin ve base.po dosyasını değiştirin.  

Makine çevirisini temizleyebilir, düzeltebilir veya kendiniz yeni çeviriyi oluşturabilirsiniz.  
ardından değişikliklerinizi kaydederek .po dosyasını oluşturabilirsiniz.  
Bu aşamalardan sonra, uygulamayı yeniden başlattığınızda yaptığınız değişiklikleri görebilirsiniz.  

Oluşturduğunuz dili resmi hale getirmek istiyorsanız:  
İlgili dil dosyasını Tecnoconocimiento Accesible blog sayfasında bulunan iletişim bilgilerini kullanarak bize ulaştırabilirsiniz.  

Diliniz dahil edilenler arasında değilse, yine de ekleyebilirsiniz.  

DATA/LOCALE klasöründe main.pot adlı dosyayı açarak kendi diliniz için bir po şablonu oluşturabilirsiniz.  

Daha sonra dilinizi eklemek için kullandığınız dizin yapısını takip edin ve base.po dosyasını çevirinizle birlikte eklemek istediğiniz yeni dilin dizinine kaydedin.  

Uygulama bir dahaki sefere başlatıldığında, dilinizi seçebileceksiniz.  

Ayrıca base.po dosyasını yeni dille birlikte blog yetkilisine gönderebilir ve yeni dil seçeneğini resmi olarak ekletebilirsiniz.  

Dil dosyalarını gönderdikten sonra, eğer bir güncelleme gelirse, ilgili güncellemeyi indirmeden önce dil dosyanızın yedeğini aldığınızdan emin olun ve daha sonra güncelleştirme işlemini gerçekleştirin.  
Yeni dosyalar, locale klasörüne yazılacağı için, herhangi bir sorun halinde kendi dosyalarınızı kaybetmemeniz için şidetle yedeklemeniz önerilir.  
İndirilen dil dosyaları sorunlu olursa, kendi yedeğinizi yukarıda belirtilen konumlara el ile tekrar yapıştırarak kullanıma devam edebilirsiniz.  

Aksi takdirde, dediğim gibi güncelleme, resmi olmayan herhangi bir değişikliği silecektir.  

Değişiklik resmiyse, değişiklikler kaybolmaz.  

Ayrıca, yalnızca resmi çevirilerin desteklendiği belirtilmelidir.  

otomatik çeviriler doğru çalışmaz ve çevirileri mükemmel değildir, aksine kesinlikle birçok hataları vardır, ancak çoğu durumda başka bir dil bilmeyen kullanıcının uygulamayı kendi dilinde kullanabilmesi için yararlı olabilirler. 

##teknik açıklamalar

DATA/LOGS dizinindeki uygulama hata ayıklama dosyalarını deoplanır.  

Bu dosyalar oluşabilecek hatalar hakkında bilgi içerir, bu yüzden istenmektedir.  
bir hata rapor edilirse, bu dosyaların eklendiğini kesin olarak belirtir.  

Bir hata oluştuğunda, günlük dosyaları zaman damgalı olduğundan, tam olarak ne zaman oluştuğunu görmeye çalışın, bu nedenle dosyada birden fazla hata varsa, bu dosyalar ve hatanın oluştuğu saat ile tespit edilmesi daha kolaydır.  

Uygulamanın hiçbir zaman donmaması veya kullanılamaz hale gelmemesi ve ortaya çıkabilecek hataların çoğunun giderilmesi için önlemler alınmaya çalışılmıştır.  

Ancak, kesinlikle hepsini düşünmenin imkansız olduğunu belirtmeliyiz. bu nedenle yapılan farklı güncellemelerle uygulamayı giderek daha sağlam hale getirmeye çalışacağız.  

Ayrıca indirme eklemenin kötüye kullanılmasına karşı uyarı bulunur. Eklediğimiz her indirme kaynak gerektirir. Bu nedenle çok fazla indirme eklenirse ve bilgisayarımızın yeterli kaynağı yoksa bilgisayarın sorun yaşayacağı unutulmamalıdır.  

Sorumlu bir şekilde kullanın ve her indirmenin RAM ve internet bant genişliği gerektirdiğini dikkate alın.

##Açıklamalar:
Bazen, görünüşe göre video içermeyen bir kanal bulabiliriz.
Bu durumda şu şekilde ilerleyeceğiz:

1. Arama sonuçlarına dönmek için Escape tuşuna basacağız
2. Kanalın sonucu üzerinde enter tuşuna basıyor ve bilgilere erişiyoruz
3. Bir defa CTRL + Sekme tuşlarına basarak Kanal listesine erişiyoruz
4. Burada varsa kanalları bulabilir ve söz konusu kanaldan indirilecek videoları seçebiliriz.

#Teşekkürler:

Beta aşamasındaki testçilere, Gera, Gustavo, Peter, Pepe, Rosa, Romina, Rayo, Óscar, Simone, Umut ve kesinlikle unuttuğum birine özel bir teşekkür etmek istiyorum.  

Aynı şekilde resmi tercümanlara da:

* İtalyanca: Simone Dal Maso
* Türkçe: Umut KORKMAZ
* İngilizce: slanovani
* Ukraynaca: Ivan Shtefuryak, Volodymyr Pyrig
* Rusça: Valentin Kupriyanov

#Değişiklik günlüğü.<a name="Değişiklik günlüğü"></a>

Bu bölümde, güncellemeler çıktıkça bir yönlendirme olarak, ana belge değiştirilmeden yeni işlevlerin ekleneceğini unutmayın.  

Bu nedenle, uygulamaya ilk sürümünde aşina olduktan sonra haberleri görmek için bu bölümü ziyaret etmeniz önerilir.  
Çünkü, burada yeni işlevler, açıklamaları ve Tuş kısayolları eklenecektir.  

Yalnızca özellikler ve Tam dallara ait güncelleştirme sürümleri eklenir.  

Kitaplık dalı, uygulamanın işlenmesinde hiçbir şeyi değiştirmeden hata düzeltmeleri ve dahili kitaplıklar için güncellemeler olacaktır.  

Değişikliklerden haberdar olmak için bu bölümü incelemek kullanıcının sorumluluğundadır.  

## Sürüm 3.0.2.0.

* TCA-Media Downloader'ın geliştirme dallarını değiştirme yeteneği eklendi.

Seçenekler/genel içerisinde, Geliştirme dalını değiştir adında bir düğmemiz bulunur.

Bu butona basarsak, Kararlı olan son dal ile haberi ilk alan ancak hatalar içerebilen beta arasında geçiş yapmamızı sağlayacaktır.

* Adlandırılmış kanallardan bilgilerin çıkarılması düzeltildi

Artık kimlik yerine adı olan kanallar doğru şekilde görüntülenecektir.

* Arama sonuçlarından veritabanına ekleme imkanı da eklendi.

Artık videolar, oynatma listeleri veya kanallar olsun bir sonuç girebiliyoruz ve içerik menüsündeki son seçenek, favoriler veritabanıyla etkileşime girmemize olanak tanıyacak.

Video, oynatma listesi veya kanal bilgisi diyaloglarındaki seçeneklerin aynısına sahip olacağız.

* Bağlantı alanına Ctrl + R ve Ctrl + D eklendi.

Artık Bağlantı sekmesinde bir YouTube videosunun bağlantısını yapıştırırsak, içerik menüsünü görüntülemeye gerek kalmadan oynatmak veya indirmek için bu kombinasyonlara basabiliriz.

* Oynatma Listesini göstermeyen kanallarla ilgili sorunlar düzeltildi.

* YouTube kısa URL'lerinin görüntülenmesi eklendi.

Artık Bağlantı sekmesinde bir Adres girdiğimizde ve bu bağlantı eşleştiğinde
Shorts türlerinden birinde sanki bir YouTube videosuymuş gibi aynı seçenekler sunulacak ve
söz konusu bağlantılarla sanki bir videoymuş gibi etkileşim kurabilmek mümkün olacak.

* YouTube klip bağlantısı görüntüleme eklendi.

Artık Bağlantı sekmesine bir YouTube klibinin adresini eklersek, bu bize dilediğimiz biçimde veya orijinal olarak indirme imkanı verecektir.

Ayrıca klibin çıkarıldığı videonun orijinal dosyasıyla karıştırılan klip hakkında bilgi edinmemizi de sağlayacaktır.

Klipler Ctrl + R kombinasyonu ile oynatılamaz ve tekrar oynatılamaz.

Klipler ayrıca sık kullanılanlar sekmesine de eklenemez.

* DATA klasörüne bir DEV dizini eklendi.

Bu dizin, çevirmenlerin üzerinde çalışacağı belgeleri, dizeleri içeren resmi dilleri ve çevrilmesi gerekenleri ve yeni dil şablonları için main.pot'u içerir.

Artık bu rehberde bulunan çeviriler alınana kadar diller resmi dillerde otomatik çeviri ile gelecektir.

Yalnızca bir sürümden diğerine eklenen dizeler otomatik olarak çevrilecektir. Bu şekilde program her zaman tercüme edilecek ve resmi tercüman çevirilerine daha fazla güvenebilecektir.

Bu dizinde, tercüme edilmek üzere kalan dizelerle birlikte resmi çevirmenin çalışması bulunmaktadır.

* YT-DLP kütüphanesinin dalını seçme yeteneği eklendi.

Artık Seçenekler/Genel içerisinde YT-DLP kütüphanesinden kullanılacak dalı seçebiliriz.

Kararlı ve Gecelik sürümleri arasından seçim yapabiliriz.

Kararlı sürümü, kütüphanenin son sürümüdür ve Gecelik, yeni özellikleri içeren ancak kararlı kadar test edilmemiş bir sürümdür.

* YT-DLP güncellemelerini denetleme seçeneği eklendi.

Artık Güncellemeleri denetlediğimizde uygulama dışında YT-DLP kütüphanesinin olup olmadığını da denetleyecek.

Eğer varsa, bizi bilgilendirecektir. Varsayılan olarak, her zaman önce uygulamanın bir güncellemesi olup olmadığını kontrol eder ve varsa, YT-DLP'yi kontrol etmez çünkü güncellemelerde YT-DLP her zaman Kararlı dalın en son sürümüyle güncellenir.

Uygulama güncellemesi bulamazsa YT-DLP'yi kontrol etmeye devam edecek ve bizi bilgilendirecektir.

Uygulamayı güncellersek ve YT-DLP Nightly dalını seçersek, uygulamayı yükledikten sonra ilgili dalı indirmek için tekrar güncelleme aramamız gerekecek.

İkincisi, uygulama güncellemelerinin yalnızca Kararlı dalını taşımasıdır.

* Güncelleme bildirimlerine YT-DLP için güncelleme bildirimleri de eklenir.

Güncelleme bildirimlerini aktif hale getirdiysek artık YT-DLP kütüphanesini de arayacak ve bulursa bize sürüm numarasını verecektir.

Menüde güncelleme aradığımız gibi oluyor, eğer uygulama güncellemesi bulursa biz uygulamayı güncelleyene kadar artık YT-DLP'yi aramıyor.

* Seçeneklere, Sık kullanılanlar sekmesiyle başla seçeneği de eklendi.

* MASTODON ile paylaşım düzeltildi.

* YT-DLP kitaplığı 2023.07.06 sürümüne güncellendi.

* Daha iyi uygulama performansı için dahili kütüphaneler güncellendi.

* Dahili hatalar düzeltildi.

* Çeviriler güncellendi.

## Sürüm 3.0.1.0.

* Sık Kullanılanlar (Alt + 4) adlı yeni sekme.

Artık bu sekmede istediğimiz videoları, oynatma listelerini veya kanalları hızlı bir şekilde erişebilmek için kaydedebiliriz.

Bu sekmeye girdiğimizde 3 Dal olacak:

Alt + S: Bizi dallarla etkileşime geçebileceğimiz ağaç alanına bırakacak.

Bu Ağaç alanında, Sık Kullanılanlar adında bir dal bulunur ve üzerindeyken Enter tuşuna bastığımızda yeni bir içerik menüsü açılır. Menüde, Tüm veritabanını temizle ve Veritabanını yedekle/geri yükle seçenekleri bulunur.

Veritabanını Yedekle/Geri Yükle seçeneğinin alt menüsü bulunur ve bu alt menüde: Yedek Oluştur ile Yedeği geri yükle seçenekleri bulunur.

Sık Kullanılanlar dalını sağ ok ile genişlettiğimizde: Videolar adlı ilk alt dalına erişiriz. Üzerinde Enter bastığımızda, Yeni Video Listesi seçeneği bulunur. Enter ile onayladığımızda, oluşturulacak bu listeye bir ad verebileceğimiz yazma alanı karşılar bizi.

Video listelerini eklediğimizde, dalı genişletebileceğiz ve enter tuşuna basarsak video listesini düzenleyebileceğimiz, silebileceğimiz veya boşaltabileceğimiz alt dallara sahip olacağız.

Ayrıca ağaç alanında Oynatma Listeleri ve Kanallar adlı iki dalımız var, bu dallardan herhangi birinin içeriği varsa, üzerine enter tuşuna basabilir ve içeriğini silebiliriz.

Alt + i: Bizi içerik alanında bırakır, bu alanda seçtiğimiz videoların listesinin içeriği, Oynatma Listesi veya Kanallar görüntülenir.

Bu alanda, herhangi bir giriş öğesine tıklarsak, videolar, oynatma listeleri veya kanallar kategorisine karşılık gelen bir menü gösterilecek ve onlarla etkileşim kurmamızı sağlayacak.

Alt + A : Bulunduğumuz dalda arama yapabileceğimiz bir kutucuğa götürecektir bu kutucuğa aradığımızı büyük yada küçük harfle yazıp entera basarak sorgu alanında sonucu bize verecektir. , üzerine enter tuşuna basarak sonuçla etkileşime geçebiliriz.

Arama alanı, eksiksiz olmasına gerek kalmadan bir metin girmenize olanak tanır; örneğin, TCA'yı ararsak, bulunduğumuz şubede bu harfleri içeren tüm videoları döndürür.

Arama kutusunda Ctrl + B tuşlarına basarak veya yazdığımız metni silip enter tuşuna basarak aramayı orijinal değerlere döndürebilir ve içerik alanını hızlı bir şekilde eski haline getirebiliriz, ayrıca içerik alanından eğer bir arama yapılmışsa Ctrl + B tuşlarına basarsak orijinal değerlere dönmüş oluruz.

Veritabanına içerik eklemek için her dalın bilgilerinden faydalınılır. Örneğin, arama sekmesinden oluşturduğumuz bir listeye bir video eklemek istiyorsak, bulunduğumuz öğede arama sonuçları olduğunda enter tuşuna basarız ve video bilgilerini veririz, şimdi açılan pencerede Video listesine ekle adlı bir düğmemiz olacak ve buna basarsak veritabanında oluşturduğumuz tüm video listelerini içeren bir menü görüntülenecek ve birini seçersek video bu listeye kaydedilecektir.

Aynı videoyu birden çok listeye ekleyebiliriz ancak her listeye yalnızca bir kez eklenebilir.

Oynatma listesi ve kanallara gelince, bilgi iletişim kutusuna benzer ve sık kullanılanlara ekle adlı bir düğme göreceğiz, eğer basarsak veritabanının ilgili dalına eklenecek, düğme daha sonra Sık kullanılanlardan kaldır olarak adlandırılacak ve sık kullanılanlar sekmesinden veya bilgi iletişim kutusundan silmesek de, söz konusu oynatmaa listesi veya kanal veritabanında olacaktır.

Oynatma listesi ve kanal dalları yalnızca aynı öğeyi kaydeder, Bağlantı farklıyken aynı adla birkaç tane kaydedebilir.

İlgili alanda, hangi konumda olduğumuzu öğrenmek için Ctrl + I tuşlarına ve istenen öğeye hızlıca gitmek için Ctrl + F tuşlarına basabiliriz.

* Bir videodaki yorumları görme yeteneği eklendi (deneysel).

Şimdi video bilgileri iletişim kutusunu açtığımızda, söz konusu videoda yorum varsa bir düğme görünecektir.

Düğmenin adı Yorumları görüntüle veya kaydet'tir ve tıkladığınızda yorumlarınızı görüntülemenize veya kaydetmenize izin verir.

Bu seçenekler deneyseldir ve bazen uygulamanın kapatılabileceği tespit edilmiştir, bu nedenle devam eden indirmeler varsa kullanıcıya indirilmekte olan bilgilerin kaybolabileceği bildirilir.

Yorumları Gösteri seçersek, Alınan yorumların yüzdelik oranlarla gösterildiği bir yorum alma penceresi görünecektir, pencerenin iptal düğmesine tıklayarak almayı iptal edebiliriz.

Alma işlemi bittiğinde, tüm yorumların olduğu bir pencere açılacak, pencerede yorumlar bir ağaç görünümünde görünecektir.

Ağacı genişletebilir ve yorumlar arasında gezinebiliriz, yorumun yanıtları varsa yanıtlarını görmek için de genişletebiliriz.

Çok uzun yorumlar, yorumun tamamı sığmayacağı için sonunda bir ** ile görünecektir.

Yorumun tamamını okuyabilmek için yeni bir kısayol tanımlanmıştır. Bu kısayol: CTRL+T olarak belirlenmiştir.

Aynı şekilde, sekme tuşuna basarsak, yorumun tamamının yanı sıra gönderen kişinin adı, tarih ve benzerlerinin de yer aldığı salt okunur bir kutuya erişiriz.

Bu pencerede Kaydet adlı bir buton bulunur. İşlevi içerik menüsündeki video bilgi penceresindeki ile aynıdır ve yorumları erişilebilir bir html'ye kaydetmektir.

Html yapısı aşağıdaki gibidir:

Videonun başlığı için 1. seviye başlık.

Ana yorum için 2. seviye başlık.

Yoruma verilen yanıtlar için, üçüncü seviye başlık.

Tüm pencerede hızlı bir şekilde hareket etmek için kısayollar bulunur:

Alt + L: Bizi Yorumların listesinde bırakır.
Alt + Y: Seçili yorumun detaylarına gider.
Alt + D: Yorumları html dosyasına kaydeder.
Alt + K, Alt + F4 veya Escape: Pencereyi kapatır.

* Bağlam menülerindeki yeni özellikler ve iyileştirmeler.

İndirme alanındaki bağlamsal menüler düzeltildi, artık video olmayan öğelerde oynatma gösterilmiyor.

Yalnızca bir video sonucu varsa, çoklu indirme menüsünün görünmemesi, ayrıca veritabanında yalnızca bir video varsa görünmemesi düzeltildi.

Bu menülere bağlama uyan yeni seçenekler eklendi, örneğin:

Tarayıcımızda seçtiğimiz videoyu, oynatma listesini veya kanalı açarak bizi YouTube'a götürecek olan WEB'de aç.

Paylaş adlı bir alt menü eklendi.

Bu menü, Bağlantıyı Twitter, Facebook, Telegram, WhatsApp, Mastodon ile veya cep telefonumuzla QR kodu ile paylaşmamızı sağlayacaktır.

Cep telefonuyla açmak için QR kodu oluştur'u seçersek, ekranın ortasında QR kodu içeren bir pencere açılacaktır. Cep telefonumuzun okuyucusuyla algıladıktan sonra işaret edersek, bu Bağlantı cep telefonumuzda video, oynatma listesi veya kanal olarak açılacaktır.

Facebook'un yalnızca Bağlantıyı paylaşmamıza izin verdiğini, bu nedenle otomatik olarak metin ekleyemeyeceğimizi, ancak bize bıraktığı ekranda elle bilgi ekleyebileceğimizi unutmayın.

Mastodon'da bizden içinde bulunduğumuz örneğin Bağlantısını isteyecek, istersek onu kaydedebilir veya değiştirebiliriz. Kaydedersek, önceden tanımlanmış olacak ve Mastodon ile her paylaşmak istediğimizde onu girmek zorunda kalmayacağız.

Herhangi bir sosyal ağ üzerinden paylaşım yapabilmek için öncelikle tarayıcımıza giriş yapmalıyız, tıpkı hem WhatsApp hem de Unigram uygulamaları yüklüyse paylaşım daha kolay olacağı gibi.

* Ayarlar iletişim kutusuna yeni seçenekler eklendi.

Genel kategorisine Eklenenler:

Güncellemeleri kontrol et ve bildir: Bu açılan kutu ile güncellemeleri aramasını ve bir Windows bildirimi ile bizi bilgilendirmesini isteyip istemediğimizi seçebiliriz.

Açılan kutudaki herhangi bir zamanı seçebilir, devre dışı bırakabilir veya güncellemeleri arayabiliriz.

Bir güncelleme bulduğunda, bir güncelleme ve sürümünü bulduğunu bildiren Windows bildirimi gösterilir.

Bu seçenek güncellemeleri indirmez, yalnızca seçtiğimiz her x seferde bir güncelleme olup olmadığını kontrol eder, bu nedenle indirmek için güncellemeleri denetlememiz gerekecek.

Biz güncelleme yapana kadar her x seçili zamanda bildirimler bize gösterilecek.

İndirilenler kategorisine eklenenler:

Alınacak bilgiler için bekleme süresi (tüm bilgiler alınmamışsa hata verir, büyük Oynatma Listesi veya Kanallar için geçerlidir): Bu birleştirilmiş tabloda, bilgilerin elde edilemediğini söylemek için geçen süreyi artırabiliriz.

Çoğu Oynatma Listesi ve Kanal için makul bir süre ve fazlasıyla yeterli olduğundan, varsayılan olarak bilgilerin alınmaya çalışıldığı 2 dakika seçilidir.

Oynatma listelerinde veya kanallarda 5.000'den fazla video olduğu için daha fazla zamana ihtiyacımız olursa, veri elde etme süresini artırabiliriz.

* Tüm iletişim kutularında canlı yayınların indirilmesine karşı koruma eklendi.

İndirmek istediğimiz Bağlantı canlı yayın ise algılanacak ve izin vermeyecek bir koruma eklendi.

Bu sorunlara neden oldu ve gelecek sürümlerde alternatif bir çözüm verilecektir.

* Uygulamanın daha iyi performans göstermesi için dahili kütüphaneler güncellendi.
* Dahili hatalar düzeltildi.
* Çeviriler güncellendi.


## Sürüm 3.0.0.0:

* İlk sürüm.
