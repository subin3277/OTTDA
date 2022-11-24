<template>
  <div>
    <h3 style="margin:20px">Movie</h3>
    <b-carousel
      id="carousel-1"
      :interval="4000"
      controls
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333; width :100% "
    >
      <b-carousel-slide v-for="i in 5" :key=i>
        <template #img>
          <div id="rankmovie">
            <MovieRankListItem :movieranklist="rankmovie[i*3-3]" />
            <MovieRankListItem :movieranklist="rankmovie[i*3-2]" />
            <MovieRankListItem :movieranklist="rankmovie[i*3-1]" />
          </div>
        </template>
      </b-carousel-slide>
    </b-carousel>

    <br>

    <h3 style="margin:20px">TV</h3>
    <b-carousel
      :interval="4000"
      controls
      img-width="1024"
      img-height="480"
      
    >
      <b-carousel-slide v-for="i in 5" :key=i>
        <template #img>
          <div id="rankmovie">
            <TVRankListItem :movieranklist="ranktv[i*3-3]" />
            <TVRankListItem :movieranklist="ranktv[i*3-2]" />
            <TVRankListItem :movieranklist="ranktv[i*3-1]" />
          </div>
        </template>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
import MovieRankListItem from "../components/MovieRankListItem"
import TVRankListItem from "../components/TVRankListItem"
import axios from "axios"

export default {
  name: "MovieRankList",
  components: {
    MovieRankListItem,
    TVRankListItem,
  },
  data() {
    return {
      rankmovie: [],
      ranktv : [],
      i:0
    }
  },
  methods: {
    getMovieRank() {
      // const url = "http://52.196.3.18:8000/movies/"
      const url = `${this.$store.state.url}`+"movies/"
      axios({
        url: url,
        method: "get",
      })
        .then((res) => {
          console.log()
          this.rankmovie = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    },

    getTvRank() {
      // const url = "http://52.196.3.18:8000/movies/"
      const url = `${this.$store.state.url}`+"movies/tv/"
      axios({
        url: url,
        method: "get",
      })
        .then((res) => {
          console.log()
          this.ranktv = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created() {
    this.getMovieRank()
    this.getTvRank()
  },
}
</script>

<style>
#rankmovie {
  text-align: center;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
}

.sr-only {
  display: none;
}

.carousel-contro-next {
  background-color: black;
}
</style>
