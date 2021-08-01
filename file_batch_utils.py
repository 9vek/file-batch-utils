import shutil
import fnmatch
import os


def files_name_replace(root, find, replace, pattern="*"):
    """
    批处理文件名查找替换
    :param root: 根目录，会遍历子文件夹
    :param find: 查找内容
    :param replace: 替换为
    :param pattern: 文件过滤，例子：*.txt, *.json, *
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
                    print(f"修改文件：{file_path} -> {new_name}")
    print(f'任务已结束， 总共修改了 {counter} 个文件名')


def files_content_replace(root, find, replace, pattern="*"):
    """
    批处理文件内容查找替换
    :param root: 根目录，会遍历子文件夹
    :param find: 查找内容
    :param replace: 替换为
    :param pattern: 文件过滤，例子：*.txt, *.json *
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
                print(f'在 {file_path} 中修改了 {temp_counter} 项')
    print(f'任务已结束， 总共在 {file_counter} 个文件中修改了 {find_counter} 项')


def files_delete(root, find, backup=True):
    """
    批处理文件删除
    :param root: 根目录，会遍历子文件夹
    :param find: 文件名匹配
    :param backup: 是否在删除之前备份
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
                print(f"删除了 {file_path} ")
    print(f"任务已结束，共删除了 {counter} 个文件")


if __name__ == '__main__':
    # files_delete(".\\", "glass")
    # files_name_replace(".\\", "concrete", "wool", "*.json")
    files_content_replace(".\\", "concrete", "wool", "*.json")
