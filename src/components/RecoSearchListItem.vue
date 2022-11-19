<template>
  <div id="searchitem">
    <span style="margin-left:5px">{{searchItem}}</span>
    <div>x</div>
  </div>
</template>

<script>
export default {
  name : 'RecoSearchListItem',
  props : {
    searchItem : String
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