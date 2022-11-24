<template>
  <div>
    <h2>누구랑 웃지?</h2>

    <div class="listWrap">
      <table class="tbList">
        <colgroup>
          <col width="6%" />
          <col width="*" />
          <col width="10%" />
          <col width="15%" />
        </colgroup>
        <tr>
          <th>no</th>
          <th>제목</th>
          <th>작성자</th>
          <th>작성일</th>
        </tr>
        <tr id="lst" v-for="(row, idx) in list" :key="idx">
          <td>{{ no - idx }}</td>
          <td class="txt_left">
            <a href="javascript:;" @click="godetail(`${row.id}`)">{{ row.title }}</a>
          </td>
          <td>{{ row.user_nickname }}</td>
          <td>{{ row.created_at.substring(0, 10) }}</td>
        </tr>
        <tr v-if="list.length == 0">
          <td colspan="4">데이터가 없습니다.</td>
        </tr>
      </table>
    </div>

    <div class="pagination" v-if="paging.totalCount > 0">
      <a href="javascript:;" @click="fnPage(1)" class="first">&lt;&lt;</a>
      <a
        href="javascript:;"
        v-if="paging.start_page > 10"
        @click="fnPage(`${paging.start_page - 1}`)"
        class="prev"
        >&lt;</a
      >
      <template v-for="(n, index) in paginavigation()">
        <template v-if="paging.page == n">
          <strong :key="index">{{ n }}</strong>
        </template>
        <template v-else>
          <a href="javascript:;" @click="fnPage(`${n}`)" :key="index">{{
            n
          }}</a>
        </template>
      </template>
      <a
        href="javascript:;"
        v-if="paging.total_page > paging.end_page"
        @click="fnPage(`${paging.end_page + 1}`)"
        class="next"
        >&gt;</a
      >
      <a
        href="javascript:;"
        @click="fnPage(`${paging.total_page}`)"
        class="last"
        >&gt;&gt;</a
      >
    </div>

    <div class="btnRightWrap">
      <a @click="gocreate" class="btn">새 게시물 작성</a>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "ArticleView",
  data() {
    return {
      body: "",
      list: "", //리스트 데이터
      no: "", //게시판 숫자처리
      paging: "", //페이징 데이터
      start_page: "", //시작페이지
      page: this.$route.query.page ? this.$route.query.page : 1,
      keyword: this.$route.query.keyword,
      paginavigation: function () {
        //페이징 처리 for문 커스텀
        var pageNumber = []
        var start_page = this.paging.start_page
        var end_page = this.paging.end_page
        for (var i = start_page; i <= end_page; i++) pageNumber.push(i)
        return pageNumber
      },
    }
  },
  methods: {
    gocreate() {
      this.$router.push({ name: "createarticle" })
    },
    getlist() {
      // const url = "http://127.0.0.1:8000/api/v1/articles/"
      const url = `${this.$store.state.url}`+"api/v1/articles/"
      axios({
        url: url,
        method: "get",
      })
        .then((res) => {
          this.list = res.data.reverse().slice((this.page - 1) * 10, this.page * 10)
          console.log(this.list)
          this.body = {
            // 데이터 전송
            board_code: this.board_code,
            page: this.page,
          }
          const paging = {
            totalCount: res.data.length,
            total_page: Math.ceil(res.data.length / 10),
            page: this.page,
            start_page: Math.ceil(this.page / 10),
            end_page: Math.ceil(this.page / 10) * 10,
            ipp: 10,
          }
          if (paging.total_page < paging.end_page) {
            paging.end_page = paging.total_page
          }
          this.paging = paging
          this.no = paging.totalCount - (paging.page - 1) * this.paging.ipp
        })
        .catch((err) => {
          console.log(err)
        })
    },
    fnPage(n) {
      //페이징 이
      if (this.page != n) {
        this.page = n
        this.getlist()
      }
    },
    godetail(id) {
      this.$router.push({name : 'articledetail', params : {id}})
    }
  },
  created() {
    this.getlist()
  },
}
</script>

<style scoped>
#lst {
  font-family: cafeair;
}
a {
  text-decoration: none;
  color: black;
}
table {
  width: 100%;
  border-collapse: collapse;
}
.searchWrap {
  border: 1px solid #888;
  border-radius: 5px;
  text-align: center;
  padding: 20px 0;
  margin-bottom: 40px;
}
.searchWrap input {
  width: 60%;
  height: 36px;
  border-radius: 3px;
  padding: 0 10px;
  border: 1px solid #888;
}
.searchWrap .btnSearch {
  display: inline-block;
  margin-left: 10px;
}
.tbList th {
  border-top: 1px solid #888;
}
.tbList th,
.tbList td {
  border-bottom: 1px solid #eee;
  padding: 5px 0;
}
.tbList td.txt_left {
  text-align: left;
}
.btnRightWrap {
  text-align: right;
  margin: 10px 0 0 0;
}

.pagination {
  margin: 20px 0 0 0;
  text-align: center;
}
.first,
.prev,
.next,
.last {
  border: 1px solid #666;
  margin: 0 5px;
}
.pagination span {
  display: inline-block;
  padding: 0 5px;
  color: #333;
}
.pagination a {
  text-decoration: none;
  display: inline-blcok;
  padding: 0 5px;
  color: #666;
}

strong {
  color: #a3e1f4
}
</style>
