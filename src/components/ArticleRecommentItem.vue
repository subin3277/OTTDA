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
            <td>{{ lst.user_nickname }}</td>
            <td>{{ lst.content }}</td>
          </tr>
        </table>
      </div>

      <template v-if="recommentcreate">
        <RecommentCreateItem :commentid ="comment.id"/>
      </template>
    </td>
  </div>
</template>

<script>
import axios from "axios"
import RecommentCreateItem from '../components/RecommentCreateItem'

export default {
  name: "ArticleRecommentItem",
  props: {
    comment: Object,
  },
  components : {
    RecommentCreateItem
  },
  data() {
    return {
      recomment: [],
      recommentcreate : false,
    }
  },
  methods: {
    getrecomment() {
      const url = "http://127.0.0.1:8000/api/v1/comments/"
      console.log(this.comment)
      axios({
        url: url + this.comment.id,
        method: "get",
        headers : {
          Authorization: `Bearer ${this.$store.state.user.token}`
        }
      })
        .then((res) => {
          this.recomment = res.data.recomment_set
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

<style></style>
