<template>
  <div>
    <h1>게시판 상세보기</h1>

    <div class="AddWrap">
      <form>
        <table class="tbAdd">
          <colgroup>
            <col width="15%" />
            <col width="*" />
          </colgroup>
          <tr>
            <th>제목</th>
            <td>{{ detail.title }}</td>
          </tr>
          <tr>
            <th>작성자</th>
            <td>{{ detail.user_nickname }}</td>
          </tr>
          <tr>
            <th>작성일</th>
            <td>{{ detail.created_at.substring(0, 10) }}</td>
          </tr>
          <tr>
            <th>내용</th>
            <td class="txt_cont" v-html="detail.content"></td>
          </tr>
          <tr v-if="this.$store.state.user.id === detail.user">
            <th></th>
            <td style = "text-align:right !important">
              <div>
                <span style="margin-right : 20px" @click="updatearticle">수정</span>
                <span style="margin-right : 20px" @click="deletearticle">삭제</span>
              </div>
            </td>
          </tr>
          <tr>
            <th>댓글</th>
            <div>
              <th>{{ comment_count }}개의 댓글이 있습니다.</th>
            </div>
            <ArticleRecommentItem v-for="(comment, idx) in detail.comment_set" :key="idx" :comment="comment"/>

            <div>
              <input type="checkbox" id="secret" @input="onclick"> 비밀댓글
            </div>
            <input
              type="text"
              style="width: 80%"
              value="댓글을 입력하세요"
              v-model="inputdata"
            />
            <button @click="createcomment(detail.id)">등록</button>
          </tr>
        </table>
      </form>
    </div>

    <!-- <div class="btnWrap">
			<a href="javascript:;" @click="fnList" class="btn">목록</a>
		</div>	 -->
  </div>
</template>

<script>
import axios from "axios"
import ArticleRecommentItem from "@/components/ArticleRecommentItem"

export default {
  name: "ArticleDetailView",
  components : {
    ArticleRecommentItem,
  },
  data() {
    return {
      detail: [],
      inputdata: "",
      num: 0,
      comment_count : 0,
      check : false,
    }
  },
  methods: {
    onclick(){
      const checkbox = document.getElementById('secret')
      this.check = checkbox.checked
    },
    getdetail(id) {
      // const url = "http://127.0.0.1:8000/api/v1/articles/"
      const url = `${this.$store.state.url}`+"api/v1/articles/"
      axios({
        url: url + id,
        method: "get",
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
        .then((res) => {
          this.detail = res.data
          if (this.detail.comment_count !== null) {
            this.comment_count = this.detail.comment_count
          }
        })
        .catch((err) => {
          alert('로그인이 필요합니다')
          console.log(err)
        })
    },
    createcomment(id) {
      // const url = "http://127.0.0.1:8000/api/v1/articles/"
      const url = `${this.$store.state.url}`+"api/v1/articles/"
      if (this.inputdata !== "") {
        axios({
          url: url + id + "/comments/",
          method: "post",
          data: {
            content: this.inputdata,
            user : this.$store.state.user.id,
            secret : this.check
          },
          headers : {
            Authorization: `Bearer ${this.$store.state.user.token}`
          }
        })
          .then((res) => {
            console.log(res)
            alert("댓글이 등록되었습니다.")
            this.inputdata = ""
            this.getdetail(this.detail.id)
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        alert("댓글을 입력해주세요.")
      }
    },
    updatearticle() {
      this.$router.push({name: 'updatearticle', params: {detail:this.detail}})
    },
    deletearticle() {
      // const url = "http://127.0.0.1:8000/api/v1/articles/"
      const url = `${this.$store.state.url}`+"api/v1/articles/"
      axios({
        url : url + this.detail.id + '/',
        method : 'delete',
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
      .then(() =>{
        alert("게시물이 삭제되었습니다.")
        this.$router.push({name : 'article'})
      })
      .catch((err)=>{
        console.log(err)
        alert("게시물 삭제에 실패하였습니다.")
      })
    }
  },
  created() {
    this.getdetail(this.$route.params.id)
  },
}
</script>

<style>

table {
  width: 100%;
  border-collapse: collapse;
}
tr {
  font-family: cafeair;
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
  text-align: left;
}
.tbAdd td.txt_cont {
  height: 300px;
  vertical-align: top;
}
.btnWrap {
  text-align: center;
  margin: 20px 0 0 0;
}
.btnWrap a {
  margin: 0 10px;
}
.btnAdd {
  background: #43b984;
}
.btnDelete {
  background: #f00;
}
@font-face {
  font-family: "cafeair";
  src: url("@/assets/fonts/Cafe24SsurroundAir.ttf");
}
</style>
