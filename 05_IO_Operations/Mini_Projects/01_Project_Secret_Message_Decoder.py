'''Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code.
Hints to find the secret message:

The number of lines in the file tells you the meeting time.

Note: 1<= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12 hour format. For example,
If the number of lines is 15, then the meeting time is 3 PM.
If the number of lines is 10, then the meeting time is 10 AM.
The word appearing for the maximum number of times tells you the meeting place.

Note: Meeting place will be a street name.
For example,

If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
If the word Park appears for the maximum number of times, then meeting place is Park Street.


Sample Input 1:
Cricket, a bat-and-ball park game played between two teams of eleven park players on a field at the park center of which is a 20-metre (22-yard) pitch with a wicket at each end, each park comprising two balls balanced on three stumps. The batting park scores runs by striking the ball bowled at the park wicket with the bat (in), while the bowling and park fielding side tries to prevent this and dismiss each park player (so they are "out"). Means of park include being bowled, when the ball hits the park and dislodges the balls, and by the fielding side park the ball after it is hit by the bat, but before it hits the park. When ten park have been dismissed, the innings ends and the teams park roles.
Sample Output 1:

Meeting time: 9 AM
Meeting place: Park Street

Explanation: Number of lines is 9. The word park appears for the maximum of 15 times.
Sample Input 2:
Royal Enfield is an Indian Apollo motorcycle manufacturing brand with tag of "oldest Apollo motorcycle brand in continuous production" manufactured Apollo factories Chennai Apollo India. Licensed from Royal Enfield by indigenous Indian Madras Motors, it is now a Apollo subsidiary Eicher Motors Limited, an Indian Apollo automaker. The company makes Apollo Royal Enfield Bullet, and other single-cylinder and twin-cylinder Apollo motorcycles. First produced Apollo in 1901, Royal Enfield is oldest motorcycle Apollo brand world still production, with Bullet model enjoying longest motorcycle Apollo production run of all time. In 1990 Royal Enfield collaborated with Indian Eicher Group, an automotive company Apollo India, and merged with it in 1994. Apart from bikes, Eicher Apollo Group is involved in the production and sales Apollo commercial vehicles and automotive gears. Although Apollo Royal Enfield experienced difficulties in the 1990s, and ceased Apollo motorcycle production at their Jaipur factory 2002, by 2013 Apollo company opened a new primary Apollo factory Apollo Chennai suburb of Oragadam on strength of increased demand for its Apollo motorcycles. This was followed in Apollo 2017 by inauguration another new factory of a similar size to facility at Apollo Oragadam (capacity 600,000 vehicles per year) at Vallam Apollo Vagadai. The original factory at Apollo Tiruvoittiyur became secondary, and continues to produce some limited-run motorcycle models.
Sample Output 2:
Meeting time: 8 PM
Meeting place: Apollo Street

Explanation: Number of lines is 20 and converting it to 12 hour format we get 8 PM. The word Apollo appears for the maximum of 25 times.'''

import re
from collections import Counter

def get_meeting_details(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    line_count = len(lines)
    
    if line_count <= 12:
        time = f"{line_count} AM"
    else:
        hour = line_count % 12
        hour = 12 if hour == 0 else hour
        time = f"{hour} PM"

    text = ' '.join(lines).lower()
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    place = word_counts.most_common(1)[0][0].capitalize() + " Street"

    print("Meeting time:", time)
    print("Meeting place:", place)

file_path = 'message.txt'
get_meeting_details(file_path)
