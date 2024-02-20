import streamlit as st
st.title("Title -> Hey Welcome!")                                               #title tag
#noe another command on streamlit
st.header("Header -> Hey Welcome!")                                             #header tag
st.subheader("subHeader -> Hey Welcome!")                                       #subheader tag
st.text("Text -> Hey Welcome!")#text tag used as a kind of a paragraph tag      #text

#heading inhtml in jupyter notebook
st.markdown("# Hi")                                                             #markdown
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("#### Hi")
st.markdown("##### Hi")
st.markdown("Hi")
#if someting is warning or if someting is sicced
st.success("Data is Submitted")                                                 #success 
#info to dipaly info of out choice
st.info("Information !")                                                        #info
st.warning("Warning!")                                                          #warning
st.error("Error!")                                                              #error
#to show a specific error
exp = ZeroDivisionError("Division not possible with 0")                         #exception
st.exception(exp)

st.help(ZeroDivisionError)# takw to documentation of that page #Help

#more command in detail
#how write code into it or write text in diff manner
st.write("range(1,10)")
st.write(range(1,10))#it is not string anymore
st.write("1+2+3")
st.write(1+2+3)

#code to write specific code# wirte in 1,2 3 string
st.code('x = 10\n'                                                              #code
        'for i in range(x):\n'
            '\tprint(i)')

#radie buttons  and checkbox                                                    #checkbox
st.checkbox('Male')# two checkbox or key cannot be same
st.checkbox('Female')

if(st.checkbox('Adult')):#different checkbox
    st.write("you are an adult")

#sameting with radio butteon
#st.radio('Select : ', ('Male' ,'Female',"other"))

radioButton=st.radio('Select : ', ('Male' ,'Female',"other"))                   #radio
if(radioButton=="Male"):
    st.write("You are a Male")
elif(radioButton=="Female"):
    st.write("You are a Female")
elif(radioButton=="other"):
    st.write("You  are an other Gender")

#select feedback also
st.subheader("Select box")                                                     #selectbox
selectBox=st.selectbox("Data Science :",["Data Analysis" ,"Web Scraping",
                       "Machine Leaning", "Deep Learning","NLP","CV",
                       "Image processing"])
st.write("You Have Selected :" ,selectBox)

st.subheader("Select box")                                                     #multiselectbox

st.subheader("multiselect box")
multiselectBox=st.multiselect("Data Science :",["Data Analysis" ,"Web Scraping",
                       "Machine Leaning", "Deep Learning","NLP","CV",
                       "Image processing"])
st.write("You Have Selected :" ,len(multiselectBox), multiselectBox ,"courses")

st.subheader("Button")
#st.button("Click me")
if (st.button("Click me")):
    st.write("Thanks for clicking me")                                               #Button

st.subheader("slider")                                                               #Slider
st.slider("Select the Level",1,10,step=1)
Vol=st.slider("Select the volume",1,100,step=1)
st.write("Volume is",Vol)

st.subheader("text Input")                                                           #Text_input
username =st.text_input("Username:")
pasword =st.text_input("Password:",type="password")

st.subheader("text Area")                                                            #text area 
st.text_area("write about yourself ")

st.subheader("text Number")                                                            #text-Number
st.number_input("Select Your Age",18,110)
st.subheader("text Date")
st.date_input("Date")                                                            #text-Date

st.subheader("text Time") 
st.time_input("Time")                                                           #text-Time


