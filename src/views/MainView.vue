<template>
  <div>
    <h1>인기 차트</h1>
    <MovieRankList />

    <div class="multi">
      <div>
        <h2>최신 게시물</h2>

        <div class="listWrap">
          <table class="tbList">
            <colgroup>
              <col width="*" />
              <col width="10%" />
            </colgroup>
            <tr>
              <th>제목</th>
              <th>작성자</th>
            </tr>
            <tr id="lst" v-for="(row, idx) in articlelist" :key="idx">
              <td class="txt_left">
                <a href="javascript:;" @click="godetail(`${row.id}`)">{{
                  row.title
                }}</a>
              </td>
              <td>{{ row.user }}</td>
            </tr>
            <tr v-if="articlelist.length == 0">
              <td colspan="2">데이터가 없습니다.</td>
            </tr>
          </table>
        </div>
      </div>

      <div>
        <h2>인기 리뷰</h2>
        <div class="listWrap">
          <table class="tbList">
            <colgroup>
              <col width="*" />
              <col width="10%" />
            </colgroup>
            <tr>
              <th>제목</th>
              <th>작성자</th>
            </tr>
            <tr id="lst" v-for="(row, idx) in articlelist" :key="idx">
              <td class="txt_left">
                <a href="javascript:;" @click="godetail(`${row.id}`)">{{
                  row.title
                }}</a>
              </td>
              <td>{{ row.user }}</td>
            </tr>
            <tr v-if="articlelist.length == 0">
              <td colspan="2">데이터가 없습니다.</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import MovieRankList from "../components/MovieRankList"

export default {
  name: "MainView",
  components: {
    MovieRankList,
  },
  data() {
    return {
      articlelist: [],
    }
  },
  methods: {
    getarticle() {
      const url = "http://127.0.0.1:8000/api/v1/articles/"
      axios({
        url: url,
        method: "get",
      })
        .then((res) => {
          this.articlelist = res.data.slice(0, 5)
          console.log(this.articlelist)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    godetail(id) {
      this.$router.push({name : 'articledetail', params : {id}})
    }
  },
  created() {
    this.getarticle()
  },
}
</script>

<style scope>
.multi {
  column-count: 2;
  column-gap: 50px;
  column-rule: 1px dotted black;
  text-align: center;

  margin-top: 50px;
}
a {
  text-decoration: none !important;
  color: black !important;
  
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

td {
  font-family: cafeair;
}
</style>
