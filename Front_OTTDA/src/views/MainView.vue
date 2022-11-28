<template>
  <div>
    <!-- <div
      id="scroll"
      style="
        background-color: #a3e1f4;
        min-width: 100vw;
        height: 100vw;
        margin-left: calc(-50vw + 50%);
      "
    >
      <img
        src="../assets/logo_full.png"
        alt=""
        style="width: 500px"
        @click="doanimate($event.target)"
      />
    </div> -->
    <div>
      <h1>인기 차트</h1>
      <MovieRankList style="width: 100%" />

      <div class="multi">
        <div>
          <h2>최신 게시물</h2>

          <div class="listWrap">
            <table class="tbList">
              <colgroup>
                <col width="*" />
                <col width="15%" />
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
                <td>{{ row.user_nickname }}</td>
              </tr>
              <tr v-if="articlelist.length == 0">
                <td colspan="2">데이터가 없습니다.</td>
              </tr>
            </table>
          </div>
        </div>

        <div>
          <h2>최신 리뷰</h2>
          <div class="listWrap">
            <table class="tbList">
              <colgroup>
                <col width="*" />
                <col width="15%" />
              </colgroup>
              <tr>
                <th>제목</th>
                <th>작성자</th>
              </tr>
              <tr id="lst" v-for="(row, idx) in reviewlist" :key="idx">
                <td class="txt_left">
                  <a href="javascript:;" @click="goreviewdetail(`${row.id}`)">{{
                    row.title
                  }}</a>
                </td>
                <td>{{ row.user_nickname }}</td>
              </tr>
              <tr v-if="reviewlist.length == 0">
                <td colspan="2">데이터가 없습니다.</td>
              </tr>
            </table>
          </div>
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
      reviewlist: [],
    }
  },
  methods: {
    getarticle() {
      const url = `${this.$store.state.url}`+"api/v1/articles/"

      // const url = "http://52.196.3.18:8000/api/v1/articles/"
      console.log(url)
      axios({
        url: url,
        method: "get",
      })
        .then((res) => {
          this.articlelist = res.data.reverse().slice(0, 5)
          console.log(this.articlelist)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    godetail(id) {
      this.$router.push({ name: "articledetail", params: { id } })
    },
    goreviewdetail(id) {
      this.$router.push({ name: "reviewdetail", params: { id } })
    },
    doanimate(target) {
      console.log(target)
      target.setAttribute(
        "style",
        "animation : slide-out-bck-top 1s cubic-bezier(0.550, 0.085, 0.680, 0.530); width:500px"
      )
      //target.animation = "slide-out-bck-top"
      // 1s cubic-bezier(0.550, 0.085, 0.680, 0.530)
    },
    getreview() {
      const url = `${this.$store.state.url}` + "reviews/reviews/"
      // const url = "http://52.196.3.18:8000/reviews/reviews/"
      axios({
        url: url,
        method: "get",
      })
        .then((res) => {
          this.reviewlist = res.data.reverse().slice(0, 5)
          console.log(this.reviewlist)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getarticle()
    this.getreview()
    this.$store.dispatch('change')
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

td a {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

/* #scroll img {
  animation: slide-out-bck-top 1s cubic-bezier(0.550, 0.085, 0.680, 0.530);
} */

@keyframes slide-out-bck-top {
  0% {
    transform: translateZ(1) translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateZ(-1100px) translateY(-1000px);
    opacity: 0;
  }
}
</style>
