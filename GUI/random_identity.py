#!/usr/bin/evn python3
# -*- coding:utf-8 -*-
import random
from datetime import date
from datetime import timedelta


class RandomID(object):

    @staticmethod
    def create_phone():
        # 第二个数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三个数字
        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9), }[second]
        # 最后8位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)

    @staticmethod
    def get_district():
        code_list = []
        # 读取地区码
        file = open('../data/district.txt',
                    encoding='ISO-8859-1')
        lines = file.readlines()
        # 逐行读取
        for line in lines:
            # 如果每行中去重后不为空，并且6位数字中最后两位不为00，则添加到列表里。（最后两位为00时为省份或地级市代码）
            if line.lstrip().rstrip().strip() != '' and (line.lstrip().rstrip().strip())[:6][-2:] != '00':
                code_list.append(line[:6])
        return code_list

    def create_id_card(self):
        code_list = self.get_district()
        id = code_list[random.randint(0, len(code_list))]  # 地区项
        id = id + str(random.randint(1950, 1998))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  # 顺序号简单处理

        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8',
                      '5': '7', '6': '6', '7': '5', '8': '5', '9': '3', '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        id = id + check_code[str(count % 11)]  # 算出校验码
        return id

    @staticmethod
    def create_name():
        global n
        xing = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '窦', '章',
                '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '余', '元', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                '姚', '邵', '堪', '汪', '祁', '禹', '戴', '宋', '庞',
                '纪', '舒', '屈', '项', '祝', '董', '梁']

        ming = ['为', '子', '中', '生', '国', '年', '着', '和', '得', '里', '后', '自',
                '家', '可', '下', '而', '过', '天', '去', '能', '对', '多', '然', '于', '心', '学',
                '好', '起', '发', '当', '没', '成', '只', '如', '事', '还', '道', '想', '作', '种', '开',
                '美', '总', '从', '无', '情', '己', '面', '最', '现', '前', '所', '同', '日', '又', '行', '意',
                '动', '方', '经', '长', '回', '位', '分', '爱', '老', '因', '给', '名', '法', '间', '斯',
                '知', '世', '次', '者', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '正',
                '感', '见', '明', '问', '力', '理', '尔', '点', '文', '定', '本', '公', '特', '外', '相', '西', '果',
                '将', '月', '实', '向', '声', '车', '全', '信', '重', '工', '并', '别', '真',
                '太', '新', '比', '才', '夫', '再', '书', '部', '水', '像', '等', '却', '加', '电', '主', '界',
                '门', '利', '海', '受', '德', '少', '克', '代', '员', '先', '由', '安', '写',
                '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '更', '东', '记',
                '应', '直', '字', '平', '报', '友', '关', '放', '至', '告', '笑', '内', '英',
                '军', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '边', '风', '解', '金', '快',
                '原', '吃', '变', '通', '师', '立', '象', '数', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条',
                '始', '达', '深', '完', '今', '提', '求', '清', '化', '空', '业', '思', '切', '非', '片',
                '语', '元', '喜', '曾', '离', '飞', '科', '言', '流', '欢', '约', '即', '指', '合',
                '反', '题', '必', '该', '论', '交', '终', '林', '晚', '决', '传', '画', '保', '运',
                '及', '则', '早', '量', '苦', '火', '布', '品', '近', '产', '答', '星', '视', '连', '司',
                '巴', '奇', '管', '类', '未', '朋', '且', '台', '夜', '青', '北', '久', '乎', '越', '观', '落', '尽', '形',
                '影', '红', '百', '令', '识', '步', '希', '亚', '术', '留', '半', '送', '兴', '造', '谈',
                '容', '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '计',
                '装', '似', '双', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '刻',
                '统', '断', '福', '城', '故', '历', '惊', '包', '争', '另', '建', '维', '绝', '树', '系', '伤', '示',
                '愿', '持', '千', '史', '准', '联', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '消', '社',
                '算', '义', '竟', '确', '酒', '需', '单', '治', '幸', '兰', '念', '举', '仅', '钟', '共', '毛', '句', '息',
                '功', '官', '待', '究', '室', '易', '游', '程', '号', '居', '考', '突', '费', '倒', '价', '图',
                '具', '刚', '永', '歌', '响', '商', '礼', '细', '专', '黄', '味', '灵', '改', '据', '般', '破', '引',
                '存', '众', '注', '笔', '甚', '沉', '备', '习', '校', '默', '务', '微', '须', '试',
                '怀', '料', '调', '广', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '参', '八', '除',
                '跑', '亮', '印', '设', '线', '温', '虽', '京', '初', '养', '香', '际', '致', '阳', '纸', '纳',
                '验', '助', '严', '证', '帝', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿',
                '展', '获', '艺', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢',
                '否', '排', '背', '止', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河',
                '续', '若', '推', '境', '遇', '雨', '标', '充', '围', '案', '伦', '护', '冷', '贝', '著', '雪',
                '索', '险', '烟', '依', '斗', '值', '帮', '汉', '佛', '肯', '闻', '沙', '局', '伯', '族',
                '低', '资', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '露', '园', '牛', '旅',
                '烈', '莫', '异', '宝', '权', '鲁', '简', '态', '寻',
                '律', '胜', '洋', '范', '舞', '秘', '午', '登', '贵', '责', '例', '较', '职',
                '属', '渐', '左', '录', '丝', '党', '继', '章', '智', '冲', '叶', '胡', '吉', '坚',
                '修', '松', '临', '藏', '戏', '善', '卫', '敢', '伊', '戴', '词', '森', '耳',
                '差', '祖', '云', '规', '散', '迷', '油', '旧', '适', '乡', '恩', '投', '博', '雷',
                '压', '超', '负', '勒', '采', '毫', '毕', '冰', '既', '状', '景', '席', '珍', '童',
                '顶', '派', '素', '农', '疑', '野', '按', '拍', '征', '骨', '余', '承', '彩',
                '巨', '琴', '环', '束', '增', '忍', '洛', '塞', '忆', '判', '欧',
                '付', '阵', '项', '休', '懂', '武', '革', '良', '恋', '委', '娜', '妙',
                '营', '摇', '诺', '宣', '银', '宫', '康', '供', '优',
                '降', '夏', '困', '健', '伴', '守', '挥', '鲜', '财', '孤', '伙',
                '杰', '迹', '盖', '坦', '江', '顺', '秋', '萨', '划', '授', '归', '浪', '听', '凡',
                '预', '雄', '升', '典', '莱', '含', '盛', '济', '蒙', '释', '介', '乾', '坤']

        for i in range(1):
            x = random.randint(0, len(xing))
            m1 = random.randint(0, len(ming)-1)
            m2 = random.randint(0, len(ming)-1)
            n = ('' + xing[x] + ming[m1] + ming[m2])
        return n

    @staticmethod
    def create_bank_account():
        # 工行卡号开头
        prefix = "622202"
        # prefix = "622609"  # 招行卡
        for i in range(13):
            prefix = prefix + str(random.randint(0, 9))
        return prefix

    @staticmethod
    def car_id():
        char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
        # 车牌号中没有I和O，可自行百度
        char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
        char2 = '1234567890'
        len0 = len(char0) - 1
        len1 = len(char1) - 1
        len2 = len(char2) - 1

        code = ''
        index0 = random.randint(1, len0)
        index1 = random.randint(1, len1)
        code += char0[index0]
        code += char1[index1]
        for i in range(1, 6):
            index2 = random.randint(1, len2)
            code += char2[index2]
        return code


if __name__ == '__main__':
    random_id = RandomID()
    name = random_id.create_name()
    phone = random_id.create_phone()
    id_card = random_id.create_id_card()
    account = random_id.create_bank_account()
    car_id = random_id.car_id()
    # print("姓名：%s" % name)
    # print("手机号：%s" % phone)
    # print("身份证号：%s" % id_card)
    # print("银行卡号：%s" % account)
    for i in range(1):
        # name = random_id.create_name()
        # phone = random_id.create_phone()
        # id_card = random_id.create_id_card()
        # account = random_id.create_bank_account()
        # car_id = random_id.car_id()
        print(name+"," + phone + "," + id_card + "," +account + "," + car_id)
        # print(id_card)
