TEXT={'agree': """Yes, I agree. That sounds perfectly fine to me""",
      'busy':"""Sorry, can we do this later this week or next week?""",
      'upsell':"""Would you consider making this a monthly donation?"""}


import sys, pyperclip


if len(sys.argv)<2:
    print("Usage python clipboard.py [keyphrase] -copy phrase text")
    sys.exit()
keyphrase= sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"TEXT for the keyphrase has been copied to clipboard: {keyphrase}")
else:
    print("No text for the keyphrase")
