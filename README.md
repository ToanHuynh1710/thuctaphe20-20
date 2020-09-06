Nhận diện gương mặt


cài đặt các thư viện cần thiết
pip install -r requirements.txt

cd src
lấy dữ liệu hình ảnh 

python detect_camera.py --cascade models/haarcascade_frontalface_default.xml --output facedata/raw


detect khuôn mặt từ hình ảnh(thư mục raw là hình ảnh gốc và thư mục processed là nơi chứa ảnh sau khi detect)

python align_dataset_mtcnn.py  facedata/raw facedata/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25


train model

python src/classifier.py TRAIN facedata/processed models/20180402-114759.pb models/new_model.pkl --batch_size 1000

nhận diện gương mặt bằng camera

python face_rec_cam_v1.py