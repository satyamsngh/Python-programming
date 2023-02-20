def getNumberOfDays(month_name):
    if( month_name.lower() == 'feb'):
        return 28
    if( month_name.lower() in ['jan','mar','may','jul','aug','oct','dec']):
        return 31
    else:
        return 30

def getDate( day ):
    if day == 1:
        return '     1'
    elif len(str(day)) == 1:
        return '  '+str(day)
    else:
        return ' '+str(day)

calendar_rows = []
month = 'feb'
current_row = ''
for i in range(1,getNumberOfDays(month)+1):
    if i % 7 == 0:
        calendar_rows.append(current_row)
        current_row = getDate(i)
    else:
        current_row = current_row+getDate(i)
    
    if i == getNumberOfDays(month):
        calendar_rows.append(current_row)
        current_row = ''
print(calendar_rows)

for i in calendar_rows:
    print(i)

    


#  * 
# * *
#  * 

#     *  
#   *   * 
#  *     *
#   *   * 
#     *  






#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31  



#  a1b9b7


