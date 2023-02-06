# requests 패키지 불러오기 (pip install requests 설치 필요)
import requests

# 네이버 영화 사이트 - 탑건: 매버릭 리뷰 페이지 
url = "https://movie.naver.com/movie/bi/mi/review.naver?code=81888"

# requests.get
resp = None