<template>
  <div id="container">
    <h2>리뷰 등록</h2>
    <div class="AddWrap">
      <form>
        <table class="tbAdd">
          <colgroup>
            <col width="15%" />
            <col width="*" />
          </colgroup>
          <tr>
            <th>제목</th>
            <td><input type="text" v-model="subject" ref="subject" /></td>
          </tr>
          <tr>
            <th>별점</th>
            <td><star-rating :increment="0.5" v-model="star"></star-rating></td>
          </tr>
          <tr>
            <th>영화</th>
            <td><input type="text" v-model="movie" disabled="true" /></td>
          </tr>
          <tr>
            <th>내용</th>
            <td><textarea v-model="cont" ref="cont"></textarea></td>
          </tr>
        </table>
      </form>
    </div>

    <div class="btnWrap">
      <a href="javascript:;" @click="golist" class="btn">목록</a>
      <a href="javascript:;" @click="createarticle" class="btnAdd btn">등록</a>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import StarRating from "vue-star-rating"

export default {
  name: "CreateReview",
  components: {
    StarRating,
  },
  data() {
    return {
      subject: "",
      cont: "",
      movie: "",
      id: "",
      star: "",
      type: "",
    }
  },
  methods: {
    golist() {
      this.$router.push({ name: "review" })
    },
    createarticle() {
      // const url = "http://127.0.0.1:8000/reviews/reviews/"
      const url = `${this.$store.state.url}`+"reviews/reviews/"
      axios({
        url: url,
        method: "post",
        data: {
          title: this.subject,
          content: this.cont,
          user: this.$store.state.user.id,
          movie_title: this.movie,
          star: this.star,
          movie_id: this.id,
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.user.token}`,
        },
      })
        .then(() => {
          alert("게시물이 등록되었습니다.")
          this.$router.push({
            name: "detail",
            params: { id: this.id, media_type: this.type },
          })
          this.subject = ""
          this.content = ""
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.movie = this.$route.params.title
    this.id = this.$route.params.id
    this.type = this.$route.params.media_type
  },
}
</script>

<style scoped>
#container {
  width: 800px;
  margin: 0 auto;
}
table {
  width: 100%;
  border-collapse: collapse;
}
.tbAdd {
  border-top: 1px solid #888;
}
.tbAdd th,
.tbAdd td {
  border-bottom: 1px solid #eee;
  padding: 5px 0;
}
.tbAdd td {
  padding: 10px 10px;
  box-sizing: border-box;
}
.tbAdd td input {
  width: 100%;
  min-height: 30px;
  box-sizing: border-box;
  padding: 0 10px;
}
.tbAdd td textarea {
  width: 100%;
  min-height: 300px;
  padding: 10px;
  box-sizing: border-box;
}
.btnWrap {
  text-align: center;
  margin: 20px 0 0 0;
}
.btnWrap a {
  margin: 0 10px;
}
.btnAdd {
  background: #a3e1f4;
}
.btnDelete {
  background: #f00;
}
</style>
