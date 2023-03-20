import os

folder_path = "/Users/jang-youngjoon/dev-projects/youtuber-look-alike/pre-processed-image/ijh"  # 파일이 있는 폴더 경로
prefix = "ijh_"  # 새로운 파일 이름의 prefix
padding_width = 6  # 숫자 자릿수 (예: 3이면 001, 002, ...)
extension = ".jpg"  # 파일 확장자

# 폴더 내 파일 목록 가져오기
file_list = os.listdir(folder_path)

# 파일 이름 변경
for i, file_name in enumerate(sorted(file_list)):
    # 파일 이름 생성
    new_file_name = prefix + str(i + 1).zfill(padding_width) + extension

    # 파일 이름 변경
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
    
    # 변경된 파일 이름 출력
    print("Renamed '{}' to '{}'".format(file_name, new_file_name))