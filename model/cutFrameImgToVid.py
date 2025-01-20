import cv2
import os

# Đường dẫn tới file MP4
video_path = r"E:\HK5\NCKH\NCKH_AI_Vision\data\video\6244937727337.mp4"
output_folder = r"E:\HK5\NCKH\NCKH_AI_Vision\data\img"

# Tạo thư mục lưu ảnh nếu chưa có
os.makedirs(output_folder, exist_ok=True)

# Đọc video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Không thể mở video. Kiểm tra đường dẫn hoặc file video.")
    exit()

# Số frame cần trích xuất mỗi giây
frames_per_second = 1

# Lấy FPS gốc của video
video_fps = cap.get(cv2.CAP_PROP_FPS)
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    print("Không thể đọc FPS từ video. Kiểm tra codec hoặc file video.")
    exit()

# Tính khoảng cách giữa các frame cần lưu
frame_interval = int(video_fps / frames_per_second)

# Bắt đầu đếm frame từ số frane trích xuất đc từ vid trctrc
frame_count = 874
frame_index = 0  # Frame hiện tại trong video

while True:
    ret, frame = cap.read()
    if not ret:  
        break
    
    # Kiểm tra nếu frame hiện tại nằm trong khoảng cần lưu
    if frame_index % frame_interval == 0:
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    frame_index += 1

cap.release()
print(f"Trích xuất xong {frame_count - 874} frame từ video")
print(f"Mỗi frame được trích xuất tương ứng với {frame_interval} theo fps gốc")
