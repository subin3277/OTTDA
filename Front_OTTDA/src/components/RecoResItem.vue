<template>
  <div style="width:100%">
    <div v-if="ottlist.length === 0">
      해당하는 OTT가 없습니다.
    </div>
    <div v-else>
      <div id="item">
        <div v-for="(lst, idx) in ottlist" :key=idx style=" height:170px; width:150px; background-color:#fdf5c7; border:1px solid black; border-radius:10px">
          <div style="margin: 50% 0px; ">
            {{lst}} 
          </div>
        </div>
        <div style="height:170px">
          <div style="margin: 50% 0px;">
            = <span style="font-family:cafe">{{price}}</span> 원 / 인당
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name : 'RecoResItem',
  props: {
    ottlist : Array,
    price : Number
  }
}
</script>

<style>
  #item {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    text-align: center;
    font-size: 20px;
    font-family:cafeair;

  }

</style>