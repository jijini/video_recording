import cv2
import numpy as np
import datetime

# 웹캠 객체 생성
cap = cv2.VideoCapture(0)

# 녹화용 옵션 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480), isColor=False)

# 현재 날짜와 시간을 이용하여 파일 이름 생성
now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d %H-%M-%S") + ".avi"

# 동영상 저장 경로 설정
save_path = "D:\python\ex230421" + filename


# 녹화 중인지 여부
recording = False

while True:
    # 카메라로부터 프레임 가져오기
    ret, frame = cap.read()
    
    # 프레임이 제대로 가져와졌는지 확인
    if not ret:
        break
    
    # 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 녹화 버튼 누르면 녹화 시작 또는 중지
    if cv2.waitKey(1) == ord('r'):
        if not recording:
            recording = True
            print('Recording started...')
            start_time = datetime.datetime.now()
            today = start_time.strftime('%Y-%m-%d %H-%M-%S')
            out = cv2.VideoWriter('recording_{}.avi'.format(today), fourcc, 20.0, (640, 480), isColor=False)
        else:
            recording = False
            end_time = datetime.datetime.now()
            print('Recording stopped. Elapsed time:', end_time - start_time)
            out.release()
            out = None
    
    # 녹화 중일 때만 프레임 저장
    if recording:
        out.write(gray)
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        cv2.putText(frame, today + ' ' + current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, 'recording', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, 'not recording', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # 영상 출력
    cv2.imshow('frame', frame)
    
    # 'quit'를 입력하면 종료
    if cv2.waitKey(1) == ord('q'):
        break
        
    # 'c'를 누르면 캡쳐
    if cv2.waitKey(1) == ord('c'):
        print
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        cv2.putText(gray, today + ' ' + current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imwrite('capture_{}_{}.png'.format(today, current_time), gray)

# 객체 해제
cap.release()
out.release()
cv2.destroyAllWindows()
