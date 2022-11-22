<template>
  <div>
    <th style="width: 10%">{{ comment.user }}</th>
    <td style="width: 90%">
      <div>
        {{ comment.content }}
        <img src="../assets/back-arrow.png" style="width:20px" @click="recommnetcreate">
      </div>

      <div class="listWrap">
        <table class="tbList">
          <colgroup>
            <col width = "10%"/>
            <col width='*'/>
          </colgroup>
          <tr class="comment-list-item" v-for="(lst, idx) in recomment" :key="idx">
            <td>{{ lst.user }}</td>
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
      const url = "http://127.0.0.1:8000/reviews/recomments/"
      console.log(this.comment)
      axios({
        url: url + this.comment.id,
        method: "get",
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
