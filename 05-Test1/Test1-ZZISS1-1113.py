results= {i:0 for i in range(1,5)}

## program check
try:
    import p1
    assert p1.f(11) == "1234567891011"
    assert p1.f(4) == "1234"
    assert p1.f(15) == "123456789101112131415"
    results[1] = 1
except:
    pass

## program check
try:
    import p2
    assert p2.f(7,3,"+") == 10
    assert p2.f(7,3,"-") == 4
    assert p2.f(7,3,"*") == 21
    assert p2.f(7,3,"%") == 1
    assert p2.f(7,3,"**") == 343
    results[2] = 1
except:
    pass

## program check
try:
    import p3
    assert p3.f("+-+++-+---") == True
    assert p3.f("+-+-+-+-+-+-") == False
    assert p3.f("+-+-+-++-++-++----") == True
    assert p3.f("++--++--++--") == False
    results[3] = 1
except:
    pass

## program check
try:
    import p4
    assert p4.f(5) == 3
    assert p4.f(9) == 21
    assert p4.f(16) == 610
    results[4] = 1
except:
    pass

# Final results
print("\nTOTAL PTS:", sum(results.values()), results)
print()
#input("Press ENTER...")
