import os
import shutil

os.chdir('data')


for file in os.listdir('.'):
     filename = os.fsdecode(file)
     if filename.endswith(("png",'img','jpg')):
        if not os.path.exists('images'):
            os.mkdir('images')

        shutil.copy(filename, 'images')
        os.remove(filename)


     elif filename.endswith(("mp4",'vido')):
        if not os.path.exists('moveis'):
            os.mkdir('moveis')

        shutil.copy(filename, 'moveis')
        os.remove(filename)

     elif filename.endswith((".pdf",'.word','.pptx')):
        if not os.path.exists('docs'):
            os.mkdir('docs')

        shutil.copy(filename, 'docs')
        os.remove(filename)


print('done')
