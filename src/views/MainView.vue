<template>
  <div>
    <h1>인기 차트</h1>
    <MovieRankList/>
  </div>
</template>

<script>
import MovieRankList from '../components/MovieRankList'

export default {
  name: "MainView",
  components: {
    MovieRankList

  },
}
</script>

<style>
</style>
