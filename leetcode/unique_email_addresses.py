"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
"""


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dic = {}

        for email in emails:
            start = 0
            end = len(email)-1
            s = e = ""
            end_hit = start_hit = s_hit = False
            
            while not end_hit or not s_hit:
                ender = email[end]
                starter = email[start]
                
                if ender == '@':
                    end_hit = True
                    
                elif not end_hit:
                    e=e+ender
                    
                if starter == '@':
                    s_hit = True                    

                if starter == '+' and not start_hit:
                    start_hit = True

                elif starter != '.' and not start_hit and not s_hit:
                    s = s + starter

                start += 1   
                end -= 1

            s = s + e

            if s not in dic.keys():
                dic[s] = 1

        return len(dic.keys())