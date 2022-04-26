class Gallery:
    __gallery_no = 0
    __user_no = 0
    __gallery_content = ''
    __photo_path = ''
    __hashtag = ''
    __gallery_readcount = 0
    __gallery_date = ''
    __comment_no = 0
    __user_no_1 = 0
    __comment_content = ''
    __comment_date = ''

    def __init__(self, gallery_dict):
        self.__gallery_no = gallery_dict['g_no']
        self.__user_no = gallery_dict['u_no']
        self.__gallery_content = gallery_dict['content']
        self.__photo_path = gallery_dict['photopath']
        self.__hashtag = gallery_dict['hashtag']
        self.__gallery_readcount = gallery_dict['rcount']
        self.__gallery_date = gallery_dict['date']
        self.__comment_no = gallery_dict['c_no']
        self.__user_no_1 = gallery_dict['u_no_1']
        self.__comment_content = gallery_dict['c_content']
        self.__comment_date = gallery_dict['c_date']

    def __del__(self):
        print(self, '인스턴스 소멸됨')

    def set_galleryno(self, galleryno):
        self.__gallery_no = galleryno

    def set_userno(self, userno):
        self.__user_no = userno

    def set_gallerycontent(self, gallerycontent):
        self.__gallery_content = gallerycontent

    def set_photopath(self, photopath):
        self.__photo_path = photopath

    def set_hashtag(self, hashtag):
        self.__hashtag = hashtag

    def set_galleryreadcount(self, galleryreadcount):
        self.__gallery_readcount = galleryreadcount

    def set_gallerydate(self, gallerydate):
        self.__gallery_date = gallerydate

    def set_commentno(self, commentno):
        self.__comment_no = commentno

    def set_userno1(self, userno1):
        self.__user_no_1 = userno1

    def set_commentcontent(self, commentcontent):
        self.__comment_content = commentcontent

    def set_commentdate(self, commentdate):
        self.__comment_date = commentdate

    def info(self):
        return '갤러리 값 : {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(self.__gallery_no,
                self.__user_no, self.__gallery_content, self.__photo_path, self.__hashtag, self.__gallery_readcount, self.__gallery_date,
                self.__comment_no, self.__user_no_1, self.__comment_content, self.__comment_date)
