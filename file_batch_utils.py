import fnmatch
import os


def files_name_replace(root, find, replace, suffix="*"):
    """
    批处理文件名查找替换
    :param root: 根目录，会遍历子文件夹
    :param find: 查找内容
    :param replace: 替换为
    :param suffix: 文件过滤，例子：*.txt, *.json, *
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
                    print(f"修改文件：{file_path} -> {new_name}")

    print(f'任务已结束， 总共修改了 {counter} 个文件名')


def files_content_replace(root, find, replace, suffix="*"):
    """
    批处理文件内容查找替换
    :param root: 根目录，会遍历子文件夹
    :param find: 查找内容
    :param replace: 替换为
    :param suffix: 文件过滤，例子：*.txt, *.json *
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
                print(f'在 {file_path} 中修改了 {temp_counter} 项')

    print(f'任务已结束， 总共在 {file_counter} 个文件中修改了 {find_counter} 项')


if __name__ == '__main__':
    files_name_replace(".\\", "wool", "wool")
    files_content_replace(".\\", "wool", "wool")
