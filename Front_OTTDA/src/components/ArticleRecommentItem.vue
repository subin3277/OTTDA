<template>
  <div>
    <div v-if="!comment.secret || comment.user===this.$store.state.user.id || this.$parent.detail.user===this.$store.state.user.id">
      <!--  || writer===this.$store.state.user.id -->
      <th style="width: 15%">{{ comment.user_nickname }}</th>
      <td style="width: 85%">
        <div>
          <span v-if="!commentst">{{ comment.content }} | </span>
          <span v-else>
            <input type="text" v-model = "inputdata">
            <button @click="updatecomment">완료</button>
          </span>
          <span style="margin-right : 10px" @click="recommentcreate"> 답글</span>
          <span v-if="$store.state.user.id === comment.user">
            <span style="margin-right : 10px" @click="updatecommentst">수정</span>
            <span style="margin-right : 10px" @click="deletecomment">삭제</span>
          </span>
        </div>

        <div class="listWrap">
          <table class="tbList">
            <colgroup>
              <col width = "70px"/>
              <col width='*'/>
            </colgroup>
            <tr class="comment-list-item" v-for="(lst, idx) in recomment" :key="idx">
              <th>{{ lst.user_nickname }}</th>
              <td>
                <div>
                  <span v-if="!recommentst">{{ lst.content }} </span>
                  <!-- <span v-else>
                    <input type="text" @input="reinputdata" :value=lst.content>
                    <button @click="updaterecomment">완료</button>
                  </span>
                  <span v-if="$store.state.user.id === lst.user">
                    <span style="margin-right : 10px" @click="updaterecommentst">수정</span>
                    <span style="margin-right : 10px" @click="deleterecomment">삭제</span>
                  </span> -->
                </div>
              </td>
            </tr>
          </table>
        </div>

        <template v-if="recommentcreatest">
          <RecommentCreateItem :commentid ="comment.id"/>
        </template>
      </td>
    </div>
    <div v-else>
      <th style="width: 15%"></th>
      <td style="width: 85%">
        <div>
          <span> 비밀댓글입니다! </span>
        </div>

        <div class="listWrap">
          <table class="tbList">
            <colgroup>
              <col width = "70px"/>
              <col width='*'/>
            </colgroup>
            <tr class="comment-list-item" v-for="(lst, idx) in recomment" :key="idx">
              <th></th>
              <td>
                <div>
                  <span v-if="!recommentst">비밀댓글입니다.</span>
                  <!-- <span v-else>
                    <input type="text" @input="reinputdata" :value=lst.content>
                    <button @click="updaterecomment">완료</button>
                  </span>
                  <span v-if="$store.state.user.id === lst.user">
                    <span style="margin-right : 10px" @click="updaterecommentst">수정</span>
                    <span style="margin-right : 10px" @click="deleterecomment">삭제</span>
                  </span> -->
                </div>
              </td>
            </tr>
          </table>
        </div>

        <template v-if="recommentcreatest">
          <RecommentCreateItem :commentid ="comment.id"/>
        </template>
      </td>
    </div>
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
      recommentcreatest : false,
      inputdata : this.comment.content,
      reinputdata : '',
      commentst : false,
      recommentst : false,
    }
  },
  methods: {
    getrecomment() {
      // const url = "http://127.0.0.1:8000/api/v1/comments/"
      const url = `${this.$store.state.url}`+"api/v1/comments/"
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
    recommentcreate() {
      this.recommentcreatest = !this.recommentcreatest
    },
    updatecommentst(){
      this.commentst = !this.commentst
    },
    updaterecommentst(){
      this.recommentst = !this.recommentst
    },
    updatecomment(){
      // const url = "http://127.0.0.1:8000/api/v1/comments/"
      const url = `${this.$store.state.url}`+"api/v1/comments/"
      axios({
        url : url + this.comment.id + '/',
        method : 'PUT',
        data : {
          content : this.inputdata,
          user : this.comment.user
        },
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        alert('댓글이 수정되었습니다.')
        this.$parent.getdetail(this.comment.article)
      })
      .catch((err) => {
        alert('수정에 실패하였습니다.')
        console.log(err)
      })
    },
    deletecomment() {
      // const url = "http://127.0.0.1:8000/api/v1/comments/"
      const url = `${this.$store.state.url}`+"api/v1/comments/"
      axios({
        url : url+this.comment.id,
        method : 'delete',
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        alert('댓글이 삭제되었습니다.')
        this.$parent.getdetail(this.comment.article)
      })
      .catch((err) => {
        console.log(err)
        alert('댓글 삭제에 실패하였습니다.')
      })
    },
    updaterecomment(){
      // const url = "http://127.0.0.1:8000/api/v1/recomments/"
      const url = `${this.$store.state.url}`+"api/v1/recomments/"
      axios({
        url : url + this.comment.id + '/',
        method : 'PUT',
        data : {
          content : this.reinputdata,
          user : this.lst.user
        },
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        alert('댓글이 수정되었습니다.')
        this.$parent.getdetail(this.comment.article)
      })
      .catch((err) => {
        alert('수정에 실패하였습니다.')
        console.log(err)
      })
    },
    deleterecomment(){
      // const url = "http://127.0.0.1:8000/api/v1/recomments/"
      const url = `${this.$store.state.url}`+"api/v1/recomments/"
      axios({
        url : url+this.recomment.id,
        method : 'delete',
        headers : {
          Authorization : `Bearer ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        alert('댓글이 삭제되었습니다.')
        this.$parent.getdetail(this.comment.article)
      })
      .catch((err) => {
        console.log(err)
        alert('댓글 삭제에 실패하였습니다.')
      })
    }
  },
  created() {
    this.getrecomment()
  },
}
</script>

<style></style>
