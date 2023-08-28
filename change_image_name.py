import os

file_path = "images_labels/handsome_ugly_faces/"
file_names = os.listdir(file_path)

i = 1
for f in file_names:
    src = os.path.join(file_path, f)
    dst = 'face_'+str(i)+'.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

