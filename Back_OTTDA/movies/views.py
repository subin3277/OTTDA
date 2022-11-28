from rest_framework.response import Response
from rest_framework.decorators import api_view

from reviews.models import Review
from reviews.serializers import ReviewSerializer

import requests
import re

from itertools import combinations
# Create your views here.


# tmdb popular movie
API_URL = 'https://api.themoviedb.org/3'
API_KEY = 'fc0ec63c4ac115e88711e01e6be3aee1'


# 메인 화면에 들어갈 인기영화
def popularMovie():

    content_list = []    
    for n in range(1, 6):
        num = str(n)
        POPULAR_MOVIE_URL = f"{API_URL}//movie/popular?api_key={API_KEY}&region=KR&language=ko-KR&page={num}"
        popularMovieData = requests.get(POPULAR_MOVIE_URL)
        resPopularMovieDatas = popularMovieData.json().get('results')

        for resPopularMovieData in resPopularMovieDatas:
            popular_movie_id = resPopularMovieData.get('id')
            popular_movie_poster_path = "https://image.tmdb.org/t/p/original"+ resPopularMovieData.get('poster_path', "")
            popular_movie_title = resPopularMovieData.get('title')

            check = re.compile('[가-힣a-zA-Z0-9,:!?;#]')
            if check.match(popular_movie_title) :
                content = {"multi_id":popular_movie_id, "poster_path":popular_movie_poster_path, "title":popular_movie_title}
                content_list.append(content)
    return content_list

@api_view(["GET"])
def popular_movie_json(request):
    
    movies = popularMovie()
    return Response(movies)

            
def popularTV():
    
    content_list = []    
    for n in range(1,2):
        num = str(n)
        POPULAR_TV_URL = f"{API_URL}/tv/popular?api_key={API_KEY}&language=ko-KR&page={num}"
        popularTVData = requests.get(POPULAR_TV_URL)
        resPopularTVDatas = popularTVData.json().get('results')

        for resPopularTVData in resPopularTVDatas:
            popular_tv_id = resPopularTVData.get('id')
            popular_tv_poster_path = "https://image.tmdb.org/t/p/original"+ resPopularTVData.get('poster_path')
            popular_tv_name = resPopularTVData.get('name')

            check = re.compile('[가-힣a-zA-Z0-9,:!?;#]')
            if check.match(popular_tv_name) :
                content = {"tv_id":popular_tv_id, "poster_path":popular_tv_poster_path, "name":popular_tv_name}
                
                content_list.append(content)
    return content_list
    
@api_view(["GET"])
def popular_tv_json(request):
    
    tvs = popularTV()
    return Response(tvs)


# 영화 OTT (Movie Providers) 목록
def movieProvider(movie_id):

    content_list = []    

    MOVIE_PROVIDER_URL = f"{API_URL}/movie/{movie_id}/watch/providers?api_key={API_KEY}"
    movieProviderData = requests.get(MOVIE_PROVIDER_URL)
    resmovieProviderKoreaDatas = movieProviderData.json().get('results')

    resmovieProviderFlatrateDatas = resmovieProviderKoreaDatas.get('KR')
    resmovieProviderDatas = resmovieProviderFlatrateDatas.get('flatrate')

    for resmovieProviderData in resmovieProviderDatas:
        movie_provider_id = resmovieProviderData.get('provider_id')
        movie_provider_logo_path = "https://image.tmdb.org/t/p/original"+ resmovieProviderData.get('logo_path', "")
        movie_provider_name = resmovieProviderData.get('provider_name')

        content = {"provider_id":movie_provider_id, "logo_path":movie_provider_logo_path, "provider_name":movie_provider_name}
        content_list.append(content)

    return content_list

@api_view(["GET"])
def movie_provider_json(request, movie_id):
    
    movie_providers = movieProvider(movie_id)
    return Response(movie_providers)


# TV OTT (Movie Providers) 목록
def tvProvider(tv_id):

    content_list = []    

    TV_PROVIDER_URL = f"{API_URL}/tv/{tv_id}/watch/providers?api_key={API_KEY}"
    
    tvProviderData = requests.get(TV_PROVIDER_URL)
    restvProviderKoreaDatas = tvProviderData.json().get('results')

    restvProviderFlatrateDatas = restvProviderKoreaDatas.get('KR')
    restvProviderDatas = restvProviderFlatrateDatas.get('flatrate')

    for restvProviderData in restvProviderDatas:
        tv_provider_id = restvProviderData.get('provider_id')
        tv_provider_logo_path = "https://image.tmdb.org/t/p/original"+ restvProviderData.get('logo_path', "")
        tv_provider_name = restvProviderData.get('provider_name')

        content = {"provider_id":tv_provider_id, "logo_path":tv_provider_logo_path, "provider_name":tv_provider_name}
        content_list.append(content)

    return content_list

@api_view(["GET"])
def tv_provider_json(request, tv_id):
    
    tv_providers = tvProvider(tv_id)
    return Response(tv_providers)

# 영화 검색하기
def searchMulti(title):

    content_list = []    
    for n in range(1, 6):
        num = str(n)
        SEARCH_MULTI_URL = f"{API_URL}/search/multi?api_key={API_KEY}&language=ko-KR&query={title}&page={num}"
        searchMultiData = requests.get(SEARCH_MULTI_URL)
        resSearchMultiDatas = searchMultiData.json().get('results')
        for resSearchMultiData in resSearchMultiDatas:
            search_multi_id = resSearchMultiData.get('id')
            search_multi_poster_path = "https://image.tmdb.org/t/p/original"+ str(resSearchMultiData.get('poster_path'))
            if resSearchMultiData.get('media_type') == 'movie':
                title = resSearchMultiData.get('title')
            elif resSearchMultiData.get('media_type') == 'tv':
                title = resSearchMultiData.get('name')
            else:
                continue
            content = {"multi_id":search_multi_id, "poster_path":search_multi_poster_path, "title":title, "media_type" : resSearchMultiData.get('media_type')}
            content_list.append(content)

    return content_list

@api_view(["GET"])
def search_multi_json(request, title):
    multi = searchMulti(title)
    return Response(multi)


# 영화상세페이지
def movieDetail(movie_id):

    content_list = []

    DETAIL_MOVIE_URL = f"{API_URL}/movie/{movie_id}?api_key={API_KEY}&language=ko-KR"
    detailMovieData = requests.get(DETAIL_MOVIE_URL)
    detail_movie_id = detailMovieData.json().get('id')
    detail_movie_title = detailMovieData.json().get('title')
    detail_movie_poster_path = "https://image.tmdb.org/t/p/original"+ detailMovieData.json().get('poster_path')
    detail_movie_overview = detailMovieData.json().get('overview')
    detail_movie_release_date = detailMovieData.json().get('release_date')
    detail_movie_runtime = detailMovieData.json().get('runtime')
    
    detailMovieGenres = detailMovieData.json().get('genres')
    genres_list = []
    for detailMovieGenre in detailMovieGenres:
        detail_movie_genres = detailMovieGenre.get('name')
        genres_list.append(detail_movie_genres)

    content = {"movie_id":detail_movie_id, "title":detail_movie_title, "poster_path":detail_movie_poster_path, "overview":detail_movie_overview, "release_date":detail_movie_release_date, "runtime":detail_movie_runtime, "genres":genres_list}
    content_list.append(content)

    return content_list

@api_view(["GET"])
def movie_detail_json(request, movie_id):
    detail = movieDetail(movie_id)
    return Response(detail)


# TV상세페이지
def tvDetail(tv_id):

    content_list = []

    DETAIL_TV_URL = f"{API_URL}/tv/{tv_id}?api_key={API_KEY}&language=ko-KR"
    detailTVData = requests.get(DETAIL_TV_URL)
    detail_tv_id = detailTVData.json().get('id')
    detail_tv_name = detailTVData.json().get('name')
    detailTVGenres = detailTVData.json().get('genres')
    genres_list = []
    for detailTVGenre in detailTVGenres:
        detail_tv_genres = detailTVGenre.get('name')
        genres_list.append(detail_tv_genres)
    
    detail_tv_poster_path = "https://image.tmdb.org/t/p/original"+ detailTVData.json().get('poster_path')
    detail_tv_overview = detailTVData.json().get('overview')
    content = {"tv_id":detail_tv_id, "name":detail_tv_name, "poster_path":detail_tv_poster_path, "overview":detail_tv_overview, "genres":genres_list}
    content_list.append(content)

    return content_list

@api_view(["GET"])
def tv_detail_json(request, tv_id):
    detail = tvDetail(tv_id)
    return Response(detail)

@api_view(['POST'])
def recoott(request):
    가격표 = {
    "Netflix" : [9500,13500,-1,17000],
    "Watcha" : [7900, -1, -1, 12900],
    "wavve" : [7900, 10900, -1, 13900],
    "Disney Plus" : [-1, -1, -1, 9900],
    "Netflix basic with Ads" : [5500, -1, -1, -1]
    }
    ott = ['Netflix', 'wavve', 'Watcha', 'Disney Plus', 'Netflix basic with Ads']
    data = request.data
    movielist = data['movie'] # 보고 싶은 것들

    tmpmustott = []
    adi = {}

    for movie in movielist:
        ottname = movie['id']
        if movie['media_type'] == "movie":
            ottservice = movieProvider(ottname) # 어떤 영화가 서비스하고 있는 모든 곳
            # movieProvider ott 리스트로 받아옴
            lst = []
            for thatott in ottservice :
                lst.append(thatott['provider_name']) # tmp 형식. ott 이름
            adi[movie["id"]] = lst
            # tmpmustott.append(lst)
        elif movie['media_type'] == "tv":
            ottservice = tvProvider(ottname)
            lst = []
            for thatott in ottservice :
                lst.append(thatott['provider_name'])
            adi[movie["id"]] = lst
            tmpmustott.append(lst)
    # adi 는 영화 id로 해당 id가 서비스 가능한 ott name을 문자열로 보유중
    v = {ot : set() for ot in ott}
    for movie_id in adi:
        ottnames = adi[movie_id]
        for ottname in ottnames:
            v[ottname].add(movie_id)
    nowcost = [1000000, 1000000, 1000000, 1000000]
    subli = [(), (), (), ()]
    for i in range(1, 6):
        for j in combinations(ott, i):
            nset = set()
            val = [0, 0, 0, 0]
            for k in j:
                nset = nset|v[k]
                for l in range(4):
                    prce = 가격표[k][l]
                    val[l] += prce
            if len(nset) != len(movielist):
                continue
            # print(f"ott 가입 해야하는 곳들 : {j}")
            # print(f"볼 수 있는 서비스들 : {nset}")
            # print(f"그 가격들 : {val}")
            for idx in range(4):
                cost = val[idx]
                if nowcost[idx] < cost or val[idx]%100:
                    continue
                nowcost[idx] = cost
                subli[idx] = j
    context = {}
    for n in range(1, 5):
        context[n] = nowcost[n-1]/n
        print(f"{n}인: {nowcost[n-1]/n}")
    # print(f"인당 가격 최솟값들 : {nowcost}")
    print(f"인당 ott 서비스 리스트들 : {subli}")
    context['list'] = subli

    return Response(context)

@api_view(['GET'])
def star_average_json(request, movie_id):
    reviews = Review.objects.filter(movie_id=movie_id)
    serializers = ReviewSerializer(reviews, many=True)
    star_sum = 0

    if len(serializers.data) == 0:
        res = {
            "star_avg": 0,
            "star_count": 0
        }
    else:
        for i in range(len(serializers.data)):
            if serializers.data[i].get('star') != 0:
                star_sum += serializers.data[i].get('star')
        star_avg = round(star_sum / len(serializers.data), 1)
        res = {
            "star_avg": star_avg,
            "star_count": len(serializers.data)

        }
    return Response(res)