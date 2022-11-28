<template>
  <div class="card" @click="goDetail(movieranklist.tv_id)">
    <p v-if="!movieranklist.poster_path"></p>
    <img :src="movieranklist.poster_path" class=""
      alt="..."
      style="width : 270px; height : 350px"/>
    <div class="card-body">{{movieranklist.name}}</div>
  </div>
</template>

<script>
export default {
  name : 'TVRankListItem',
  props : {
    movieranklist : Object,
  },
  methods : {
    goDetail(id){
      this.$router.push({name :'detail', params : {id:id, media_type:'tv'}})
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