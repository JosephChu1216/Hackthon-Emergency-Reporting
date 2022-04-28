from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, EmailField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length

# from wtforms import ValidationError
# from flask_pagedown.fields import PageDownField
# from ..models import Role, User
arealist = [('Taipei_City', '台北市'), ('New Taipei_City', '新北市'), ('Keelung_City', '基隆市'),
            ('Taoyuan_City', '桃園市'), ('Hsinchu_County', '新竹縣'), ('Hsinchu_City', '新竹市'),
            ('Miaoli_City', '苗栗市'), ('Miaoli_County', '苗栗縣'), ('Taichung_City', '台中市'),
            ('Changhua_County', '彰化縣'), ('Changhua_City', '彰化市'), ('Nantou_City', '南投市'),
            ('Nantou_County', '南投縣'), ('Yunlin_County', '雲林縣'), ('Chiayi_County', '嘉義縣'),
            ('Chiayi_City', '嘉義市'), ('Tainan_City', '台南市'), ('Kaohsiung_City', '高雄市'),
            ('Pingtung_County', '屏東縣'), ('Pingtung_City', '屏東市'), ('Yilan_County', '宜蘭縣'),
            ('Yilan_City', '宜蘭市'), ('Hualien_County', '花蓮縣'), ('Hualien_City', '花蓮市'),
            ('Taitung_City', '台東市'), ('Taitung_County', '台東縣')]


class LoginForm(FlaskForm):
    username = StringField('What is your name?',
                           validators=[Length(min=1, max=12, message='Not Null'), DataRequired(message='Not Null')])
    password = PasswordField('password',
                             validators=[Length(min=4, max=12, message='Not Null'), DataRequired(message='Not Null')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    username_r = StringField('What is your name?',
                             validators=[Length(min=1, max=12, message='Not Null'), DataRequired(message='Not Null')])
    password_r = PasswordField('password',
                               validators=[Length(min=4, max=12, message='Not Null'), DataRequired(message='Not Null')])
    email = EmailField('What is your name?', validators=[DataRequired(message='Not Null')])
    sex = SelectField(u'Sex', choices=[('male', '男'), ('female', '女')], validators=[DataRequired(message='Not Null')])
    age = StringField(u'Age', validators=[Length(min=1, max=3, message='Not Null'), DataRequired(message='Not Null')])
    area = SelectField(u'Area', choices=[('Taipei_City', '臺北市'), ('New_Taipei_City', '新北市'), ('Keelung_City', '基隆市'),
                                         ('Taoyuan_City', '桃園市'), ('Hsinchu_County', '新竹縣'), ('Hsinchu_City', '新竹市'),
                                         ('Miaoli_City', '苗栗市'),
                                         ('Miaoli_County', '苗栗縣'), ('Taichung_City', '台中市'), ('Changhua_County', '彰化縣'),
                                         ('Changhua_City', '彰化市'),
                                         ('Nantou_City', '南投市'), ('Nantou_County', '南投縣'), ('Yunlin_County', '雲林縣'),
                                         ('Chiayi_County', '嘉義縣'),
                                         ('Chiayi_City', '嘉義市'), ('Tainan_City', '台南市'), ('Kaohsiung_City', '高雄市'),
                                         ('Pingtung_County', '屏東縣'),
                                         ('Pingtung_City', '屏東市'), ('Yilan_County', '宜蘭縣'), ('Yilan_City', '宜蘭市'),
                                         ('Hualien_County', '花蓮縣'),
                                         ('Hualien_City', '花蓮市'), ('Taitung_City', '台東市'), ('Taitung_County', '台東縣')])
    career = SelectField(u'Career', choices=["農、林、漁、牧業", "製造業", "批發及零售業", "運輸及倉儲業", "住宿及餐飲業",
                                             "出版影音及資通訊業", "金融及保險業", "教育業", "醫療保健及社會工作服務業", "藝術、娛樂及休閒服務業", "其他"])
    submit_r = SubmitField('Submit')


class PhotoForm(FlaskForm):
    image = FileField('Upload Your Image',
                      validators=[FileAllowed(['png', 'jpeg', 'jpg'], "wrong format!"), FileRequired()])
    submit_i = SubmitField('Submit')
