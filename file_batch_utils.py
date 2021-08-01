import shutil
import fnmatch
import os


def files_name_replace(root, find, replace, pattern="*"):
    """
    �������ļ��������滻
    :param root: ��Ŀ¼����������ļ���
    :param find: ��������
    :param replace: �滻Ϊ
    :param pattern: �ļ����ˣ����ӣ�*.txt, *.json, *
    """
    counter = 0
    for path, sub_dirs, files in os.walk(root):
        for file_name in fnmatch.filter(files, pattern):
            if find in file_name:
                file_path = os.path.join(path, file_name)
                new_name = os.path.join(path, file_name.replace(find, replace))
                if file_path != new_name:
                    os.rename(file_path, new_name)
                    counter += 1
                    print(f"�޸��ļ���{file_path} -> {new_name}")
    print(f'�����ѽ����� �ܹ��޸��� {counter} ���ļ���')


def files_content_replace(root, find, replace, pattern="*"):
    """
    �������ļ����ݲ����滻
    :param root: ��Ŀ¼����������ļ���
    :param find: ��������
    :param replace: �滻Ϊ
    :param pattern: �ļ����ˣ����ӣ�*.txt, *.json *
    """
    find_counter = 0
    file_counter = 0
    for path, sub_dirs, files in os.walk(root):
        for file_name in fnmatch.filter(files, pattern):
            file_path = os.path.join(path, file_name)
            with open(file_path) as file:
                content = file.read()
            temp_counter = content.count(find)
            if temp_counter > 0:
                content = content.replace(find, replace)
                with open(file_path, "w") as file:
                    file.write(content)
                find_counter += temp_counter
                file_counter += 1
                print(f'�� {file_path} ���޸��� {temp_counter} ��')
    print(f'�����ѽ����� �ܹ��� {file_counter} ���ļ����޸��� {find_counter} ��')


def files_delete(root, find, backup=True):
    """
    �������ļ�ɾ��
    :param root: ��Ŀ¼����������ļ���
    :param find: �ļ���ƥ��
    :param backup: �Ƿ���ɾ��֮ǰ����
    """
    counter = 0
    for path, sub_dirs, files in os.walk(root):
        for file_name in files:
            if find in file_name:
                file_path = os.path.join(path, file_name)
                if backup is True:
                    if not os.path.exists(os.path.join(root, "backup")):
                        os.mkdir(os.path.join(root, "backup"))
                    backup_dir = os.path.join(root, "backup")
                    backup_path = os.path.join(backup_dir, file_name)
                    shutil.copyfile(file_path, backup_path)
                os.remove(file_path)
                counter += 1
                print(f"ɾ���� {file_path} ")
    print(f"�����ѽ�������ɾ���� {counter} ���ļ�")


if __name__ == '__main__':
    # files_delete(".\\", "glass")
    # files_name_replace(".\\", "concrete", "wool", "*.json")
    files_content_replace(".\\", "concrete", "wool", "*.json")
