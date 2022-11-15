<template>
  <div>
    <p>
      영상 제목
      <input type="text" style="width:500px"/>
      <button style="margin : 10px">검색</button>
    </p>

    <p>
      시청 인원
      <input type="checkbox" id="p_1" class="checkbox"/> <label for="p_1">1</label>
      <input type="checkbox" id="p_2" class="checkbox"/> <label for="p_2">2</label>
      <input type="checkbox" id="p_4" class="checkbox"/> <label for="p_4">4</label>
    </p>
    <button>추천받기</button>
  </div>
</template>

<script>
export default {
  name: "RecoView",
}
</script>

<style>
  .checkbox {
    margin-left: 15px;
  }

  label {
    margin : 10px;
  }
</style>
