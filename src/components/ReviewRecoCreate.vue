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
  name: "ReviewRecoCreate",
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
      // const url = "http://127.0.0.1:8000/reviews/comments/"
      const url = `${this.$store.state.url}`+"reviews/comments/"
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
          this.$parent.getrecomment()
          this.inputdata = ""
          alert("등록되었습니다.")
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style>
