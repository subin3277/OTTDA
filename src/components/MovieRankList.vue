<template>
  <div>
    <carousel>
      <slide>slide1</slide>
      <slide>slide2</slide>
      <slide>slide2</slide>
      <slide>slide2</slide>
      <slide>slide2</slide>
      <slide>slide2</slide>
    </carousel>
    <MovieRankListItem/>
    <!-- <div class="carousel slide" data-bs-ride="carousel">
      <div  class="carousel-inner">
        <div id="rankmovie" class="carousel-item active" >
          <MovieRankListItem />
        </div>
        
        <div class="carousel-item"></div>
        <div class="carousel-item"></div>
      </div>

      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleControls"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleControls"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div> -->
    
  </div>
</template>

<script>
import MovieRankListItem from "../components/MovieRankListItem"
import axios from "axios"

import {Carousel, Slide} from 'vue-carousel'

export default {
  name: "MovieRankList",
  components: {
    MovieRankListItem,
    Carousel,
    Slide
  },
  data() {
    return {
      rankmovie: [],
    }
  },
  methods: {
    getMovieRank() {
      // const url = "http://52.196.3.18:8000/movies/"
      const url = "http://127.0.0.1:8000/movies/"
      axios({
        url: url,
        method: "get",
      })
        .then((res) => {
          this.rankmovie = res
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created() {
    this.getMovieRank()
  },
}
</script>

<style>
#rankmovie {
  text-align: center;
  display: flex;
  flex-flow:row nowrap;
  justify-content: center;
}
</style>
