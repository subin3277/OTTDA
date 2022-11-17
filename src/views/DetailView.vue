<template>
  <div>
    <div id="detail_description">
      <img src = "@/assets/quokka.png" style="width:200px ; margin:50px">
      <div style="margin-left:10px">
        <h1>제목</h1>
        <p>내용~~~~~~~~~~~~~~~~</p>
      </div>
    </div>

    <h2>시청가능한 OTT</h2>
    <DetailOTTList/>
  </div>
</template>

<script>
import DetailOTTList from '../components/DetailOTTList.vue'
export default {
  name: "SearchView",
  components: {
    DetailOTTList
  },
  methods : {
    getDetail(id){
      console.log(id)
    }
  },
  created() {
    this.getDetail(this.$route.params.movie_id)
  }
}
</script>

<style>
#detail_description{
  display: flex;
  text-align: center;
}

#detail_description p{
  font-family: cafeair;
}

@font-face {
  font-family: "cafeair";
  src: url("@/assets/fonts/Cafe24SsurroundAir.ttf");
}
</style>
