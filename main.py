from openai import OpenAI#for gpt
import openpyxl #excel handling
import google.generativeai as genai #for gemini

#API keys - i removed my keys, use urs for validation
OPENAI_API_KEY = ""
gemini_api_key = ""

# Configure the gpt,Gemini API
client=OpenAI(api_key=OPENAI_API_KEY)
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


#to get the attrs(3) and return as list of mentioned city and country
def get_attractions(city, country):
    prompt = f"Just List 3 major tourist attractions in {city}, {country}."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", "content":prompt
        }]
    )
    attractions = response.choices[0].message.text.strip().split('\n')
    return [attraction.strip() for attraction in attractions if attraction]


# function to get descriptions from ChatGPT
def get_chatgpt_description(country, city, attraction):
    #gpt prompt 
    prompt = (f"Provide a detailed description of the tourist attraction {attraction} in {city}, {country}. "
            f"The description should be between 2000 to 2500 characters.")        
    chatgpt_response= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", "content":prompt
        }])  # to ensure character count is between 2000 and 2500
    
    description = chatgpt_response.choices[0].message.text_strip()
    return description

# function to get descriptions from Gemini
def get_gemini_description(country, city, attraction):
    #gemini promptt
    gemini_response = chat.send_message(f"Provide a detailed description of the tourist attraction {attraction} in {city}, {country}. "
                f"The description should be between 2000 to 2500 characters.")
    description= gemini_response.text
    return description
    
# TODO: function to combine unique points from both descriptions,
#1. can make into set and combine for getting unique vals (but not correct)
#2. again make a API call to openAI and feed 2 responses to get unique combined descriptions
def combine_descriptions(chatgpt_desc, gemini_desc):

    #gpt prompt 
    prompt = (f"Combine the unique points of {chatgpt_desc} and {gemini_desc} and give a single paragraph response.")        
    chatgpt_response= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", "content":prompt
        }])  
    
    combined_desc= chatgpt_response.choices[0].message.text_strip()
    return combined_desc

# to save data in Excel
def save_to_excel(data, filename='tourist_attractions.xlsx'):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Tourist Attractions"

    #columns
    columns = ["Country", "City", "Attraction Name", "ChatGPT Description", "Gemini Description", "Combined Description"]
    sheet.append(columns)

    for row in data:
        sheet.append(row)

    workbook.save(filename)


def collect_data(country, city):
    data = []
    attractions= get_attractions(city, country)
    for attraction in attractions:
        chatgpt_desc = get_chatgpt_description(country, city, attraction)
        gemini_desc = get_gemini_description(country, city, attraction)
        combined_desc = combine_descriptions(chatgpt_desc, gemini_desc)
        data.append([country, city, attraction, chatgpt_desc, gemini_desc, combined_desc])
    return data

# Main 
if __name__=="__main__":
    country = input("Enter the country: ")#"France"
    city = input("Enter the city: ")#"Paris"
    data = collect_data(country, city)

    # Save the data to Excel
    save_to_excel(data)
