bill=100
tip_percent=10
people=2

tip=bill*tip_percent/100
total=bill+tip
each=total/people

print("Bill:      ", bill)
print("Tip:       ", round(tip, 2))
print("Total:     ", round(total, 2))
print("Each pays: ", round(each, 2))