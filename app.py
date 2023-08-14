import streamlit as st
import QR_Gen
import pdf_create as pdf
from PIL import Image
import style
page_bg_img = style.stylespy() #used for styling the page

# Appname

st.set_page_config(page_title="Child Safety QRAI 🖌️",layout="wide")

st.markdown(page_bg_img,unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4C2164;'>Child Safety QR.AI 🖌️</h1>", unsafe_allow_html=True)

# Split the page into two columns
col1, col2 = st.columns(2,gap='medium')










# Form UI in the first column
with st.form(key="form1"):

        
        
        with col1:
            
            Name = st.text_input('Enter First name')
            Address = st.text_input('Enter your address')
            Birthday = st.date_input('Your birthday')
            Gender = st.radio('Gender', ['Male', 'Female', 'Others'])
            Contact = st.number_input('Enter your contact number')
            anothercontact = st.number_input('Enter another contact number')
            Contact_Email = st.text_input('Enter Contact email address')
            FathersName = st.text_input("Enter Father's name")
            MothersName = st.text_input('Enter Mother"s name')
        with col2:
            
            SchoolName = st.text_input('Enter your school name')
            SchoolAddress = st.text_input('Enter your school address')
            city = st.text_input('City')
            state = st.text_input('State')
            ZipCode = st.number_input('Zip code')
            Country = st.text_input('Country')
            Addhar = st.number_input('Last four digit of Addhar number')
            Blood_Group = st.selectbox('Blood Group', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
            Identification_mark = st.text_input('Identification mark')
            Allergenes = st.text_input('Allergenes')
            uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        
        submit = st.form_submit_button(label="Submit",use_container_width=True)        


  

# Controlnet UI in the second column

st.header("QR Generation")
with st.form(key="form2"):
        p_prompt = st.text_input('Positive Prompt')
        n_prompt = st.text_input('Negative Prompt')
        conditioning_scale = st.slider('Controlnet Conditioning Scale', 0.0, 5.0)
        strength = st.slider('Strength', 0.0, 1.0)
        guidance_scale = st.slider('Guidance Scale', 1.00, 50.00)
        sampler = st.selectbox('Sampler', ['DPM++ Karras SDE', 'DPM++ Karras', 'Heun', 'Euler', 'DDIM', 'DEIS'])
        seed = st.slider('Seed value', -1, 9999999999)
        genarate = st.form_submit_button(label="Generate",use_container_width=True)

# Process form submissions and getting the link of the generated pdf
if submit:
    st.write(Name,  Birthday, FathersName, MothersName, Gender)
    if uploaded_file is not None:
        st.subheader("Uploaded Image")
        # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True) #used for showing the uploaded image
    
        save_path = "uploaded_image.png"
        pil_image = Image.open(uploaded_file)
        pil_image.save(save_path)
        st.success(f"Image saved as {save_path}")
        # fileURL = str(pdf.create_qr_code_pdf(Name,Birthday,FathersName,MothersName,Address,Gender,Contact,anothercontact,Contact_Email,SchoolName,SchoolAddress,city,state,ZipCode,Country,Blood_Group,Identification_mark,Allergenes)) #used for generating the pdf
        st.success("In the next step enter your prompt")
        # st.write(fileURL) #used for showing the link of the generated pdf
    else:
        st.info("Please upload an image.")
        
positive_prompt = str(p_prompt)
negative_prompt = str(n_prompt)
Sampler = str(sampler)
Conditioning_scale = float(conditioning_scale)
Strength = float(strength)
Guidance_scale = float(guidance_scale)
Seed = int(seed)
fileURL = str(pdf.create_qr_code_pdf(Name,Birthday,FathersName,MothersName,Address,Gender,Contact,anothercontact,Contact_Email,SchoolName,SchoolAddress,city,state,ZipCode,Country,Blood_Group,Identification_mark,Allergenes))
#QR code generation
if genarate:
    # fileURL = str(pdf.create_qr_code_pdf(Name,Birthday,FathersName,MothersName,Address,Gender,Contact,anothercontact,Contact_Email,SchoolName,SchoolAddress,city,state,ZipCode,Country,Blood_Group,Identification_mark,Allergenes)) #used for generateing pdf upload and returning the upload link
    genimg = QR_Gen.generate_qr_code(fileURL,positive_prompt, negative_prompt, Sampler, Strength, Conditioning_scale, Guidance_scale, Seed) #used for generateing 
    image = Image.open(genimg)
    st.image(image, caption='Generated QR code')
    st.success("QR code generated successfully")

