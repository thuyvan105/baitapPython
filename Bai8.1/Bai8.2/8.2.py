def  append_middle ( s1 , s2 ):
    print ( "Chuỗi lệnh ban đầu là" , s1 , s2 )
    # only number between of s1
    mi  =  int ( len ( s1 ) / 2 )

    # get character from 0 to only number between from s1
    x  =  s1 [: mi :]
    # Nối s2 với nó
    x  +=  s2
    # Nối lại ký tự còn lại từ s1
    x  +=  s1 [ mi :]
    print ( "Sau khi thêm chuỗi mới vào giữa:" ,    x )

append_middle ( "abc" , "ccc" )
