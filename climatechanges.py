import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def iklimdeğişikliğinedir(ctx):
    await ctx.send(f' İklim değişikliği, "nedeni ne olursa olsun iklimin ortalama durumunda ve/ya da değişkenliğinde onlarca yıl ya da daha uzun süre boyunca gerçekleşen değişiklikler" biçiminde tanımlanmaktadır.')

@bot.command()
async def nasılönleyebiliriz(ctx):
    await ctx.send(f'Gereksiz teklonojik,fişe bağlı ağletleri kapatarak. Toplu taşıma kullanarak. Ağaç dikerek. Işıklar kullanılmadığı sürece kapalı tutarak. petekleri kombiyi kısarak veya kapatarak ve bunun gibi havaya kötü kokular yayan, çevrenin yok edilmesini sağlayan ,doğal kaynaklarımızı yok ettiğini düşündüğün her şeyi yapabilirsin.')

@bot.command()
async def önerdiğinvideolarvarmı(ctx):
    await ctx.send(f'Barış Özcan-ın "https://youtu.be/HStCv8ixyWg?si=y1DEodYGxefvb395" bu videosu ile "https://youtu.be/6PiX-sGNFLM?si=lcQTRSlNZMyVVyfT" bu videosunu izlemeni tavsiye ederim ' )

@bot.command()
async def iklimdeğişikliğinindoğalnedenlerinelerdir(ctx):
    await ctx.send(f'Yanardağ patlamalarının yaydığı aerosoller. Güneş lekelerinin oluşturduğu manyetik alanlar sebebi ile yükselen sıcaklığının etkisi.Güneş patlamalarının yaydığı radyasyon sebebi ile sıcaklık yükselten etkisi.Donmuş toprak (kutuplar ve tundra ikliminin hakim olduğu bölgelerde) alanlardaki karbon sızıntısı. Doğal kaynaklı orman yangınları. Su buharı.Hayvan dışkı ve tüketiminin metan gazı ve karbondioksit salınımına etkisi sayılabilir.')


@bot.command()
async def iklimdeğişikliğininyapaynedenlerinelerdir(ctx):
    await ctx.send(f'Fosil yakıtların (kömür, petrol ve doğalgaz) ve organik materyallerin yakılması ile atmosfere karışan kükürt dioksit kaynaklı sülfat aerosolleri. Orman kıyımı ve insan kaynaklı orman yangınları. Çöp ayrıştırmama sonucu büyüyen katı atık sahaları.Nüfus fazlalığı sonucu karbon ayak izi oranlarının yükselmesi. Madencilik sonucu salınan gazlar ve yeryüzü yapılarındaki değişim.Tüketim alışkanlıkları sayılabilir.')

@bot.command()
async def iklimdeğişikliğinelereyolaçar(ctx):
    await ctx.send(f'Deniz seviyelerinin yükselmesi. Donmuş kıta parçalarının yapılarının değişmesi. Dağlık bölge yapılarının değişmesi. Canlı ekosistem yapısının bozulması. Gıda üretim sisteminde geri dönülemez aksaklıkların meydana gelmesi.Hava olaylarının doğal afetler düzeyine çıkması gibi sonuçlara yol açar.')

@bot.command()
async def önerdiğinbirwebsitesivarmı(ctx):
    await ctx.send(f'"https://www.aydemperakende.com.tr/blog/iklim-degisikligi-nedir-etkileri-ve-alinabilecek-onlemler" Bu siteyi öneririm.')







bot.run("YOUR TOKEN IS HEREE")
