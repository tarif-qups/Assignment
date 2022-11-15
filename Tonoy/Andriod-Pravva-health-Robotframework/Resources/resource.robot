*** Settings ***
Library  AppiumLibrary
Library  BuiltIn
Variables  ../Locators/locators.py
Variables  ../TestData/TestData.py


*** Keywords ***

# signup
Action_For_SignUp_Action
  Sleep  5
  click element  ${signup_ID}
  sleep  5
  input text  ${mobile_ID}  ${number}
  sleep  5
  input text  ${username_ID}  ${username}
  sleep  5
  input text  ${password_ID}  ${password}
  sleep  5
  input text  ${repassword_ID}  ${repassword}
  sleep  5
  input text  ${email1_ID}  ${email1}
  sleep  5
  click element  ${login0_ID}
  sleep  5

# forget password

Action_For_forget_password
  click element  ${forgetpass_ID}
  sleep  5
  input text  ${forgetusername_ID}  ${number}
  sleep  5
  click element  ${login1_ID}
  sleep  5

# forget user name / mobile\

Action_For_forget_username
  click element  ${forgetusern_ID}
  sleep  5
  input text  ${forgetusermob_ID}  ${number}
  sleep  5
  click element  ${login2_ID}
  sleep  5

# LOGIN

Action_For_LOGIN
  input text  ${loginuser_ID}  ${number}
  sleep  5
  input text  ${loginpass_ID}  ${password}
  sleep  5
  click element  ${login_ID}
  sleep  5

# Book an appointment

Action_For_Book_Appointment
  click element  ${book_ID}
  sleep  5
  click element  ${service_ID}
  sleep  5
  click element  ${familyphysicans_XPATH}
  sleep  5
  click element  ${liketosee_ID}
  sleep  5
  click element  ${taslima_XPATH}
  sleep  5
  go back
  sleep  5
  go back
  sleep  5

# book a health check
# Annual Membership plan

Action_For_Health_Check
  click element  ${bookhealth_ID}
  sleep  5
  click element  ${annualplan_XPATH}
  sleep  5
  click element  ${viewdetils_ID}
  sleep  5
  click element  ${ecg_XPATH}
  sleep  5
  click element  ${booked_ID}
  sleep  5
  go back
  sleep  5
  click element  ${healthcheck_XPATH}
  sleep  5
  click element  ${diabetesviewdetails_XPATH}
  sleep  5
  click element  ${booked1_XPATH}
  sleep  5
  go back
  sleep  5
  go back
  sleep  5

# signup for a membership plan

Action_For_Membership_Plan
  click element  ${signupmembership_ID}
  sleep  5
  click element  ${signupmembershipok_ID}
  sleep  5
  go back
  sleep  5

# map

Action_For_Map
  click element  ${map_ID}
  sleep  5
  click element  ${mapallow_ID}
  sleep  5
  go back
  sleep  5

# Registation

Action_For_Register
  click element  ${register_XPATH}
  sleep  5
  input text  ${reg_fstname_ID}  ${username}
  sleep  5
  input text  ${reg_middlename_ID}  ${middlename}
  sleep  5
  Swipe    716    1374    716    372
  input text  ${reg_lastname_ID}  ${lastname}
  sleep  5
  click element  ${dateofbirth_ID}
  sleep  5
  click element  ${date_ok_ID}
  sleep  5
  input text  ${email_ID}  ${email1}
  sleep  5
  click element  ${selectgender_ID}
  sleep  5
  click element  ${gendercancel_ID}
  sleep  5
  Swipe    619    1366    639    472
  input text  ${nationality_ID}  ${nationality}
  sleep  5
  click element  ${selectstatus_ID}
  sleep  5
  click element  ${statuscancel_ID}
  sleep  5
  click element  ${selectoccupation_ID}
  sleep  5
  click element  ${occupationcancel_ID}
  sleep  5
  input text  ${phnnmbr_ID}  ${number}
  sleep  5
  Swipe    662    1378    662    507
  input text  ${address_ID}  ${address}
  sleep  5
  input text  ${city_ID}  ${city}
  sleep  5
  input text  ${state_ID}  ${state}
  sleep  5
  input text  ${city_ID}  ${city}
  sleep  5
  input text  ${state_ID}  ${state}
  sleep  5
  input text  ${country_ID}  ${country}
  sleep  5
  Swipe    666    1370    662    422
  input text  ${postalcode_ID}  ${postcode}
  sleep  5
  input text  ${emergncycontact_ID}  ${number}
  sleep  5
  click element  ${selectrelation_ID}
  sleep  5
  click element  ${relationcancel_ID}
  sleep  5
  input text  ${emergncycontact1_ID}  ${number}
  sleep  5
  Swipe    573    1370    604    604
  click element  ${aboutus_ID}
  sleep  5
  click element  ${aboutuscancel_ID}
  sleep  5
  click element  ${radioclick1_ID}
  sleep  5
  click element  ${radioclick2_ID}
  sleep  5
  go back

# link your + your family's accounts

Action_For_link
  click element  ${linkfamilysaccount_ID}
  sleep  5
  click element  ${linkfamilysaccountok_ID}
  sleep  5
  click element  ${addprofile_ID}
  sleep  5
  click element  ${cross_ID}
  sleep  5
  go back
  sleep  5

# how can we serve you better?

Action_For_serve
  click element  ${serve_ID}
  sleep  5
  click element  ${addmemberok_ID}
  sleep  5
  go back
  sleep  5

# contact us

Action_For_contact_us
  click element  ${contactus_ID}
  sleep  5
  click element  ${contactallow_ID}
  sleep  5
  go back
  sleep  5

# Logout

Action_For_Logout
  click element  ${navigate3_XPATH}
  sleep  5
  Swipe    627    2152    658    898
  click element  ${logout_XPATH}
  sleep  5

