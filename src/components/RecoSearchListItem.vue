<template>
  <div id="searchitem" style="width:500px">
    <span style="margin-left:5px">{{searchItem.title}}</span>
    <!-- <span style="margin-left:5px">{{searchItem.id}}</span> -->
    <div>x</div>
  </div>
</template>

<script>
export default {
  name : 'RecoSearchListItem',
  props : {
    searchItem : Object
  }
}
</script>

<style>
#searchitem {
  
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