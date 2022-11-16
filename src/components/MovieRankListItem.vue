<template>
  <div id="carditem">
    <div class="card">
      <img src="@/assets/quokka.png"  class=""
        alt="..." />
      <div class="card-body">제목</div>
    </div>
    <div class="card">
      <img src="@/assets/quokka.png"  class=""
        alt="..." />
      <div class="card-body">제목</div>
    </div>
    <div class="card">
      <img src="@/assets/quokka.png"  class=""
        alt="..." />
      <div class="card-body">제목</div>
    </div>
  </div>
</template>

<script>
export default {
  name : 'MovieRankListItem'
}
</script>

<style>
#carditem {
  text-align: center;
  display: flex;
  flex-flow:row nowrap;
  justify-content: center;
}
</style>