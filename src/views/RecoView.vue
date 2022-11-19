<template>
  <div>
    <div id="inputform">
      <span style="margin-right:10px">영상 제목</span>
      <div @keyup.enter="pluslist">
        <input type="text" class="keyword" autocomplete="off" @keyup="recosearch" style="width:500px" :value="inputdata" @input="inputdata = $event.target.value"/>
        <div class="keywords">

        </div>
        <RecoSearchListItem v-for="(lst, idx) in searchlist" :key="idx" :searchItem="lst"/>
      </div>
      <!-- <button style="margin-left : 10px">검색</button> -->
    </div>

    <p>
      시청 인원
      <input type="checkbox" id="p_1" class="checkbox"/> <label for="p_1">1</label>
      <input type="checkbox" id="p_2" class="checkbox"/> <label for="p_2">2</label>
      <input type="checkbox" id="p_4" class="checkbox"/> <label for="p_4">4</label>
    </p>
    <button>추천받기</button>
  </div>
</template>

<script>
import RecoSearchListItem from '@/components/RecoSearchListItem.vue'
import axios from 'axios'

export default {
  name: "RecoView",
  components: {
    RecoSearchListItem,
  },
  data() {
    return {
      inputdata : null,
      searchlist : [],
      list : []
    }
  },
  methods : {
    getData() {
      const URL = "http://127.0.0.1:8000/movies/search/"
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
      this.searchlist.push(this.inputdata)
      this.inputdata = null
      this.closeKeywords()
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
        for(let lst of this.list) {
            const $li = document.createElement("li")
            $li.textContent = `${lst.title}`
            $li.style.border = "1px solid black"
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
</style>
