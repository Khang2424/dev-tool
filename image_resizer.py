# cài đặt thư viện PIL bằng lệnh pip install pillow
# Chương trình này sẽ tự động resize ảnh trong thư mục input và lưu vào thư mục output
from PIL import Image
import os

def resize_image(input_path, output_path, size=(640, 640)):
    """
    Resize an image to the specified size while maintaining aspect ratio.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path where the resized image will be saved
        size (tuple): Target size (width, height)
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert image to RGB if it's not
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate the aspect ratio
            aspect_ratio = img.width / img.height
            
            # Calculate new dimensions while maintaining aspect ratio
            if aspect_ratio > 1:
                # Image is wider than tall
                new_width = size[0]
                new_height = int(size[0] / aspect_ratio)
            else:
                # Image is taller than wide
                new_height = size[1]
                new_width = int(size[1] * aspect_ratio)
            
            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Create a new image with white background
            final_img = Image.new('RGB', size, (255, 255, 255))
            
            # Calculate position to paste the resized image
            paste_x = (size[0] - new_width) // 2
            paste_y = (size[1] - new_height) // 2
            
            # Paste the resized image onto the white background
            final_img.paste(resized_img, (paste_x, paste_y))
            
            # Save the result
            final_img.save(output_path, quality=95)
            print(f"Đã lưu ảnh: {output_path}")
            
    except Exception as e:
        print(f"Lỗi khi xử lý ảnh {input_path}: {str(e)}")

def process_directory(input_dir, output_dir):
    """
    Process all images in a directory.
    
    Args:
        input_dir (str): Input directory containing images
        output_dir (str): Output directory for resized images
    """
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"Lỗi: Thư mục input '{input_dir}' không tồn tại!")
        print("Vui lòng tạo thư mục và đặt ảnh vào đó.")
        return
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Đã tạo thư mục output: {output_dir}")
    
    # Get list of files in input directory
    try:
        files = os.listdir(input_dir)
        print(f"\nTìm thấy {len(files)} file trong thư mục input")
        print("\nDanh sách file trong thư mục input:")
        for file in files:
            print(f"- {file}")
    except Exception as e:
        print(f"Lỗi khi đọc thư mục input: {str(e)}")
        return
    
    # Supported image formats
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    
    # Counter for sequential numbering
    counter = 0
    
    # Process each file in the input directory
    for filename in files:
        if any(filename.lower().endswith(fmt) for fmt in supported_formats):
            input_path = os.path.join(input_dir, filename)
            # Get the file extension
            _, ext = os.path.splitext(filename)
            # Đổi tên file mới với định dạng namda_1, namda_2, ...
            new_filename = f"namda_{counter}{ext}"
            output_path = os.path.join(output_dir, new_filename)
            print(f"\nĐang xử lý ảnh: {filename}")
            resize_image(input_path, output_path)
            counter += 1
    
    if counter == 0:
        print("\nKhông tìm thấy ảnh nào trong thư mục input!")
        print("Các định dạng ảnh được hỗ trợ: .jpg, .jpeg, .png, .bmp, .gif")
    else:
        print(f"\nĐã xử lý thành công {counter} ảnh!")
        print(f"Ảnh đã xử lý được lưu trong thư mục: {output_dir}")

if __name__ == "__main__":
    # Đổi input và ouput ở đây
    input_directory = r"C:\Users\Admin\Desktop\Tai lieu cac mon hoc\Dai hoc\Lập trình python cho máy học\YOLO\anh-tho\Nam da\Namda"
    output_directory = r"C:\Users\Admin\Desktop\Tai lieu cac mon hoc\Dai hoc\Lập trình python cho máy học\YOLO\anh-tho\Nam da\Namda-640x640"
    
    # Process the images
    print(f"\nĐang xử lý ảnh từ: {input_directory}")
    print(f"Lưu ảnh đã xử lý vào: {output_directory}")
    process_directory(input_directory, output_directory)
    print("\nXử lý ảnh hoàn tất!") 