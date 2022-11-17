<template>
  <div class="card">
    <p v-if="!movieranklist.poster_path"></p>
    <img :src="movieranklist.poster_path" class=""
      alt="..."
      style="width : 270px; height : 350px"/>
    <div class="card-body">{{movieranklist.name}}</div>
  </div>
</template>

<script>
export default {
  name : 'MovieRankListItem',
  props : {
    movieranklist : Object,
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