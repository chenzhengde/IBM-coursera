# 冬季课题项目调查问卷

student_school = input('请问您的学校 ')
student_year = input('请问您的年级 ')
student_major = input('请问您更偏向于2+2还是4+0 ')

# 第一部分是关于直接就业海外读研的调查
# old_decision是疫情前打算的毕业去向
# original_country是原预想留学地区
# present_country是现预想留学地区
# reason_for_change是疫情发生后换地区的原因
work_or_not = int(input('请问您毕业后是准备就业还是读研？就业输入1 读研输入2 '))
if work_or_not == 1:
    old_decision = input('疫情前打算的毕业去向？就业/读研 ')
    print('问卷结束，谢谢参与')
    print(old_decision)
elif work_or_not == 2:
    decision_change_or_not = int(input('疫情是否改变了原先的读研计划？ 不变输入1 改变输入2 '))
    # 1 没有改变，研究生去向（大陆，东南亚，北美，欧洲，澳洲）
    # 2 改变，原先地区，现在地区，原因
    if decision_change_or_not == 1:
        # original_country是一个多选题
        original_country = input('研究生去向（大陆，香澳台，新加坡，北美，英国及欧盟，澳洲） ')
        print('问卷结束，谢谢参与')
        print(f'研究生去向：{original_country}')
    elif decision_change_or_not == 2:
        original_country = input('原预想留学地区 ')
        present_country = input('现预想留学地区 ')
        # 原因是填空，剩下的做成选择，original_country和present_country也是选择（六选一）
        reason_for_change = input('请简要说明改变的原因 ')
        print('问卷结束，谢谢参与')
        print(f'原预想留学地区：{original_country}, 现预想留学地区：{present_country}, 原因：{reason_for_change}')

# 第二部分是关于疫苗的调查
# 随着疫苗技术的发展，是否会对您的选择造成改变
# 已知新冠疫苗保护效力为80%左右，且中国留学生可以优先免费注射疫苗
# 1 是否愿意接种疫苗 假如否，问题结束 假如是，进入下个问题
# 2 接种疫苗后，原先的计划是否发生改变（如继续疫情前的计划，包括继续选择2+2）
# 请选择一个选项：
# A 不打算出国，接种后决定出国
# B 打算出国，接种并不改变计划
# C 不打算出国，接种并不改变计划

print('已知新冠疫苗保护效率为80%左右，且中国留学生可以优先免费注射疫苗')
vaccine_or_not = int(input('是否愿意接种疫苗 若愿意注射1 不愿意注射2 '))
if vaccine_or_not == 2:
    print('感谢参与')
    print('不愿意注射疫苗')
elif vaccine_or_not == 1:
    print('''
A 不打算出国，接种后决定出国
B 打算出国，接种并不改变计划
C 不打算出国，接种并不改变计划
    ''')
    choice_question = input('请选择一个选项: ')
    print('感谢参与')
    if choice_question == 'A':
        print('不打算出国，接种后决定出国')
    elif choice_question == 'B':
        print('打算出国，接种并不改变计划')
    elif choice_question == 'C':
        print('不打算出国，接种并不改变计划')
