from files.mkd import mkd
from files.files_maker import files_gen
from files.files_sorter import sort_files
from files.files_mv import mvf

if __name__ == '__main__':
    dir_src = 'test'
    dir_mv = 'mvdir'
    dir_dst = 'sorted'
    mkd(dir_src)
    sample = {'tar': 3, 'gz': 2,
              'zip': 1, 'avi': 3,
              'png': 2, 'img': 1,
              'jpg': 3, 'mpg': 2,
              'mp4': 1, 'txt': 3,
              'md': 2, 'pdf': 1}
    sample2 = {'tar': 5, 'gz': 2}
    files_gen(dir_src, sample)
    sort_files(dir_src, dir_dst)
    mkd(dir_mv)
    files_gen(dir_mv, sample2)
    mvf('tar', 'arc', [2, 5], 2, "_renamed")
