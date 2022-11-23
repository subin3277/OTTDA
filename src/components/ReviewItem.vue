<template>
  <div >
    <b-card
        :header="review.title"
        header-text-variant="black"
        header-tag="header"
        header-bg-variant="#a3e1f4"
        :title="review.star"
        style="width: 20rem; height: 20rem; margin:10px; background:#a3e1f470"
        :footer="review.user_nickname"
        @click="godetail(review.id)"
      >
        <b-card-text style="font-family:cafeair">{{review.content}}</b-card-text>
      </b-card>
  </div>
</template>

<script>
export default {
  name : 'ReviewItem',
  props : {
    review : Object
  },
  methods : {
    
    godetail(id){
      this.$router.push({name : 'reviewdetail', params: {id}})
    }
  }
}
</script>

<style>
</style>