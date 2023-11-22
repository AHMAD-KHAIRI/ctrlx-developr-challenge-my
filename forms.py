from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TelField, SelectMultipleField, widgets, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired
from markupsafe import Markup

class BootstrapListWidget(widgets.ListWidget):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = [f"<{self.html_tag} {widgets.html_params(**kwargs)}>"]
        for subfield in field:
            if self.prefix_label:
                html.append(f"<li class='list-group-item'>{subfield.label} {subfield(class_='form-check-input ms-1')}</li>")
            else:
                html.append(f"<li class='list-group-item'>{subfield(class_='form-check-input me-1')} {subfield.label}</li>")
        html.append("</%s>" % self.html_tag)
        return Markup("".join(html))

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class RegistrationForm(FlaskForm):
    group_name = StringField(label='Team name', validators=[DataRequired(message="This field is required. For Academia, insert A_ before your Group name. For Industry, insert I_ before your Group name.")])
    # group_member_one = StringField(label='Group member one: Enter your name', validators=[DataRequired(message="This field is required.")])
    # group_member_two = StringField(label='Group member two: Enter your name')
    # group_member_three = StringField(label='Group member three: Enter your name')
    # group_member_four = StringField(label='Group member four: Enter your name')

    # TO-DO: Add sector categories and store in database
    # sector_categories = MultiCheckboxField(label='Industry Sector Categories:',
    #                             choices=[('academia', 'Academia'), 
    #                                         ('industry', 'Industry')],validators=[InputRequired(message="Please select one.")])
    # occupation = StringField(label='Occupation:')
    # # occupation = StringField(label='Occupation:', render_kw={"style": "display: none;"})
    # education = StringField(label='Enter your education background', validators=[DataRequired(message="This field is required.")])
    # handphone = TelField(label='Enter your mobile number', validators=[DataRequired(message="This field is required.")])
    email = EmailField(label='Main email address', validators=[DataRequired(message="This field is required."), Email(message="Enter a correct email.")])
    password = PasswordField("Set password", validators=[DataRequired()])
    
    # Define the categories field as a SelectMultipleField
    # interest_categories = MultiCheckboxField(label='Categories of Interest:', 
    #                                 choices=[('data_collection', 'Machine Data Collection/ Big Data'), 
    #                                 ('plc', 'Programmable Logic Controllers (PLC)'), 
    #                                 ('hmi', 'Human Machine Interface (HMI)'), 
    #                                 ('iot', 'Internet of Things (IoT)'),
    #                                 ('low_code', 'Low-Code / No-Code (e.g. Blockly)'),
    #                                 ('motion', 'Motion Control'),
    #                                 ('simulation', 'Simulation/ Digital Twin')],validators=[InputRequired(message="Select at least one.")])
    agree_to_tnc = BooleanField(label='I accept the Terms and Conditions for the Registration and Use of Services', validators=[DataRequired(message="This field is required.")])
    submit = SubmitField(label='Register and take me to the developR challenge!')


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Take me to the developR challenge.")
