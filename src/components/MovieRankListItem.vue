<template>
  <div class="card" @click="goDetail(movieranklist.movie_id)">
    <p v-if="!movieranklist.poster_path">로딩 중.......</p>
    <img :src="movieranklist.poster_path" class=""
      alt="..."
      style="width : 270px; height : 350px"/>
    <div class="card-body">{{movieranklist.title}}</div>
  </div>
</template>

<script>
export default {
  name : 'MovieRankListItem',
  props : {
    movieranklist : Object,
  },
  methods : {
    goDetail(movie_id){
      this.$router.push({name :'detail', params : {movie_id}})
    }
  }
}
</script>

<style>
#carditem {
  text-align: center;
  display: flex;
  flex-flow:row nowrap;
  justify-content: center;
  margin : 0px 20px
}
</style>