<template>
  <div class="card" @click="goDetail(movieranklist.multi_id)">
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
    goDetail(id){
      console.log(id)
      this.$router.push({name :'detail', params : {id:id, media_type:'movie'}})
    }
  }
}
</script>

<style>
.card {
  --bs-card-border-radius : 1rem !important;
}
</style>