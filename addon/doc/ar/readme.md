# instantTranslate #
[[!meta title="instantTranslate"]]

* مطورو الإضافة: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto
  Buffolino وآخرون.
* تحميل [الإصدار النهائي][1]
* تحميل [الإصدار التجريبي][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## إعداد اللغات ##
لإعداد لغة المصدر, ولغة الهدف, أو في حالة التبديل بين لغة المصدر ولغة الهدف, اذهب إلى: قائمة NVDA الرئيسية>> التفضيلات>> إعدادات instant translate.

يوجد بالإضافة اثنان من صناديق الخيارات الأول يسمى "لغة المصدر" والثاني يسمى
"لغة الهدف", ومربع تحديد لتقرير ما إذا كان يجب على الإضافة نسخ الترجمة
للحافظة.

فضلا عن ذلك, إذا قمت باختيار الخيار التلقائي (أول اختيار) من صندوق الخيارات
الأول المسمى ب"لغة المصدر", فإنه يوجد أيضا صندوق خيارات آخر يسمى "لغة
التبديل" ومربع تحديد عن التبديل التلقائي بين اللغات.

إن معنى كل من صندوق الخيارات الأول والثاني ومربع التحديد الخاص بنسخ الترجمة
للحافظة واضح, لكن من الضروري شرح باقي صناديق الخيارات ومربعات التحديد
الأخرى. تذكر دائما أن الشرح المكتوب أدناه يعتبر بأن لغة المصدر قد تم ضبطها
لتكون هي الخيار التلقائي.

يعتبر صندوق الخيارات "لغة التبديل" مفيد عندما تبدل بين لغتي المصدر والهدف
عبر مفتاح اختصار (انظر أدناه)، في الحقيقة, إن ضبط لغة الهدف لتكون الخيار
التلقائي ليس له معنى, لذا فإن الإضافة تقوم بضبط قيمتها لتكون نفس قيمة اللغة
الموجودة بصندوق الخيارات الأول وهو لغة المصدر.

هب أنك تترجم عادة إلى اللغة الإنجليزية (لغتك الرئيسية),لكنك في بعض الأحيان
(على سبيل المثال, عند كتابة مستند) تحتاج للترجمة إلى الإيطالية (لغتك
الثانية), فرضا)، فإنه يمكنك ضبط صندوق الخيارات "لغة التبديل" للإيطالية, لذا
فإنك ستترجم من الإنجليزية للإيطالية دون الحاجة إلى الذهاب لإعدادات
الإضافة. من الواضح إن هذه الخاصية "لغة التبديل" تقل أهميتها أو تعظم وفقا
لحاجاتك الدائمة.

الآن, أصبح مربع تحديد لغة التبديل يظهر إذا وفقط إذا قمت باختيار الخيار
التلقائي من صندوق الخيارات "لغة المصدر", وأصبح يتصل مباشرة بصندوق الخيارات
"لغة التبديل". إذا قمت بتحديد المربع, فستقوم الإضافة تلقائيا بالتبديل من
إعدادات لغة المصدر ولغة الهدف لإعداد آخر تكون فيه لغة الهدف هي لغة المصدر
واللغة المختارة في صندوق خيارات "لغة التبديل" هي لغة الهدف الجديدة، يفيد جدا
عندما تكون لغة المصدر للنص الذي تريد ترجمته هي لغة الهدف.

مثال بسيط: بالنظر للمثال المشروحسابقا, إذا كنت تترجم نص بلغة أخرى غير
الإنجليزية, فليست هناك مشكلة, حيث ستحصل على الترجمة الصحيحة بالإنجليزية. لكن
إذا أردت ترجمة نص من اللغة الإنجليزية, فإنه من الطبيعي أن تحصل على ترجمة
للإنجليزية مطابقة للنص الأصلي, وهذا ليس له جدوى. فشكرا لوظيفة لغة التبديل,
ومع ذلك, هب أنك تريد أن تعرف كيف كيف يبدو النص بالإيطالية, ففي هذه الحالة
ستقوم الإضافة آليا بتبديل لغة الهدف للإيطالية, لذا فستحصل على ترجمة صحيحة
ذات معنى.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## الاستخدام ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. كما يمكنك ترجمة النص المخزن بالحافظة.
3. Press the dedicated shortcut key to translate the last spoken text.

## مفاتيح الاختصار ##
يجب ضغط كافة الاختصارات التالية بعد ضغط مفتاح الإضافة "NVDA+Shift+t":

* T: ترجمة النص المظلل,
* Shift+t: ترجمة النص من الحافظة,
* S: تبديل بين لغتي المصدر والهدف,
* a: الإعلان عن الإعداد الحالي,
* S: نسخ آخر نتيجة للحافظة,
* I: التعرف على لغة النص المظلل,
* L: translate the last spoken text,
* O: open translation settings dialog
* H: announces all available layered commands.

## Changes for 4.4.3 ##
* Added the ability to replace underscores with spaces, may provide better
  translation results depending on context (thanks to Beka Gozalishvili)
* Added compatibility for NVDA 2022.1

## Changes for 4.4.2 ##
* Restore language detection and auto-swapping (Thanks to Cyrille for fix)
* updated languages for translation (thanks to Cyrille)

## Changes for 4.4 ##
* Instant translate is now compatible with NVDA 2019.3 (Python 3 versions of
  NVDA)

## Changes for 4.3 ##
* nvda compatibility fix Now instant translate will be compatible with
  latest nvda builds.
* found a way to use google as a translation service again.

## Changes for 4.2 ##
* Restored working state with newer versions of nvda.
* Restored automatic language detection.

## Changes for 4.1 ##
* InstantTranslate is working again, now with Yandex translator service
  instead of Google.

## Changes for 4.0 ##
* Translation is automatically performed after swapping.
* Cache bug fixed.

## مستجدات الإصدار 3.0 ##
* تغيير كيفية استخدام مفاتيح الاختصار, الآن يمكنك ضغط مفتاح الإضافة
  "NVDA+Shift+t", ثم الضغط على الأحرف المنفردها لأداء المهام المطلوبة (انظر
  إلى كافة أوامر الإضافة بقسم "مفاتيح الاختصار").
* تنفيذ التبديل بين اللغات
* تغيير تنسيق الإعدادات, الآن يمكننا تغيير إعدادات Instante translate إذا
  كنا في بيئة أو حقل للقراءة فقط ولكن عليك أن تتذكر أن تقوم بغلق وإعادة
  تشغيل NVDA أولا. 
* إزالة التقييد على حجم النص المراد ترجمته
* إضافة حرف الوصول السريع T إلى قائمة إعدادات instant translate
* الاختيار التلقائي أصبح موجودا الآن في الموضع الأول في صندوق خيار لغات
  المصدر ولم يعد موجودا في صندوق خيار لغات الهدف.
* إضافة مربع تحديد لإعداد نسخ نتائج الترجمة.
* تخزين ملف الإعدادات داخل مجلد الإعدادات.
* تتزامن لغات المصدر والهدف مع ما تعرضه خدمة الترجمة من قوقل حاليا (22 إبريل
  2015).


## مستجدات الإصدار 2.1 ##
* من الآن يمكن للإضافة ترجمة النص المخزن بحافظة الويندوز عن طريق الضغط على
  nvda+shift+y.

## مستجدات الإصدار 2.0 ##
* إضافة عنصر لواجهة المستخدم يمكن من خلاله تحديد لغة المصدر ولغة الهدف.
* إضافة عنصر قائمة للتحكم في إعدادات الإضافة بقائمة التفضيلات.
* من الآن سيتم كتابة الإعدادات في ملف منفصل.
* من الآن سيتم نسخ نتائج الترجمة إلى حافظة الويندوز للرجوع إليها وقت الحاجة.

## مستجدات الإصدار 2.0 ##
* إصدار أولي


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
