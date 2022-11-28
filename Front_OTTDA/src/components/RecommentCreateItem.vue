<template>
  <div>
    <form @submit.prevent="createrecomment">
      <input
        type="text"
        @input="inputdata = $event.target.value"
        :value="inputdata"
      />
      <button>등록</button>
    </form>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "RecommentCreateItem",
  props: {
    commentid: String,
  },
  data() {
    return {
      inputdata: "",
    }
  },
  methods: {
    createrecomment() {
      // const url = "http://127.0.0.1:8000/api/v1/comments/"
      const url = `${this.$store.state.url}`+"api/v1/comments/"
      axios({
        url: url + this.commentid + "/recomments/",
        method: "post",
        data: {
          content: this.inputdata,
          user: this.$store.state.user.id
        },
        headers : {
          Authorization: `Bearer ${this.$store.state.user.token}`
        }
      })
        .then(() => {
          this.inputdata = ""
          alert("등록되었습니다.")
          this.$parent.getrecomment()
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
