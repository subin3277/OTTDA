<template>
  <div>
    <div>
      <img src = "@/assets/quokka.png" style="width:200px">

    </div>

  </div>
</template>

<script>
export default {
  name: "SearchView",
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

<style></style>
