<template>
  <div>
    <div id="inputform">
      <span style="margin-right:10px; font-size:20px">영상 제목</span>
      <div @keyup.enter="pluslist">
        <input type="text" class="keyword" autocomplete="off" @keyup="recosearch" style="width:500px" :value="inputdata" @input="inputdata = $event.target.value"/>
        <div class="keywords">

        </div>
        <RecoSearchListItem v-for="(lst, idx) in searchlist" :key="idx" :searchItem="lst" style="width:500px"/>
      </div>
      <!-- <button style="margin-left : 10px">검색</button> -->
    </div>

    <!-- <p>
      시청 인원
      <input type="checkbox" id="p_1" class="checkbox"/> <label for="p_1">1</label>
      <input type="checkbox" id="p_2" class="checkbox"/> <label for="p_2">2</label>
      <input type="checkbox" id="p_4" class="checkbox"/> <label for="p_4">4</label>
    </p> -->
    <button @click="getreco" style="margin:30px">추천받기</button>

    <h2 style="margin-bottom:20px">OTT를 추천해드릴게요!</h2>
    <h2 style="margin-top:20px">1인</h2>
    <hr>
    <reco-res-item :ottlist="ottlist[0]" :price="ott[1]"/>

    <h2 style="margin-top:20px">2인</h2>
    <hr>
    <reco-res-item :ottlist="ottlist[1]" :price="ott[2]"/>

    <h2 style="margin-top:20px">4인</h2>
    <hr>
    <reco-res-item :ottlist="ottlist[3]" :price="ott[4]"/>
  </div>
</template>

<script>
import RecoSearchListItem from '@/components/RecoSearchListItem.vue'
import axios from 'axios'
import RecoResItem from '@/components/RecoResItem.vue'

export default {
  name: "RecoView",
  components: {
    RecoSearchListItem,
    RecoResItem,
  },
  data() {
    return {
      inputdata : null,
      searchlist : [],
      list : [],
      inputid : null,
      inputtype : null,
      ottlist : [],
      ott : [],
    }
  },
  methods : {
    getreco(){
      console.log(this.searchlist)
      // const url = "http://127.0.0.1:8000/movies/al/"
      const url = `${this.$store.state.url}`+"movies/al/"
      axios({
        url : url,
        method : 'post',
        data : {
          movie : this.searchlist
        }
      })
      .then((res) => {
        this.ott = res.data
        this.ottlist = res.data.list
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getData() {
      // const URL = "http://127.0.0.1:8000/movies/search/"
      const URL = `${this.$store.state.url}`+"movies/search/"
      axios({
        url: URL + this.inputdata,
        method: "get",
      })
        .then((res) => {
          this.list = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    pluslist() {
      console.log(this.list)
      const tmp = {id : this.inputid, title:this.inputdata, media_type : this.inputtype}
      this.searchlist.push(tmp)
      this.inputdata = null
      this.inputid = null
      this.closeKeywords()
    },
    minuslist(title) {
      let lst = []
      for (var i in this.searchlist){
        if (i.title !== title) {
          lst.push(i)
        }
      }
      this.searchlist = lst
    },
    closeKeywords(){
      const keywords = document.querySelector(".keywords")
      keywords.style.display = "none"
      keywords.innerHTML = ""
    },
    recosearch: function(e) {
      const keyword = document.querySelector(".keyword")
      const keywords = document.querySelector(".keywords")

      const selectedKeyword = keywords.querySelector("li.selected")

      // li.selected 가 없는 경우에만 api에서 데이터를 가져옴
      if(keyword.value.length > 1 && !selectedKeyword){

        console.log("=== API 호출 ===")
        this.getData()
        keywords.innerHTML = ""
        
        const $ul = document.createElement("ul")
        $ul.style.padding = "0px"
        for(let lst of this.list) {
            const $li = document.createElement("li")
            $li.textContent = `${lst.title}`
            $li.setAttribute('id', lst.multi_id)
            $li.setAttribute('style', 'width:500px')
            $li.className = lst.media_type
            $li.style.border = "0.5px solid black"
            $ul.append($li)
        }
        keywords.append($ul)
        
        keywords.style.display = "block" 

      }
      
      if(keyword.value.length === 0) {
          keywords.innerHTML = ""
      }
      
      // 요구사항 1 - esc를 누르면 추천 검색어 창이 닫여야 합니다.
      if(e.key === "Escape") {
          this.closeKeywords()
      }
      
      // console.log(e.key)
      
      // 요구사항 2 - 키보드의 위, 아래 키를 누르면 추천 검색어 하이라이트가 옮겨지고 엔터를 누르면 하이라이트가 위치한 검색어가 입력창에 반영되어야 합니다.
      
      const keywordsList = keywords.querySelectorAll("li")
      
      if((e.key === "ArrowUp" || e.key === "ArrowDown") && keywords.style.display === "block") {
          let target
          const initIndex = e.key === "ArrowUp" ? keywordsList.length - 1 : 0
          const adjacentSibling = selectedKeyword && (e.key === "ArrowUp" ? selectedKeyword.previousElementSibling : selectedKeyword.nextElementSibling)
          
          if(adjacentSibling) {
              target = adjacentSibling
          } else {
              target = keywordsList.item(initIndex)
          } 
          
          selectedKeyword && selectedKeyword.classList.remove("selected")
          target.classList.add("selected")
          keyword.value = target.textContent
          this.inputdata = target.textContent
          this.inputid = target.id
          this.inputtype =target.className.split(' ')[0]
      }
    },
  }
}
</script>

<style>
  .checkbox {
    margin-left: 15px;
  }

  label {
    margin : 10px;
  }

  #inputform{
    display: flex;
    justify-content: center;
  }

  li {
    list-style: none;
    padding-left: 0px;

    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }
</style>
