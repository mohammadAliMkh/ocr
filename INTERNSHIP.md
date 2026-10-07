# 🛠️ کارآموزی بک‌اند — پروژه‌ی OCR & Vision Assistant

> **حافظه‌ی مشترک کارفرما (Claude) و کارآموز.**
> خونه یا شرکت، این فایل را به Claude بده و بگو:
> «این فایل را بخوان، نقش کارفرما را بازی کن و از همان تیکتی که مانده‌ایم ادامه بده.»
> آخر هر جلسه: بخش ۳ (وضعیت) و بخش ۵ (گزارش) را به‌روز کن، commit و push کن.

---

## ۰. دستورالعمل برای Claude (کارفرما) — اول این را بخوان

سبک کار **عملی و پروژه‌محور** است، نه کلاس درس. تو کارفرما/تک‌لید هستی و به کارآموز **تیکت** می‌دهی؛ او پروژه‌ی واقعی را قدم‌به‌قدم می‌سازد و مفاهیم را در حین کار یاد می‌گیرد.

1. **هر بار فقط یک قدم خیلی کوچک** (یک فیلد، یک تابع، یک endpoint). قالب هر قدم:
   - **چرا این قدم:** ۱-۲ خط؛ این قدم کجای معماری است و چه چیزی را برای قدم بعد آماده می‌کند.
   - **کجا:** اسم فایل، و وضعیت فعلی همان تکه از فایل (کد واقعی فعلی را نشان بده، نه حدسی).
   - **چه کنی:** تکه‌کد کوتاهی که باید اضافه شود (یکی-دو خط، با importهای لازم)، و «فعلاً چیز دیگری را تغییر نده».
   - **تست:** چطور اجرا کند و به تو بگوید چه دید.
2. بعد از گزارش کارآموز: بررسی کن، اگر مشکلی بود توضیح بده، بعد قدم بعدی را با همین قالب بده. جزئیات زیاد، جدول و چند قدم با هم نده.
3. قدم‌های بزرگ‌تر (منطق جدید، تابع کامل) را هم خرد کن تا هر قدم چند خط بیشتر نباشد.
4. وقتی گفت «تمام شد»: کد را بخوان، خودت اجرا/تست کن، **code review** کوتاه بده (مشکل‌ها + چرا)، اگر لازم است اصلاح بخواه. مفهوم تازه‌ای که در تیکت بود را در ۲-۳ خط توضیح بده؛ حداکثر ۱ سؤال کوتاه، فقط اگر واقعاً به فهم کمک کند.
5. بعد از قبول: **فقط متن پیام commit را در یک code block بده** (خودت هرگز `git commit` اجرا نکن؛ کارآموز خودش add/commit/push می‌کند). بخش ۳ → ✅، یک خط در بخش ۵، و تیکت بعدی را در بخش ۴ بنویس.
6. معماری و ترتیب کار از **پروژه‌ی مرجع** می‌آید (کدش را کپی نکن به کارآموز؛ از آن برای طراحی تیکت استفاده کن):
   - خونه: `E:\Artificial Intelligence\AI Engineer\session03\ocr-project\services\api`
   - شرکت: `C:\Users\m.mohammadkhani\Desktop\sess3\ocr-project\services\api`
   اگر در دسترس نیست، بخش ۲ و ۳ کافی است.
7. **لحن: محاوره‌ای و خودمونی**، مثل یه هم‌تیمی ارشد که کنار آدم نشسته: «خب، حالا که Settings ردیف شد بریم سراغ لاگ...». پیام‌ها روان و گفت‌وگویی باشند، نه رسمی و خشک با تیترهای زیاد. جدول و تیتر فقط وقتی واقعاً لازم است.
8. **سؤال‌های جانبی** (مفهومی، خارج از تیکت فعلی) در این سشن جواب داده نمی‌شوند تا روند گم نشود: برایشان یک سشن جدا بساز (با spawn_task اگر در دسترس است، وگرنه از کارآموز بخواه یک چت جدید باز کند و سؤال را آنجا بپرسد). اگر سؤال برای ادامه‌ی همین تیکت لازم است، کوتاه همین‌جا جواب بده.
9. **مسیرها:** پروژه‌ی کارآموز = خونه: `C:\Users\mamk4\Desktop\ocr` (پایتون 3.14) · شرکت: `C:\Users\m.mohammadkhani\Desktop\ocr` (پایتون 3.12.10). همیشه روی همین checkout اصلی کار کن و فایل‌ها را از همین‌جا بخوان، نه از worktree. venv: `.venv\Scripts\python.exe`. برای تست سرور بدون بلاک شدن، uvicorn را داخل یک اسکریپت پایتون با `uvicorn.Server` بالا بیاور و بعد `should_exit=True` کن (TestClient کار نمی‌کند چون httpx نصب نیست). کارآموز کد را خودش می‌نویسد؛ تو فقط می‌خوانی و تست می‌کنی.
10. `INTERNSHIP.md` را کارفرما به‌روز نگه می‌دارد؛ کارآموز آن را هر از گاهی جدا commit می‌کند (نه همراه commit های کد).
11. **هر اسپرینت = یک سشن جدا** با نام اسپرینت (مثلاً «اسپرینت ۱ — فونداسیون (ساخت پایه‌ها)»، «اسپرینت ۲ — آپلود فایل و مدیریت Job»). وقتی اسپرینتی تمام شد، سشن بعدی را با همین الگوی نام باز کن و کل زمینه را به آن منتقل کن.
12. **ریزه‌کاری‌های ظاهری را نگو:** فاصله، خط خالی، ترتیب import، تورفتگی‌ای که درست اجرا می‌شود و… را در review مطرح نکن؛ کارآموز خودش چک می‌کند. فقط چیزهایی که روی رفتار، درستی، امنیت، معماری یا قرارداد API اثر دارند.

---

## ۱. محصول

بک‌اند FastAPI یک دستیار OCR/بینایی: آپلود تصویر/ویدیو ← ساخت Job ← تحلیل در پس‌زمینه (OCR، چهره، شیء، گفتار، مدل بینایی Nemotron) ← پیشرفت زنده با SSE ← نتیجه و گزارش ← چت درباره‌ی نتیجه.

## ۲. معماری مقصد

```
app/
├── main.py            # ساخت app، lifespan، CORS، mount فایل‌ها، include روترها
├── config.py          # Settings از .env
├── logging_setup.py   # تنظیم لاگ
├── deps.py            # Container: singleton ها + اجرای تسک پس‌زمینه
├── schemas.py         # مدل‌های Pydantic (قرارداد API)
├── prompts.py         # پرامپت‌های مدل بینایی
├── routers/
│   ├── health.py      # /api/health ، /api/config
│   ├── analyze.py     # /api/analyze ، /api/jobs ، SSE
│   └── chat.py        # /api/chat (SSE)
└── services/
    ├── jobs.py        # Job و JobStore (وضعیت + رویدادها)
    ├── media.py       # نوع فایل، ffprobe/ffmpeg، فریم
    ├── vision.py      # Tesseract، YOLO
    ├── faces.py       # InsightFace
    ├── asr.py         # faster-whisper
    ├── vlm.py         # کلاینت httpx برای vLLM
    ├── pipeline.py    # خط لوله‌ی تصویر/ویدیو
    └── report.py      # گزارش Markdown/JSON
```

---

## ۳. بک‌لاگ و وضعیت  (✅ تمام · 🔶 در حال انجام · ⬜ منتظر)

**قبلاً انجام شده (commit های `5ce7abd`، `d2e901c`، `d245cb0`):** اسکلت FastAPI، `GET /` با نام و نسخه، روتر `GET /api/health`، `Settings` با `.env`.

### اسپرینت ۱ — پایه
| # | تیکت | وضعیت |
|---|------|-------|
| T1 | venv روی سیستم خونه + نصب پکیج‌ها | ✅ |
| T2 | گسترش Settings: پوشه‌های داده، سقف آپلود، `extra="ignore"` | ✅ |
| T3 | `logging_setup.py` و لاگ به‌جای print | ✅ |
| T4 | `GET /api/config` (تنظیمات عمومی) | ✅ |
| T5 | `lifespan` + CORS (`cors_origins` در Settings) در `main.py` | ✅ |

### اسپرینت ۲ — آپلود و Job
| # | تیکت | وضعیت |
|---|------|-------|
| T6 | `schemas.py` اولیه (MediaKind، JobStatus، JobSnapshot) | ✅ |
| T7 | `services/media.py`: `detect_kind` (تصویر/ویدیو/نامعتبر) | ✅ |
| T8 | `POST /api/analyze`: ذخیره‌ی فایل آپلودی (chunk‌دار + سقف حجم) | ✅ |
| T9 | `services/jobs.py`: `Job` و `JobStore` در حافظه | ✅ |
| T10 | `GET /api/jobs` ، `GET /api/jobs/{id}` ، `DELETE /api/jobs/{id}` | ✅ |
| T11 | `deps.py` + اجرای پس‌زمینه با pipeline **ساختگی** (sleep + progress) | ✅ |
| T12 | SSE: `GET /api/jobs/{id}/events` | ✅ |

### اسپرینت ۳ — OCR تصویر
| # | تیکت | وضعیت |
|---|------|-------|
| T13 | OCR کلاسیک با Tesseract (`vision.py`) | 🔶 |
| T14 | کلاینت `vlm.py` با httpx (اول با سرور Mock) | ⬜ |
| T15 | `prompts.py` + استخراج JSON از جواب مدل | ⬜ |
| T16 | `pipeline.py`: خط لوله‌ی تصویر (Tesseract + VLM) | ⬜ |

### اسپرینت‌های بعد (وقتی رسیدیم ریز می‌شوند)
۴) ویدیو: ffprobe/ffmpeg، فریم‌ها، faster-whisper · ۵) YOLO و InsightFace · ۶) گزارش + `StaticFiles` + چت استریم · ۷) pytest، Dockerfile، README

---

## ۴. تیکت فعلی

### ✅ اسپرینت ۲ بسته شد — بعدی: اسپرینت ۳ (سشن «اسپرینت ۳ — OCR تصویر»)
**وضعیت کد در پایان اسپرینت ۲:**
- `app/services/jobs.py`: `Job` (`id`، `kind`، `filename`، `status`، `progress`، `message`، `created_at`، `upload_path`، `events`، `_subscribers`) با متدهای `publish(type, **data)`، `set_progress(value, message)` (clamp ۰..۱)، `finish(message)`، `fail(error)`، async generator `subscribe()` (اول کپی تاریخچه، بعد صف زنده، پایان روی `done`/`error`، `finally` ← discard)، `snapshot()`. `JobStore`: `create`، `get`، `list_jobs` (جدیدترین اول)، `delete -> bool`.
- `app/deps.py`: `Container` با `jobs` و `tasks: set` و `spawn(coro)`؛ `container = Container()`.
- `app/services/pipeline.py`: `fake_pipeline(job)` — ۵ مرحله × `asyncio.sleep(4)` با `set_progress`، بعد `finish()`؛ کل بدنه در `try` و `except Exception` ← `log.exception` + `fail(...)`. **این همان جایی است که اسپرینت ۳ تحلیل واقعی را می‌گذارد.**
- `app/routers/analyze.py`: `POST /api/analyze` (detect_kind ← 400، ذخیره‌ی chunk‌دار در `upload_dir/{job.id}{suffix}`، سقف ← 413 با پاک کردن فایل و Job، `container.spawn(fake_pipeline(job))`، `response_model=JobSnapshot`)، `GET /api/jobs`، `GET /api/jobs/{id}`، `DELETE /api/jobs/{id}` (فایل را هم پاک می‌کند)، `GET /api/jobs/{id}/events` (SSE با `StreamingResponse`).

**ریزه‌کاری‌ها / بدهی فنی برای اسپرینت‌های بعد:**
- `CORS_ORIGINS` در `.env.example`.
- آپلود: `except Exception` ← 500 و `finally: await file.close()`.
- `Container.shutdown()` در lifespan همراه `vlm.aclose()` (اسپرینت ۳).
- Jobها فقط در RAM ← با ری‌استارت گم می‌شوند و فایل‌ها یتیم می‌مانند (بازیابی از `report.json` در اسپرینت ۶).
- SSE: هدرهای `Cache-Control: no-cache` و `X-Accel-Buffering: no` (اسپرینت ۷، پشت پراکسی).
- `progress` در `JobSnapshot` با `Field(ge=0, le=1)`؛ از `set_progress` استفاده شود، نه مقداردهی مستقیم.

---

## ۵. گزارش جلسه‌ها

### جلسه‌ی ۱ — 2026-09-30 (خونه)
- کارفرما پروژه‌ی مرجع و ریپو را بررسی کرد. محیط شرکت: پایتون 3.12.10 (از `pyvenv.cfg` در commit اول). خونه: پایتون 3.14.5 — بررسی PyPI نشان داد همه‌ی کتابخانه‌های پروژه برای ۳.۱۴ ویندوز wheel دارند، پس با ۳.۱۴ ادامه می‌دهیم.
- T1 ✅: `.venv` ساخته شد، پکیج‌ها نصب شدند (fastapi 0.142.2؛ شرکت 0.141.1 بود ← به‌خاطر `>=`). `.env` ساخته شد.
- مفاهیم مرور‌شده: venv و PATH/activate، `>=` در برابر `==` و `pip freeze`، commit جدا برای `style`.
- سبک کار عوض شد: تیکت کوتاه و عملی، بدون جزئیات ریز.
- بعدی: پیش‌کار commit ها ← T2.
- T2 قدم ۱ تا ۵ ✅: `data_dir`، `upload_dir`/`output_dir` با `@property`، `build()` با `mkdir(parents, exist_ok)`، صدا زدن در `main.py`، `/data` در `.gitignore`. مفاهیم: `.env` بر پیش‌فرض اولویت دارد و pydantic نوع را تبدیل می‌کند؛ `Path` فقط آدرس است؛ git پوشه‌ی خالی را نمی‌بیند.
- commit ها: `30ddf43` · `7a28085` · `ecbe41d`. نکته‌ی review: پیام‌ها دقیق‌تر شوند (مثلاً `chore: ignore data directory`). push شد.

- T2 قدم ۶ تا ۸ ✅: `max_upload_mb` (مفهوم Fail Fast با `MAX_UPLOAD_MB=abc`)، `extra="ignore"` (فرق «متغیر ناشناخته» با «مقدار غلط»)، `.env.example`. commit ها `d45d87e` (پیام تکراری کپی شده بود — دقت شود) و `8ca95a0`.

- T3 ✅: لاگینگ. مفاهیم: سطوح لاگ (DEBUG<INFO<WARNING<ERROR)، `%s` به‌جای f-string در لاگ، `__name__`، خطای `'NoneType' object has no attribute` (زنجیره کردن روی تابعی که None برمی‌گرداند). commit ها تمیز و جدا. سؤال جانبی «.env در برابر پیش‌فرض کد» به سشن جدا رفت.

- T4 ✅: `/api/config` و refactor به `public_snapshot()`. مفاهیم: prefix روتر، refactor، تابع بدون return ← `null`. `INTERNSHIP.md` اشتباهی در commit `27fdfba` رفت (فایل‌ها را جدا add کن). سؤال‌های git به سشن جدا رفت.

- T5 ✅: lifespan (درس: مشخصات اپ مثل title بیرون، کارهای «موقع روشن شدن» داخل lifespan؛ refactor را با تست قبلی چک کن) و CORS (`cors_origin_list`، `CORSMiddleware`؛ درس: CORS را مرورگر اعمال می‌کند، سرور همچنان جواب می‌دهد — امنیت/احراز هویت نیست). commit ها `10f99da`، `4931b16`.
- قرار جدید: موقع commit، کارفرما فقط متن پیام commit را می‌دهد؛ خود کارآموز commit می‌کند.


### جلسه‌ی ۲ — 2026-10-02 (خونه)
- T5 بسته شد (commit `ab533b3`). سشن قبلی خیلی بزرگ شد؛ ادامه در سشن جدید از «کار عقب‌افتاده» و بعد T6 قدم ۱.
- سشن «اسپرینت ۲ — آپلود فایل و مدیریت Job» شروع شد. CORS fix ✅ (`8bc722e`)؛ دو کامنت lifespan مانده. `schemas.py` هنوز ساخته نشده (قدم ۱ T6 دوباره یادآوری شد).
- T6 قدم ۱: `schemas.py` ساخته شد ولی کارآموز `JobStatus` را به `processing/finished/failed` عوض کرده بود ← تست دوم ValidationError نداد. درس: قرارداد API را خودسرانه عوض نکن (فرانت روی همین مقادیر کار می‌کند). خواسته شد به `queued/running/done/error` برگردد؛ هنوز commit نشده. نکته: خطای `UnicodeEncodeError` در کنسول ویندوز مال cp1252 است نه کد ← `PYTHONIOENCODING=utf-8`.
- T6 قدم ۱ ✅ (`0fb33e4`) با `JobStatus` اصلاح‌شده. پیام commit به‌صورت کل دستور `git commit -m "..."` ثبت شد ← درس: فقط متن داخل code block را به‌عنوان پیام بزن. خط خالی زیر `def lifespan` هنوز مانده. قدم ۲ (`Field(ge=0, le=1)`) داده شد.
- T6 قدم ۲ ✅ (`8677c3d`، پیام commit این بار درست). مفهوم: `Field(ge, le)` = قانون داده در خود قرارداد. قدم ۳ (`created_at` با `default_factory`) داده شد.
- T6 قدم ۳ ✅ (`91b4d7b`). مفهوم: `default_factory` (برای هر نمونه صدا زده می‌شود) در برابر `default=time.time()` (یک بار موقع import). جواب سؤال را کارآموز نداد — در قدم ۴ دوباره کوتاه توضیح داده شد. قدم ۴ (پیش‌فرض‌ها) داده شد.
- T6 قدم ۴ ✅ (`7c025b4`) ← **T6 بسته شد.** `try_schemas.py` به‌جای پاک شدن به ریشه منتقل شد. T7 قدم ۱ (پوشه‌ی services و set پسوندها) داده شد.
- T7 قدم ۱ ✅ (set پسوندها؛ `__init__.py` جا افتاده بود). `try_schemas.py` پاک شد. قدم ۲ (`detect_kind` با پسوند) داده شد.
- T7 قدم ۲ ✅ (`detect_kind` با پسوند). قدم ۳ (`MediaError`) داده شد.
- T7 قدم ۳ ✅ (`33ba0e6`). مفهوم: تابع با `-> MediaKind` نباید `None` برگرداند؛ حالت نامعتبر = raise با کلاس خطای مخصوص (بعداً در روتر ← 400). قدم ۴ (fallback روی content_type) داده شد.
- T7 قدم ۴: fallback درست، ولی رگرسیون (`MediaError` ← `ValueError`) در `58ee021`. درس: فقط چیزی را عوض کن که قدم خواسته؛ و تست‌های قدم قبل را دوباره اجرا کن (regression).
- رگرسیون fix شد (`794f6c6`) ← **T7 بسته شد.** پیام commit مبهم بود (درس: پیام بگوید چه چیزی درست شد). T8 قدم ۱ (اسکلت روتر آپلود) داده شد.

### جلسه‌ی ۳ — 2026-10-03 (شرکت)
- همگام‌سازی: کد شرکت روی `794f6c6` بود (درست)، ولی `INTERNSHIP.md` داخل ریپو نسخه‌ی قدیمی (وسط T4) بود؛ نسخه‌ی آخر خونه commit نشده بود ← از روی نسخه‌ی خونه جایگزین شد و مسیرهای شرکت به بخش ۰ اضافه شد. درس: آخر جلسه `INTERNSHIP.md` را هم commit و push کن.
- venv شرکت سالم است (پایتون 3.12.10، fastapi 0.141.1، pydantic-settings 2.15.0)؛ `python-multipart` نصب نیست (برای T8 قدم ۱ عمداً).
- ریزه‌کاری‌ها هنوز باز: پیام خطای `detect_kind` · خط خالی زیر `async def lifespan` · `CORS_ORIGINS` در `.env.example`. اول fix پیام خطا داده شد، بعد T8 قدم ۱.
- برای اسپرینت‌های ۳ تا ۷ سشن‌های جدا ساخته شد (گروه سایدبار «کارآموزی بک‌اند OCR»)؛ هر کدام اول چک می‌کند اسپرینت قبلی بسته شده باشد.
- fix پیام خطای `detect_kind` ✅ (`00a1ee4`؛ ۷ حالت رگرسیون تست شد). T8 قدم ۱ دوباره داده شد.
- T8 قدم ۱ ✅ (آپلود از `/docs` و تست با uvicorn.Server: `{"filename","content_type"}` برمی‌گردد). کارآموز `python-multipart` را نصب کرد ولی به `requirements.txt` اضافه نکرد ← درس: «روی سیستم من کار می‌کند»؛ وابستگی‌ای که در requirements نیست در خانه/Docker می‌شکند. مفهوم: آپلود فایل = بدنه‌ی `multipart/form-data` نه JSON؛ FastAPI پارسش را به `python-multipart` می‌سپارد که وابستگی اختیاری است. ریزه: `health , analyze` ← `health, analyze`. قدم ۲ (`detect_kind` + `HTTPException(400)`) داده شد.
- T8 قدم ۲ ✅ (تست: jpg ← 200 image، pdf ← 400، بدون پسوند + video/mp4 ← 200 video). ولی کارهای قدم ۱ (requirements، فاصله، commit ها) انجام نشده بود و دو قدم روی هم commit‌نشده ماندند ← درس: هر قدم را قبل از قدم بعد commit کن. مفهوم: لایه‌بندی خطا (service خطای دامنه می‌دهد، router آن را به HTTP ترجمه می‌کند). قدم ۳ تا انجام کارهای مانده نگه داشته شد.
- کارهای مانده ✅: دو commit جدا و تمیز (`09714c7`، `dc4cac8`). فقط فاصله‌ی import روی دیسک اصلاح نشده بود. قدم ۳الف (id و مسیر ذخیره) داده شد.
- T8 قدم ۳الف ✅ (`1df74c8`، `486c015`). مفاهیم: نام فایل ورودی کاربر است ← Path Traversal؛ گروه‌بندی importها طبق PEP 8. قدم ۳ب (ذخیره‌ی chunk‌دار) داده شد.
- T8 قدم ۳ب ✅. مفهوم: خواندن تیکه‌ای ← مصرف RAM ثابت (~۱MB) مستقل از حجم فایل. قدم ۴الف (سقف حجم ← 413) داده شد.
- T8 قدم ۴الف ✅. کارآموز خودش دید فایل نیمه‌کاره‌ی ویدیو در `data/uploads` می‌ماند. مفهوم: `open("wb")` فایل را همان اول می‌سازد و `with` فقط می‌بندد، پاک نمی‌کند ← فایل یتیم (orphan) دیسک را پر می‌کند. قدم ۴ب (پاک‌سازی) داده شد.
- T8 قدم ۴ب ✅. مفهوم: `raise` خالی همان خطا را دوباره پرتاب می‌کند (تمیزکاری وسط راه). قدم ۵ (`response_model=JobSnapshot`) داده شد.
- T8 قدم ۵ ✅ ← **T8 بسته شد.** کارآموز درست گفت `status`/`progress`/`created_at` از پیش‌فرض‌های T6 می‌آیند. مفهوم: `response_model` = قرارداد خروجی (اعتبارسنجی + مستندات + جلوگیری از لو رفتن فیلدهای داخلی مثل مسیر فایل). ریزه‌ها: import `app.schemas` در گروه `app` و ترتیب الفبایی، خط خالی داخل `if not chunk:`. commit: `feat: return job snapshot from upload endpoint`. T9 قدم ۱ (کلاس `Job`) داده شد.
- T9 قدم ۱ ✅ (کد دقیق). مفهوم: `Job` شیء زنده و تغییرپذیر روی سرور، `JobSnapshot` عکس لحظه‌ای برای API؛ هر نمونه id و created_at خودش را دارد. قدم ۲ (`snapshot()`) داده شد.
- T9 قدم ۲ ✅. مفهوم: کلاس معمولی پایتون هیچ اعتبارسنجی ندارد؛ pydantic در «مرز» (لحظه‌ی ساخت snapshot) چک می‌کند ← خطا دیر و دور از محل باگ ظاهر می‌شود؛ بعداً متد `progress()` با clamp. باز هم قدم قبلی commit نشده بود. قدم ۳ (`JobStore`) داده شد.
- T9 قدم ۳ ✅. کارآموز درست گفت چرا `get` باید خود شیء را برگرداند (تغییر progress توسط تحلیل‌گر باید برای خواننده دیده شود). قرار جدید (قانون ۱۲): ریزه‌کاری‌های ظاهری در review گفته نمی‌شوند. قدم ۴ (`list_jobs` و `delete`) داده شد.
- T9 قدم ۴ ✅. مفهوم: dict ترتیب درج را نگه می‌دارد (`reversed` ← جدیدترین اول)؛ `bool` از `delete` برای 404 در روتر. قدم ۵ (اتصال JobStore به آپلود) داده شد.
- T9 قدم ۵ ✅ ← **T9 بسته شد.** تست کارفرما با سقف ۱MB: آپلود کوچک ← Job در store و فایل روی دیسک؛ 413 ← نه Job ماند نه فایل. مفهوم: refactor = ساختار داخلی عوض شود، رفتار بیرونی نه. commit: `feat: register uploaded files as jobs`. T10 قدم ۱ (`GET /jobs/{id}`) داده شد.

### جلسه‌ی ۴ — 2026-10-05 (شرکت)
- T9 commit شد (`971c28a`). T10 قدم ۱ ✅: 200 / 404 / بعد از ری‌استارت 404. کارآموز درست گفت: Jobها در RAM هستند و فایل روی دیسک ← با ری‌استارت Job گم می‌شود ولی فایل یتیم می‌ماند (راه‌حل مرجع: بازیابی از `report.json` موقع استارت، اسپرینت ۶). commit: `feat: add get job endpoint`. قدم ۲ (`GET /jobs`) داده شد.
- T10 قدم ۲ ✅ (تست کارفرما: `['b.jpg','a.jpg']`). commit: `feat: add list jobs endpoint`. قدم ۳ (`DELETE /jobs/{id}` + `upload_path` روی Job) داده شد.
- T10 قدم ۳ ✅ ← **T10 بسته شد.** commit: `feat: add delete job endpoint`. T11 قدم ۱ (`deps.py` و `Container`) داده شد.
- T11 قدم ۱ ✅ (refactor تمیز؛ ۶ جا `container.jobs`). مفهوم: یک نسخه‌ی مشترک از اشیای سراسری (singleton) ← در غیر این صورت چند store جدا. commit: `refactor: move job store into dependency container`. قدم ۲ (`fake_pipeline`) داده شد.
- T11 قدم ۲ ✅ (تست کارفرما: `done`، `progress=1.0`). commit: `feat: add fake analysis pipeline`. قدم ۳ (`container.spawn`) داده شد.
- T11 قدم ۳ ✅. اول `scratch_spawn.py` داخل `app/` ساخته شد ← `No module named 'app'` (پایتون پوشه‌ی خود اسکریپت را در sys.path می‌گذارد، نه cwd) ← به ریشه منتقل شد و کار کرد (`queued 0.0 1` ← `running 0.4 1` ← `done 1.0 0`). جواب سؤال‌ها نیامد؛ کارفرما توضیح داد. commit: `feat: run background tasks from container`. قدم ۴ (spawn در آپلود) داده شد.
- T11 قدم ۴ ✅: آپلود فوراً `queued`، بعد `running` با progress رو به بالا، بعد `done`؛ `/api/health` وسط کار فوراً جواب داد. ۵ ثانیه برای تست دستی کم بود ← `asyncio.sleep(4)` (۲۰ ثانیه). commit ها: `feat: start background analysis after upload` و `chore: slow down fake pipeline for manual testing`. قدم ۴ب (آزمایش `time.sleep`) داده شد.
- T11 قدم ۴ب: کارآموز گفت health فوراً جواب داد (فایل روی دیسک `asyncio.sleep` بود؛ احتمالاً تغییر اعمال نشده یا health بعد از برگشتن آپلود زده شده). کارفرما آزمایش را با pipeline بلاک‌کننده‌ی ۵ ثانیه‌ای اجرا کرد: خود آپلود ۵.۱ ثانیه طول کشید و health که در ثانیه‌ی ۱ فرستاده شده بود ۴.۱ ثانیه منتظر ماند. مفهوم: یک event loop؛ `await` نوبت را پس می‌دهد، `time.sleep` کل سرور را قفل می‌کند ← کار سنگین CPU بعداً با `asyncio.to_thread`. قدم ۵ (خطا در pipeline) داده شد.

### جلسه‌ی ۵ — 2026-10-06 (شرکت)
- T11 قدم ۵: تغییرات آزمایش اول روی دیسک نیامده بود (ذخیره نشده) ← کارفرما آزمایش raise را خودش اجرا کرد: Job برای همیشه `running 0.6` و «Task exception was never retrieved». کارآموز پرسید چرا اینجا و الان ← توضیح: کار پس‌زمینه هیچ لایه‌ای بالای سرش نیست که خطا را بگیرد؛ اسکلت برای pipeline واقعی؛ `except Exception` فقط در بالاترین سطح کار پس‌زمینه. ترفند: `git diff` قبل از تست. commit `0e4a1d6` ✅ ← **T11 بسته شد** (shutdown به اسپرینت ۳ منتقل شد). T12 قدم ۱ (`events` و `publish`) داده شد.
- T12 قدم ۱ ✅ (خروجی درست: دو رویداد با `type` و `ts`). commit: `feat: add event log to job`. قدم ۲ (`set_progress` با clamp + رویداد) داده شد. `finish()` و `fail()` به قدم ۳ رفتند.
- T12 قدم ۲ ✅ (`set_progress(2)` ← 1.0، `set_progress(-1)` ← 0.0، pipeline ← `done 5`). commit: `feat: publish progress events from job`. قدم ۳ (`finish`/`fail`) داده شد.
- T12 قدم ۳ ✅ (`fail` ← `error` و رویداد آخر؛ pipeline ← `done 6 done` = ۵ progress + ۱ done). commit: `feat: publish done and error events`. قدم ۴الف (مشترک شدن با `asyncio.Queue`، فقط زنده) داده شد.
- T12 قدم ۴الف ✅: رویدادها یکی‌یکی (هر ۴ ثانیه) چاپ شدند و برنامه با `done` خودش تمام شد. commit: `feat: let clients subscribe to job events`. قدم ۴ب (تاریخچه برای مشترک دیررس) داده شد.

### جلسه‌ی ۶ — 2026-10-07 (شرکت)
- T12 قدم ۴ب ✅ (کد `subscribe` با replay تاریخچه درست؛ `scratch_sub.py` پاک شد). commit: `feat: replay past events to late subscribers`. قدم ۵ (endpoint SSE) داده شد.
- T12 قدم ۵ ✅ با `curl.exe -N`: وسط تحلیل رویدادها یکی‌یکی؛ بعد از done همه یک‌جا و اتصال بسته (replay تاریخچه)؛ id ساختگی ← 404. commit: `feat: stream job events over SSE` ← **T12 و اسپرینت ۲ بسته شدند.** ادامه در سشن «اسپرینت ۳ — OCR تصویر».

---

## ۶. محیط و نسخه‌ها
- **شرکت:** پایتون 3.12.10 · fastapi 0.141.1 · starlette 1.7.0 · uvicorn 0.54.0 · pydantic 2.13.5
- **خونه:** پایتون 3.14.5 · fastapi 0.142.2 · pydantic-settings 2.15.0 (بقیه مشابه)
- کد باید روی هر دو اجرا شود (از امکانات مخصوص ۳.۱۳/۳.۱۴ استفاده نشود).
- پروژه‌ی مرجع در Dockerfile از `python:3.11` استفاده می‌کند.

## ۷. روش کار
- **اجرا** (ریشه‌ی پروژه، venv فعال): `uvicorn app.main:app --reload` ← `http://127.0.0.1:8000/docs`
- **commit:** هر commit یک نوع کار: `feat:` ، `fix:` ، `style:` ، `docs:` ، `refactor:` ، `test:` ، `chore:`
- **خونه ↔ شرکت:** `git push` / `git pull`. `.venv` و `.env` منتقل نمی‌شوند: `python -m venv .venv` ← `pip install -r requirements.txt` ← `.env` از روی `.env.example`.
- **گیر کردی:** متن کامل خطا + چه کردی + چه انتظار داشتی.
