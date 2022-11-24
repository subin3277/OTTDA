<template>
  <div id="container">
    <h2>게시물</h2>
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
            <th>내용</th>
            <td><textarea v-model="cont" ref="cont"></textarea></td>
          </tr>
        </table>
      </form>
    </div>

    <div class="btnWrap">
      <a href="javascript:;" @click="golist" class="btn">목록</a>
      <a href="javascript:;" @click="update" class="btnAdd btn">수정</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "UpdateArticle",
  data() {
    return {
      subject : '',
      cont : '',
      detail : []
    }
  },
  methods : {
    golist(){
      this.$router.push({name:'article'})
    },
    update(){
      // const url = "http://127.0.0.1:8000/api/v1/articles/"
      const url = `${this.$store.state.url}`+"api/v1/articles/"
      axios({
        url : url + this.detail.id + '/',
        method : 'put',
        data : {
          title : this.subject,
          content : this.cont,
          user : this.detail.user
        },
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        alert('게시글을 수정하였습니다.')
        this.$router.push({name : 'articledetail', params : {id:this.detail.id}})
      })
      .catch((err) => {
        console.log(err)
        alert('게시글 수정에 실패하였습니다.')
      })
    }
  },
  created() {
    this.detail = this.$route.params.detail
    this.subject = this.detail.title
    this.cont = this.detail.content
  }
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
