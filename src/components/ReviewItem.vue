<template>
  <div >
    <b-card
        :header="review.title"
        header-text-variant="black"
        header-tag="header"
        header-bg-variant="#a3e1f4"
        header-class="header"
        style="width: 20rem; height: 20rem; margin:10px; background:#a3e1f470"
        :footer="review.user_nickname"
        footer-class="footer"
        body-class="class"
        @click="godetail(review.id)"
      >
        <b-card-text style="font-family:cafeair">
          <star-rating style="height:15px; margin:5px" :increment="0.5" v-model="star" read-only=true></star-rating>
          <span class="body">{{review.content}}</span>
        </b-card-text>
      </b-card>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
export default {
  name : 'ReviewItem',
  props : {
    review : Object
  },
  data(){
    return {
      star : 0,
    }
  },
  components : {
    StarRating,
  },
  methods : {
    
    godetail(id){
      this.$router.push({name : 'reviewdetail', params: {id}})
    }
  },
  created() {
    this.star = this.review.star
  }
}
</script>

<style>
.header {
  height: 60px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
.footer {
  height: 40px;
}
.body {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  margin-top: 25px;
}
</style>