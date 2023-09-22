# Removebgpython
شرح لكيفية استخدام الكود الذي قدمته لإزالة الخلفية من صور PNG باستخدام Python:

الخطوة 1: تحضير البيئة

قبل أن تستخدم هذا الكود، تأكد من أن لديك Python مثبتًا على جهاز الكمبيوتر الخاص بك. يمكنك تثبيت Python من موقع الويب الرسمي للغة Python (https://www.python.org/).

بعد تثبيت Python، يجب عليك تثبيت المكتبة المطلوبة rembg باستخدام مدير الحزم pip. يمكنك القيام بذلك باستخدام الأمر التالي في سطر الأوامر:

Copy code
pip install rembg
الخطوة 2: تنفيذ الكود

بمجرد أن تكون قد أعددت البيئة، يمكنك تنفيذ الكود لإزالة الخلفية من صور PNG.

قم بفتح محرر النص المفضل لديك (مثل VS Code أو PyCharm) وقم بإنشاء ملف Python جديد. ثم، قم بنسخ الكود الذي قدمته في الملف.

الخطوة 3: تعديل المتغيرات

قبل تشغيل البرنامج، تحتاج إلى تعديل المتغيرات input_path و output_dir لتناسب موقع ومجلد الصور الخاصة بك. قم بتحديد المجلد الذي تحتوي فيه الصور التي تريد إزالة خلفيتها كمسار الإدخال input_path. ثم، قم بتحديد المجلد الذي تريد حفظ الصور الناتجة فيه كمسار الإخراج output_dir.

الخطوة 4: تشغيل الكود

الآن يمكنك تشغيل الكود. افتح سطر الأوامر أو الموجه في مجلد البرنامج الذي يحتوي على الكود واستخدم الأمر التالي:

Copy code
python اسم_الملف.py مسار_الإدخال مسار_الإخراج
حيث اسم_الملف.py هو اسم ملف البرنامج الذي أنشأته و مسار_الإدخال هو المسار إلى مجلد الصور الذي تريد معالجته و مسار_الإخراج هو المسار الذي تريد حفظ الصور المعالجة فيه.




Step 1: Environment Setup

Before using this code, make sure you have Python installed on your computer. You can install Python from the official Python website (https://www.python.org/).

Once Python is installed, you need to install the required library, rembg, using the pip package manager. You can do this by running the following command in your command prompt or terminal:

Copy code
pip install rembg
Step 2: Running the Code

Once you've set up the environment, you can run the code to remove backgrounds from PNG images.

Open your preferred text editor (e.g., VS Code or PyCharm) and create a new Python file. Then, copy the code provided into the file.

Modify the variables before running the program. You need to specify the input_path and output_dir to match the location of your images. Set the input_path to the folder containing the images you want to remove backgrounds from. Then, set the output_dir to the folder where you want to save the resulting images.

Step 3: Executing the Code

Now, you can execute the code. Open your command prompt or terminal in the directory where your code file is located and use the following command:

Copy code
python filename.py input_path output_dir
Replace filename.py with the name of your Python file, input_path with the path to the folder containing your images, and output_dir with the path where you want to save the processed images.

Step 4: Completion

After running the program, the backgrounds of your images will be removed, and the resulting images will be saved in the output directory you specified. You will see a message confirming the completion of the background removal process, along with the location where the images have been saved.
