# import streamlit as st

# def show_profile():
#     st.title('Profile')
#     st.write("""
#     Hi, I'm [Your Name], a passionate [Your Profession/Title] with experience in [Your Field].
#     """)

# def show_projects():
#     st.title('Projects')
#     st.subheader('Project 1: Project Name')
#     st.write("""
#     Description of Project 1. This project was about [Project Details].
#     - Technologies used: Python, Streamlit, Pandas
#     - [Link to Project Demo or Code Repository]
#     """)
#     # Add more projects as needed

# def show_skills():
#     st.title('Skills')
#     st.write("""
#     - Programming Languages: Python, JavaScript, SQL
#     - Frameworks/Libraries: Streamlit, Flask, React
#     - Tools: Git, Docker
#     - Data Analysis: Pandas, NumPy, Matplotlib
#     """)
#     # You can also add certifications or accomplishments here

# def show_contact():
#     st.title('Contact')
#     st.write("""
#     Feel free to reach out to me via email at [Your Email Address].
#     You can also find me on [LinkedIn](Your LinkedIn Profile Link) and [GitHub](Your GitHub Profile Link).
#     """)

# def main():
#     st.sidebar.title('Navigation')
#     menu = ['Profile', 'Projects', 'Skills', 'Contact']
#     choice = st.sidebar.selectbox('Select Option', menu)

#     if choice == 'Profile':
#         show_profile()
#     elif choice == 'Projects':
#         show_projects()
#     elif choice == 'Skills':
#         show_skills()
#     elif choice == 'Contact':
#         show_contact()

# if __name__ == '__main__':
#     main()






# import streamlit as st

# def show_profile():
#     st.title('Profile')
#     st.write("""
#     Hi, I'm [Your Name], a passionate [Your Profession/Title] with experience in [Your Field].
#     """)

# def show_projects():
#     st.title('Projects')
#     st.subheader('Project 1: Project Name')
#     st.write("""
#     Description of Project 1. This project was about [Project Details].
#     - Technologies used: Python, Streamlit, Pandas
#     - [Link to Project Demo or Code Repository]
#     """)
#     # Add more projects as needed

# def show_skills():
#     st.title('Skills')
#     st.write("""
#     - Programming Languages: Python, JavaScript, SQL
#     - Frameworks/Libraries: Streamlit, Flask, React
#     - Tools: Git, Docker
#     - Data Analysis: Pandas, NumPy, Matplotlib
#     """)
#     # You can also add certifications or accomplishments here

# def show_contact():
#     st.title('Contact')
#     st.write("""
#     Feel free to reach out to me via email at [Your Email Address].
#     You can also find me on [LinkedIn](Your LinkedIn Profile Link) and [GitHub](Your GitHub Profile Link).
#     """)

# def main():
#     st.sidebar.title('Navigation')
#     menu = ['Profile', 'Projects', 'Skills', 'Contact']
#     choice = st.sidebar.selectbox('Select Option', menu)

#     if choice == 'Profile':
#         show_profile()
#     elif choice == 'Projects':
#         show_projects()
#     elif choice == 'Skills':
#         show_skills()
#     elif choice == 'Contact':
#         show_contact()

# def load_code_from_file(file_path):
#     with open(file_path, 'r') as file:
#         code_content = file.read()
#     return code_content

# if __name__ == '__main__':
#     st.code(load_code_from_file("sample_text.txt"))
#     main()
#---------------------------------------------------------------

# import streamlit as st

# def main():

#     st.sidebar.title('業務用ポートフォリオ')
#     menu = ['TOP','VBA', 'python', 'RPA']
#     choice = st.sidebar.selectbox('Select Option', menu)

#     if choice == 'TOP':
#         show_TOP()
#     if choice == 'VBA':
#         show_VBA()
#     if choice == 'python':
#         show_python()
#     if choice == 'RPA':
#         show_RPA()



# def show_TOP():
#     st.title('TOP')

#     # 外部ファイルからテキストを読み込んで表示する
#     with open('TOP.txt', 'r',encoding='UTF-8') as file:

#         TOP_data = file.read()

#     # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
#     st.text(TOP_data)
#     # 画像を表示する
#     st.title('Sample Image')
#     # 画像ファイルのパス
#     img = open('sample_image.png', 'rb').read()  
#     st.image(img, caption='Sample Image', use_column_width=True)
#     # st.image(img, caption='Sample Image', width=1000)

# def show_VBA():

#     st.title('VBA')
#     # 外部ファイルからテキストを読み込んで表示する
#     with open('VBA.txt', 'r',encoding='UTF-8') as file:

#         VBA_data = file.read()

#     # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
#     st.text(VBA_data)
#     # 画像を表示する
#     st.title('Sample Image')
#     # 画像ファイルのパス
#     img = open('sample_image.png', 'rb').read()  
#     st.image(img, caption='Sample Image', use_column_width=True)
#     # st.image(img, caption='Sample Image', width=1000)

# def show_python():
#     st.title('python')

#     # 外部ファイルからテキストを読み込んで表示する
#     with open('python.txt', 'r',encoding='UTF-8') as file:

#         python_data = file.read()

#     # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
#     st.text(python_data)
#     # 画像を表示する
#     st.title('Sample Image')
#     # 画像ファイルのパス
#     img = open('sample_image.png', 'rb').read()  
#     st.image(img, caption='Sample Image', use_column_width=True)
#     # st.image(img, caption='Sample Image', width=1000)

# def show_RPA():
#     st.title('RPA')

#     # 外部ファイルからテキストを読み込んで表示する
#     with open('RPA.txt', 'r',encoding='UTF-8') as file:

#         RPA_data = file.read()

#     # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
#     st.text(RPA_data)
#     # 画像を表示する
#     st.title('Sample Image')
#     # 画像ファイルのパス
#     img = open('sample_image.png', 'rb').read()  
#     st.image(img, caption='Sample Image', use_column_width=True)
#     # st.image(img, caption='Sample Image', width=1000)


# if __name__ == '__main__':
#     main()
#---------------------------------------------------------------

#---------------------------------------------------------------
#--ログイン認証
# https://github.com/mkhorasani/Streamlit-Authenticator
# https://techblog.cccmkhd.co.jp/entry/2023/08/29/140205
#---------------------------------------------------------------
#--インストール
#pip install streamlit-authenticator
#--パスワードのハッシュ化
#①[config.yaml]ファイルを作成
#②ファイルに下記内容を入れる
#--------------------
# credentials:
#   usernames:
#     mame:
#       name: mame
#       password: 
#--------------------
#③下記コードを実行すると、
#ターミナルで、
#your name:   ⇒ユーザー名の登録
#your password:　⇒パスワードの登録　※表示されない
#[config.yaml]に書き込み。同じユーザーの場合は上書き、新規の場合は下に追加される
#write yaml file! ⇒登録が成功するとメッセージ
#[config.yaml]を確認すると password:にハッシュ化された文字列が追加される
#---------------------------------------------------------------
# from getpass import getpass
# import os
# import streamlit_authenticator as stauth
# import yaml

# yaml_path = "config.yaml"

# if __name__=="__main__":
#     yaml_data = {"credentials":{"usernames":{}}}
#     person = {}
#     if os.path.exists(yaml_path):
#         with open(yaml_path,"r") as f:
#             yaml_data = yaml.safe_load(f)
    
#     username = input("your name: ")
#     password = getpass("your password: ")
#     password = stauth.Hasher([password]).generate()[0]
#     # email = input("your email: ")
    
#     person = {
#         "name":username,
#         # "email":email,
#         "password":password
#     }
    
#     yaml_data["credentials"]["usernames"][username] = person
    
#     with open(yaml_path, "w") as f:
#         yaml.dump(yaml_data, f)
#         print("write yaml file!")

#---------------------------------------------------------------
#ログイン画面表示
#---------------------------------------------------------------
# import streamlit as st
# import streamlit_authenticator as stauth

# import yaml
# # from yaml.loader import SafeLoader


# with open("config.yaml","r") as file:
#     config = yaml.safe_load(file)

# authenticator = stauth.Authenticate(
#     config["credentials"],
#     cookie_name="some_cookie_name",
#     key="some_key",
#     cookie_expiry_days="1"
# )

# name, authentication_status, username = authenticator.login("Login","main")

# if authentication_status:
#     # 認証に成功
#     authenticator.logout("Logout","main")
#     # main()
# elif authentication_status == False:
#     # 認証に失敗(入力値が不正)
#     st.error("username/password is incorrect")
# elif authentication_status == None:
#     # 入力せずにログインを試みた場合
#     st.warning("Please enter your username and password")
#---------------------------------------------------------------
#--まとめ
#---------------------------------------------------------------
import streamlit as st
import streamlit_authenticator as stauth
import yaml
# from yaml.loader import SafeLoader

# st.set_page_config(
#     layout="wide"  # ページ全体のレイアウトをワイド表示に設定
# )

def main():

    st.sidebar.title('業務用ポートフォリオ')
    menu = ['TOP','VBA', 'python', 'RPA']
    choice = st.sidebar.selectbox('▼Select_Option', menu)

    if choice == 'TOP':
        show_TOP()
    if choice == 'VBA':
        show_VBA()
    if choice == 'python':
        show_python()
    if choice == 'RPA':
        show_RPA()

def show_TOP():

    st.title('TOP')
    # 外部ファイルからテキストを読み込んで表示する
    with open('TOP.txt', 'r',encoding='UTF-8') as file:

        TOP_data = file.read()

    # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
    st.text(TOP_data)
    # 画像を表示する
    st.title('Sample Image')
    # 画像ファイルのパス
    img = open('sample_image.png', 'rb').read()  
    st.image(img, caption='Sample Image', use_column_width=True)
    # st.image(img, caption='Sample Image', width=1000)

def show_VBA():

    st.title('VBA')
    # 外部ファイルからテキストを読み込んで表示する
    with open('VBA.txt', 'r',encoding='UTF-8') as file:

        VBA_data = file.read()

    # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
    st.text(VBA_data)
    # 画像を表示する
    st.title('Sample Image')
    # 画像ファイルのパス
    img = open('sample_image.png', 'rb').read()  
    st.image(img, caption='Sample Image', use_column_width=True)
    # st.image(img, caption='Sample Image', width=1000)

# def show_python():
#     st.title('■開発してきたツール■')

#     # 外部ファイルからテキストを読み込んで表示する
#     with open('python.txt', 'r',encoding='UTF-8') as file:

#         python_data = file.read()

#     # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
#     st.text(python_data)
#     # 画像を表示する
#     # st.title('※イメージ※社内FAQボット')
#     # 画像ファイルのパス
#     img = open('社内ボット.PNG', 'rb').read()  
#     st.image(img, caption='社内FAQボット', use_column_width=True)
#     # st.image(img, caption='Sample Image', width=1000)

def show_python():
    st.title('■開発してきたツール■')

    # 外部ファイルからテキストを読み込んで表示する
    with open('python.txt', 'r', encoding='UTF-8') as file:
        python_data = file.readlines()

    # 連番を示す変数
    count = 1

    for line in python_data:
        # 行が①、②、③などの形式で始まるかチェック
        if line.strip().startswith('①') or line.strip().startswith('②') or line.strip().startswith('③'):
            st.markdown(f"---\n```\n{line.strip()}\n```")  # 枠で囲んで表示
            count += 1

    # 画像を表示する
    img = open('社内ボット.PNG', 'rb').read()  
    st.image(img, caption='社内FAQボット', use_column_width=True)

def show_RPA():
    st.title('■開発してきたツール■')

    # 外部ファイルからテキストを読み込んで表示する
    with open('RPA.txt', 'r',encoding='UTF-8') as file:

        RPA_data = file.read()

    # st.markdown("<p style='text-align: center;'>Center Aligned Text</p>", unsafe_allow_html=True)
    
    st.text(RPA_data)
    # 画像を表示する
    # st.title('※イメージ※ダッシュボードSlack通知')
    # 画像ファイルのパス
    img = open('RPA.PNG', 'rb').read()  
    st.image(img, caption='ダッシュボードSlack通知', use_column_width=True)
    # st.image(img, caption='Sample Image', width=1000)

with open("config.yaml","r") as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config["credentials"],
    cookie_name="some_cookie_name",
    key="some_key",
    # cookie_expiry_days="1"
)

name, authentication_status, username = authenticator.login("Login","main")

if authentication_status:
    # 認証に成功
    authenticator.logout("Logout","sidebar")
    main()
elif authentication_status == False:
    # 認証に失敗(入力値が不正)
    st.error("username/password is incorrect")
elif authentication_status == None:
    # 入力せずにログインを試みた場合
    st.warning("Please enter your username and password")
