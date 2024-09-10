contact = {}    # dict

while True:
    print('--------전화번호부 프로그램----------')
    print('1.추가  2.조회  3.검색  4.수정  5.삭제  9.종료')
    menu = int(input('메뉴를 선택해주세요.(숫자 only) : '))

    if menu == 1: # 연락처 추가
        print('연락처를 추가합니다.')
        new_name = input('이름 : ')
        new_tel = input('전화번호 : ')
        #print(new_name, new_tel)

        contact[new_name] = new_tel       # contact(dict)의 new_name(key)에 new_tel(value)를 반영. 
        contact.setdefault(new_name, new_tel)     # setdefault : 기존에 값이 존재하면 기존값을 덮어쓰기하지 않는다.
    
    
    elif menu == 2: # 연락처 조회
        print('연락처를 조회합니다.')
        #print(contact)
        for name, tel in contact.items():      # items : key, values 같이 가져오는 거
            print(name, ':', tel)

    
    elif menu == 3: # 연락처 검색
        print('연락처를 검색합니다.')
        search_name = input('검색 이름: ')

        try:
            print(contact[search_name])
        except:
            print('없는 이름입니다.')
        # print(contact.get(searct_name, '없는 이름입니다.'))      # index는 없을 경우 오류 발생하나, get은 오류 미발생
        

    elif menu == 4: # 연락처 수정
        print('연락처를 수정합니다.')

        try:
            mod_name = input('수정 이름 : ')
            mod_tel = input('새 전화번호: ')
            contact[mod_name] = mod_tel
        except:
            print('등록되지 않은 이름입니다.')

    elif menu == 5: # 연락처 삭제
        print('연락처를 삭제합니다.')
        del_name = input('삭제 이름 : ')

        try:
            del contact[del_name]
            print('연락처 삭제가 완료되었습니다.')

        except:
            print('등록되지 않은 이름입니다.')
    
    elif menu == 9: # 프로그램 종료
        print('프로그램을 종료합니다.')
        break

    else :
        print('잘못된 입력입니다.')