# set pattern equal to this to extract the phone number : r"\d{3}.\d{3}.\d{4}"
# set pattern equal to this to extract the date: r"\d{4}.\d{2}.\d{2}" 
email_text = """
Hi Team,

Please note the following updates for our project:

1. The next meeting is scheduled for 2024-08-15 at our main office. Please confirm your availability.
2. We have received a new batch of feedback from clients. Some of the notable ones include:
   - "The service was excellent and the response time was quick."
   - "Please contact me at john.doe@example.com for further discussions."
3. Our support team can be reached at:
   - Phone: 123-456-7890 (John Doe)
   - Phone: 987-654-3210 (Jane Smith)
4. The project deadline has been moved to 2024-12-31. Ensure all deliverables are completed by then.
5. For any urgent issues, please email support@project.com or call our hotline at 555-123-4567.
6. The previous meeting minutes are available at 2023-07-25. Please review them before the next meeting.

Best regards,
Project Manager
"""
import re

pattern = r"\d{4}.\d{2}.\d{2}"
matches = re.findall(pattern, email_text)
print("dates: ", matches)

pattern = r"\b\d{3}.\d{3}.\d{4}\b"
matches = re.findall(pattern, email_text)
print("phone numbers: ", matches)

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
matches = re.findall(pattern, email_text)
print("email addresses: ", matches)





