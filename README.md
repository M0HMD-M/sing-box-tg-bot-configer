# sing-box-tg-bot-configer


## راه اندازی بات

اگر نسخه های قبلی بات(بعد از ۱۴۰۲/۲/۲۵) رو دارید و فعاله می‌تونید به دستور زیر به روزش کنید و مجبور نباشید همه چی رو از اول راه‌اندازی کنید. 
```bash
curl -Lo /root/update.py https://raw.githubusercontent.com/hrostami/sb-server-configer/master/Update.py
python3 update.py
```
اول فایل first.py رو میگیریم که توکن بات تلگرام رو به راحتی ست کنید و بقیه کار رو هم خودش خودکار انجام میده شما نیازی نیست کاری انجام بدید.
```bash
curl -Lo /root/first.py https://raw.githubusercontent.com/hrostami/sb-server-configer/master/first.py
```
حالا بریم سراغ اجرا کردن اسکریپت. فقط لازمه که توکن بات تلگرام رو در ادامه این دستور وارد کنید، بقیه موارد (آی پی، پورت، ارسال پیام به کانال یا شما، آیدی کانال و بازه زمانی تجدید کانفیگ) رو بعدا تو تلگرام با دستور set/ تعریف میکنیم و هر وقت هم خواستیم میتونیم تغییرشون بدیم:
```bash
python3 first.py توکن_بات_تلگرام
```
 __یادتون نره به جای توکن تلگرام تو دستور بالا توکن بات خودتون رو قرار بدید! بعنوان مثال مثل دستور پایین بشه__

```bash
مثال
python3 first.py 1234567890:Abcdefgh_ZoCIX14i4PSBnBUnUGwUHJM
```
هر وقت خواستید هر کدوم از پارامتر ها رو تغییر بدید تو بات تون با دستور set می‌تونید این کار رو انجام بدید. 

بعد از اینکه تموم شد دستور زیر رو اجرا کنید که فایل first.py که دیگه بهش احتیاج نداریم حذف بشه:
```bash
rm first.py
```
### نحوه استفاده از بات
اسکریپت مون که اجرا و تموم شد *قبل از هر چیزی* دستور start/ رو براش بفرستید. شما با ارسال دستور start/ در تلگرام به بات تون آی دی شما بعنوان صاحب ست میشه و دیگه بات فقط به شما جواب میده. بعد از این دستور لازمه که با دستور set/ پارامتر های بات رو ست کنیم. دستور set/ رو که بفرستید بات راهنمایی تون میکنه چطور بقیه کار رو انجام بدید.

در نظر داشته باشید برای اینکه بات بتونه تو کانالی که براش تعریف کردید پیام بده باید اونجا ادمین شده باشه!

اگر بعد از اینکه پراکسی رو راه انداحتید کانفیگ تون تایم اوت داد اس ان آی  جدید براش بفرستید تو تلگرام و دوباره امتحان کنید. پیامی که به بات تلگرام میفرستید هم به این شکل باشه
```bash
/replace sni
```
با دستور status/ هم میتونید استاتوس سینگ باکس یا کانفیگر رو تو تلگرام دریافت کنید که ببینید سینگ باکس در چه وضعیتیه و اگه مشکلی هست از کجاست.
```bash
/status sing-box
/status configer.service
```
با دستور run/ هم میتونید هر دستوری که خواستید تو ترمینال اجرا کنید و نتیجه ش براتون ارسال میشه
```bash
/run command
```
بعنوان مثال دو تا دستور پر کاربرد برای چک کردن پورت ها و ریستارت کردن سرور:
```bash
/run netstat -tulnp
/run reboot
```


*با تشکر از همه کسایی که برای دسترسی آزاد به اینترنت زحمت میکشن از جمله سگارو عزیز و تیم IRCF*
