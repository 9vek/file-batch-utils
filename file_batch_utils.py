import fnmatch
import os


def files_name_replace(root, find, replace, suffix="*"):
    """
    �������ļ��������滻
    :param root: ��Ŀ¼����������ļ���
    :param find: ��������
    :param replace: �滻Ϊ
    :param suffix: �ļ����ˣ����ӣ�*.txt, *.json, *
    """
    counter = 0
    for path, sub_dirs, files in os.walk(root):
        for file_name in fnmatch.filter(files, suffix):
            if find in file_name:
                file_path = os.path.join(path, file_name)
                new_name = os.path.join(path, file_name.replace(find, replace))
                if file_path != new_name:
                    os.rename(file_path, new_name)
                    counter += 1
                    print(f"�޸��ļ���{file_path} -> {new_name}")

    print(f'�����ѽ����� �ܹ��޸��� {counter} ���ļ���')


def files_content_replace(root, find, replace, suffix="*"):
    """
    �������ļ����ݲ����滻
    :param root: ��Ŀ¼����������ļ���
    :param find: ��������
    :param replace: �滻Ϊ
    :param suffix: �ļ����ˣ����ӣ�*.txt, *.json *
    """
    find_counter = 0
    file_counter = 0
    for path, sub_dirs, files in os.walk(root):
        for file_name in fnmatch.filter(files, suffix):
            file_path = os.path.join(path, file_name)
            with open(file_path) as file:
                content = file.read()
            temp_counter = content.count(replace)
            if temp_counter > 0:
                content = content.replace(find, replace)
                with open(file_path, "w") as file:
                    file.write(content)
                find_counter += temp_counter
                file_counter += 1
                print(f'�� {file_path} ���޸��� {temp_counter} ��')

    print(f'�����ѽ����� �ܹ��� {file_counter} ���ļ����޸��� {find_counter} ��')


if __name__ == '__main__':
    files_name_replace(".\\", "wool", "wool")
    files_content_replace(".\\", "wool", "wool")
