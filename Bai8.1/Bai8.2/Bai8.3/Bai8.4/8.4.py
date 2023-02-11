def  find_digits_chars_symbols ( sample_str ):
    char_count  =  0
    number_đếm  =  0
    icon_đếm  =  0
    cho  char  trong  sample_str :
        if  char . isalpha () :
            char_count  +=  1
         yêu tinh char . isdigit () :
            chữ_số  +=  1
        # nếu nó không phải là chữ cái hoặc chữ số thì đó là ký hiệu đặc biệt
        khác :
            icon_đếm  +=  1

    in ( "Ký tự =" , char_count , "Chữ số =" , chữ số_đếm , " Ký hiệu = " , ký hiệu_đếm )
sample_str  =  "A*45bc%^-bgBl<"   
print ( "tổng số đếm tắt ký tự, Chữ số và ký hiệu \n " )
find_digits_chars_symbols ( sample_str )
