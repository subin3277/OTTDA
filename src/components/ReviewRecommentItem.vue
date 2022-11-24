<template>
  <div>
    <th style="width: 15%">{{ comment.user_nickname }}</th>
    <td style="width: 85%">
      <div>
        {{ comment.content }}
        <img src="../assets/back-arrow.png" style="width:20px" @click="recommnetcreate">
      </div>

      <div class="listWrap">
        <table class="tbList">
          <colgroup>
            <col width = "70px"/>
            <col width='*'/>
          </colgroup>
          <tr class="comment-list-item" v-for="(lst, idx) in recomment" :key="idx">
            <th>{{ lst.user_nickname }}</th>
            <td>{{ lst.content }}</td>
          </tr>
        </table>
      </div>

      <template v-if="recommentcreate">
        <ReviewCreateItem :commentid ="comment.id"/>
      </template>
    </td>
  </div>
</template>

<script>
import axios from "axios"
import ReviewCreateItem from '../components/ReviewRecoCreate'

export default {
  name: "ReviewRecommentItem",
  props: {
    comment: Object,
  },
  components : {
    ReviewCreateItem
  },
  data() {
    return {
      recomment: [],
      recommentcreate : false,
    }
  },
  methods: {
    getrecomment() {
      // const url = "http://127.0.0.1:8000/reviews/comments/"
      const url = "http://52.196.3.18:8000/reviews/comments/"
      console.log(this.comment)
      axios({
        url: url + this.comment.id,
        method: "get",
        headers : {
          Authorization: `Bearer ${this.$store.state.user.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.recomment = res.data.recomments
        })
        .catch((err) => {
          console.log(err)
        })
    },
    recommnetcreate() {
      this.recommentcreate = !this.recommentcreate
    },
  },
  created() {
    this.getrecomment()
  },
}
</script>

<style>
th {
  border-top : 0px !important
}
</style>
