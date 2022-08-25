import streamlit as st
import pickle
import sklearn

st.image('imagee.png',width=700)
model=pickle.load(open('model.pkl','rb'))
st.title("Loan Prediction")
name=st.text_input("Name")

#for gender
gen_display=("Female","Male")
gen_options=list(range(len(gen_display)))
gen=st.radio("Select your Gender",gen_options,format_func=lambda x:gen_display[x])

#for Marital status
mar_display=("No","Yes")
mar_options=list(range(len(mar_display)))
mar=st.radio("Are you Married?",mar_options,format_func=lambda x:mar_display[x])

#for Education
edu_display=("Not Graduate","Graduate")
edu_options=list(range(len(edu_display)))
edu=st.radio("Select your Education Status",edu_options,format_func=lambda x:edu_display[x])

#for Dependents
dep_display=("Zero","One","Two","More than two")
dep_options=list(range(len(dep_display)))
dep=st.radio("Number of Dependents",dep_options,format_func=lambda x:dep_display[x])

#for Property
prop_display=("Rural","Semi-Urban","Urban")
prop_options=list(range(len(prop_display)))
prop=st.radio("Property Area",prop_options,format_func=lambda x:prop_display[x])

#for credit
cred_display=("Between 300 to 500","Above 500")
cred_options=list(range(len(cred_display)))
cred=st.radio("Credit Score",cred_options,format_func=lambda x:cred_display[x])

#for emp
emp_display=("Job","Business")
emp_options=list(range(len(emp_display)))
emp=st.radio("Employment",emp_options,format_func=lambda x:emp_display[x])

mon_inc=st.number_input("Applicant's Monthly Income",value=0)
co_mon_inc=st.number_input("Co-Applicant's Monthly Income",value=0)
loan_amt=st.number_input("Loan Amount",value=0)

dur=st.radio('Loan Duration',("2 Months","6 Months","8 Months","1 Year","16 Months"))

if st.button("Submit"):
    duration=0
    if dur==0:
        duration=60
    if  dur==1:
        duration=180
    if  dur==2:
        duration=240
    if  dur==3:
        duration=360
    if  dur==4:
        duration=480
    features=[[gen,mar,dep,edu,emp,mon_inc,co_mon_inc,loan_amt,duration,cred,prop]]
    print(features)
    prediction=model.predict(features)
    lc=[str(i) for i in prediction]
    ans=int("".join(lc))
    if ans==0:
        st.write(
            "Hello "+name+"," ,
            "Acoording to our calculations,you will not get the loan from Bank"
        )
    else:
        st.write(
            "Hello "+name+"," ,
            'Congratulations!!! You will get the loan from Bank'
        )

