"""
@file
@brief Some automation helpers to grab mails from student about project.
"""
import re
import os
from pyquickhelper import noLOG, run_cmd, remove_diacritics


def grab_addresses(mailbox, subfolder, date, no_domain=False, fLOG=noLOG):
    """
    look for some emails in a mail box
    from specific emails or sent to specific emails

    @param      mailbox         MailBoxImap object (we assume you are logged in)
    @param      date            date (grab emails since ..., example ``1-Oct-2014``)
    @param      subfolder       folder of the mailbox to look into
    @param      no_domain       remove domain when searching for emails
    @param      fLOG            logging function
    @return                     list of emails
    """
    emails = mailbox.enumerate_mails_in_folder(
        subfolder, date=date, body=False)
    mid = {}
    res = []
    for mail in emails:
        tos = mail.get_to()
        tos = [(m[1].split('@')[0] if no_domain else m[1])
               for m in tos if m and m[1]]
        res.extend(tos)
    res = list(sorted(set(res)))
    return res
