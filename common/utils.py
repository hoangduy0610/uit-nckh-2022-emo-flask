from datetime import datetime

def generate_random_image_path():
    current_time = datetime.now()
    file_name = current_time.strftime("IMG_%Y-%m-%d_%H-%M-%S.jpg")
    return 'uploads/faces/' + file_name