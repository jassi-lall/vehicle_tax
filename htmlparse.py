from bs4 import BeautifulSoup

with open('stage2.htm', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
x = soup.find_all('input', {'id':'wizard_vehicle_enquiry_capture_vrn_vrn'})
print(len(x))



""""
forms = soup.find_all('form')
for form in forms:
    print(form.prettify())
    for input in form.find_all('input'):
        print('#' * 30)
        print(input.prettify())
        print('#' * 30)
    print('---------------------------------------------')


print("\n" * 4)

"""