from typing import List

def numUniqueEmails(emails: List[str]) -> int:
    unique_emails = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        unique_emails.add(local + '@' + domain)
    return len(unique_emails)

print(numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob@leetcode.com", "testemail.david@lee.tcode.com"]))