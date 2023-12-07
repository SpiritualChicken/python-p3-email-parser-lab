# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
        self.email_addresses = str(email_addresses)
    
    def parse(self):
        matches = self.email_regex.findall(self.email_addresses)

        unique_addresses = sorted(set(matches))
        return unique_addresses

parser = EmailAddressParser("talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"]