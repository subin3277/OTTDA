<template>
  <div id="searchitem" style="width:500px">
    <span style="margin-left:10px; font-family:cafeair; font-size:20px">{{searchItem.title}}</span>
    <!-- <span style="margin-left:5px">{{searchItem.id}}</span> -->
    <!-- <div @click="deletelist">x</div> -->
  </div>
</template>

<script>
export default {
  name : 'RecoSearchListItem',
  props : {
    searchItem : Object
  },
  methods : {
    deletelist() {
      this.$parent.minuslist(this.searchItem.title)
    }
  }
}
</script>

<style>
#searchitem {
  display: flex;
  justify-content: space-between;
  background-color: #FDF5C7;
  margin: 2px;
  padding: 2px;
}

#searchitem div {
  border: 1px solid black;
  padding : 2px 5px;
}
</style>