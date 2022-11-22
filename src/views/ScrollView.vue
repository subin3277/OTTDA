<template>
  <div
    id="scroll"
    style="
      background-color: #a3e1f4;
      min-width: 100vw;
      height: 100vw;
      margin-left: calc(-50vw + 50%);
    "
  >
    <img
      src="../assets/logo_full.png"
      alt=""
      style="width: 500px; margin-left: auto; margin-right: auto;"
      @click="doanimate($event.target)"
    />
  </div>
</template>

<script>
export default {
  name: "ScrollView",
  methods: {
    doanimate(target) {
      target.setAttribute(
        "style",
        "animation : slide-out-bck-top 2s cubic-bezier(0.550, 0.085, 0.680, 0.530); width:500px"
      )
      const thi = this.$router
      setTimeout(function () {
        const cont = document.getElementsByClassName('container')
        cont.setAttribute('style','display:block')
        thi.push({ name: "main" })
      }, 2000)
    },
  },
}
</script>

<style>
.container {
  display: block;
}
#logo {
  display: flex;
}
</style>
