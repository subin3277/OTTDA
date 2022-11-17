<template>
  <div>
    <b-col>
      <div class="card" id="carditem" style="width: 300px" @click="goDetail">
        <img v-if="searchItem.poster_path == 'https://image.tmdb.org/t/p/originalNone'" src="../assets/quokka.png" style="width: 270px; margin-top: 10px">
        <img v-else
          :src="searchItem.poster_path"
          class=""
          alt="..."
          style="width: 270px; margin-top: 10px"
        />
        <div class="card-body">{{ searchItem.title }}</div>
      </div>
    </b-col>
  </div>
</template>

<script>
export default {
  name: "SearchResListItem",
  props: {
    searchItem: Object,
  },
  methods: {
    goDetail(movie_id) {
      this.$router.push({ name: "detail", params: { movie_id } })
    },
  },
}
</script>

<style>
#carditem {
  text-align: center;
  display: block;
  flex-flow: column nowrap;
  justify-content: center;
  margin: 0px 20px;
}
</style>
