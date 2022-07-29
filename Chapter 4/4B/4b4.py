import os
os.system('cls||clear')

# Code starts here

day = int(input())
month = input()

if month == 'december':
  astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
      
elif month == 'january':
   astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
         
elif month == 'february':
    astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
         
elif month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'Aries'
         
elif month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'Taurus'
         
elif month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'Gemini'
         
elif month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'Cancer'
         
elif month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'Leo'
         
elif month == 'august':
    astro_sign = 'Leo' if (day < 23) else 'virgo'
         
elif month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'Libra'
         
elif month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'Scorpio'
         
elif month == 'november':
    astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
         
         
print(f"Your Astrological sign is : {astro_sign}")

#-----Zodiac Sign------
#The horoscopes commonly reported in newspapers use the position of the sun at the time of one’s birth to 
#try and predict the future. This system of astrology divides the year into twelve zodiac signs, as outline 
#in the table below.
#Write a program that asks the user to enter his or her month number and day of birth. Then your program 
#should report the user’s zodiac sign as part of an appropriate output message.
