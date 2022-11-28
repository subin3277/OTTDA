<template>
  <div style="background : #FDF5C7; margin:3px">
    <span id="list">
      <img :src="ottlst.logo_path" style="margin:10px">
      <span>{{ottlst.provider_name}}</span>
    </span>
  </div>
</template>

<script>
export default {
  name : 'DetailOTTList',
  props : {
    ottlst : Object
  }
}
</script>

<style>
#list {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
</style>