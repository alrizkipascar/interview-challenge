import os
import time
from dotenv import load_dotenv
import requests
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
import re
from urllib.parse import urlparse
import json
from concurrent.futures import ThreadPoolExecutor

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Set up Google Generative AI API
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=GEMINI_API_KEY
)


def first_prompt():
    """"
    This will be the first prompt or instruction so the ai can understand the command properly
    """
    prompt = f"""
    You are an AI assistant specialized in web scraping instructions.
    Convert natural language prompts into useful and simple information, just simple one paragraph.
    I will give you some URL and question about the company so answer it without the URL and question.
    
    If you can't find certain information, indicate with "Not found".
    """
    
    try:
        print()
        response = llm.invoke(prompt)
        time.sleep(1)
        response_text = response.content
        
        print(response_text)
        
        
        
    except Exception as e:
        print(f"Error first prompt section")
        return {
            "section": "First Prompt",
            "error": str(e)
        }

def prompt_company_info(url, question, html_content=None):
    """
    Extract info with question for company information from a website using Google's Generative AI
    """
    # if html_content is None:
    #     html_content = fetch_website_content(url)
    
    # if not html_content:
    #     return {
    #         "url": url,
    #         "domain": extract_domain(url),
    #         "company_name": None,
    #         "error": "Failed to fetch content"
    #     }
    
    # # Use a smaller portion of the HTML to avoid token limits
    # truncated_html = html_content[:15000]  # First 15K characters
    
    prompt = f"""
    1 sentence simple answer.
    Website URL: {url}
    Question: {question}
    """
    
    try:
        print(url, question)
        time.sleep(2)
        response = llm.invoke(prompt)
        time.sleep(2)
        response_text = response.content
        return response_text
    
    except Exception as e:
        print(f"Error prompt company info section")
        return {
            "section": "Promt Company Info",
            "error": str(e)
        }

if __name__ == "__main__":
    first_prompt()