<template>
  <div>
    <div id="detail_description">
      <img :src = "detail.poster_path" style="width:200px ; margin: 20px 10px 20px 30px">
      <div style="margin-left:10px; margin-top:20px">
        <h1 v-if="type==='movie'">{{detail.title}}</h1>
        <h1 v-else-if="type==='tv'">{{detail.name}}</h1>
        <p>{{detail.overview}}</p>
        <p>개봉일 : {{detail.release_date}}</p>
      </div>
    </div>

    <h2>시청가능한 OTT</h2>
    <p v-if="!outtlist"> {{message}} </p>
    <DetailOTTList v-for="(ott, idx) in ottlist" :key=idx :ottlst="ott"/>
    
    <h2 style="margin-top : 30px">리뷰</h2>
    <div @click="gocreatereview">리뷰 작성하기</div>
    
    <div id="review">
        <ReviewListItem v-for="(review, idx) in reviewlist" :key="idx" :review="review"/>
    </div>

    
    
  </div>
</template>

<script>
import axios from 'axios'
import DetailOTTList from '../components/DetailOTTList.vue'
import ReviewListItem from '../components/ReviewItem.vue'

export default {
  name: "SearchView",
  data() {
    return {
      ottlist : null,
      message : "시청가능한 OTT가 없습니다!",
      detail : null,
      type : null,
      reviewlist : null,
    }
  },
  components: {
    DetailOTTList,
    ReviewListItem
  },
  methods : {
    getOTT(id, type){
      console.log(id, type)
      let url = "http://127.0.0.1:8000/movies/"
      this.type = type
      if (type === 'movie') {
        url = url + 'movieprovider/' 
      } 
      else if (type === 'tv') {
        url = url + 'tvprovider/'
      }
      axios({
        url: url+id+'/',
        method : 'get',
      })
      .then((res) => {
        this.ottlist = res.data
        this.message = ""
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getDetail(id, type){
      let url = "http://127.0.0.1:8000/movies/"
      this.type = type
      if (type === 'movie') {
        url = url + 'moviedetail/' 
      } 
      else if (type === 'tv') {
        url = url + 'tvdetail/'
      }
      axios({
        url: url+id+'/',
        method : 'get' 
      })
      .then((res) => {
        console.log(res.data)
        this.detail = res.data[0]
      })
      .catch((err) => {
        console.log(err)
      })
    },
    gocreatereview(){
      let data = {}
      if(this.type === 'movie'){
        data = {
          id : this.detail.movie_id,
          title : this.detail.title,
          media_type : this.type
        }
      }
      else {
        data = {
          id : this.detail.tv_id,
          title : this.detail.name,
          media_type : this.type
        }
      }
      this.$router.push({name:'createreview', params:data})
    },
    getreview(id){
      const url = "http://127.0.0.1:8000/reviews/reviewsearch/"
      axios({
        url : url + id,
        method : 'get',
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
      .then((res) => {
        this.reviewlist = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    this.getOTT(this.$route.params.id, this.$route.params.media_type)
    this.getDetail(this.$route.params.id, this.$route.params.media_type)
    this.getreview(this.$route.params.id)
  }
}
</script>

<style>
/* #wrap {
  display: flex;
}
*/
#review {
  display: flex;
  flex-direction: row;
  overflow: scroll;
} 

#detail_description{
  display: flex;
  justify-content: flex-start;
}

#detail_description p{
  font-family: cafeair;
  text-align: start;
}
#detail_description h1{
  text-align: start;
}

@font-face {
  font-family: "cafeair";
  src: url("@/assets/fonts/Cafe24SsurroundAir.ttf");
}
</style>
