import time, rotatescreen as rs
pd = rs.get_primary_display()

angel = [90,180,270,0]

for i in range(5):
    for x in angel:
        pd.rotate_to(x)
        time.sleep