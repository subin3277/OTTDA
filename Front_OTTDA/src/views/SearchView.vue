<template>
  <div>
    <p @keyup.enter="search">
      <input type="text" style="width: 500px" :value="inputdata" @input="inputdata = $event.target.value" />
      <button style="margin: 10px" @click="search">검색</button>
    </p>
    <p v-if="inputdata===null">검색어를 입력해주세요!</p>
    <p v-else>
      <b-container>
        <b-row cols="3" align-h="center">
          <SearchResListItem
            v-for="(lst, idx) in ressearch"
            :key="idx"
            :searchItem="lst"
          />
        </b-row>
      </b-container>
    </p>
  </div>
</template>

<script>
import axios from "axios"
import SearchResListItem from "@/components/SearchResListItem"

export default {
  name: "SearchView",
  components: {
    SearchResListItem,
  },
  data() {
    return {
      inputdata: '',
      ressearch: [],
    }
  },
  methods: {
    search() {
      // const URL = "http://127.0.0.1:8000/movies/search/"
      const URL = `${this.$store.state.url}`+"movies/search/"
      axios({
        url: URL + this.inputdata,
        method: "get",
      })
        .then((res) => {
          this.ressearch = res.data
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  updated(){
    // const URL = "http://127.0.0.1:8000/movies/search/"
    const URL = `${this.$store.state.url}`+"movies/search/"
      axios({
        url: URL + this.inputdata,
        method: "get",
      })
        .then((res) => {
          this.ressearch = res.data
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
  },
  created() {
    this.search()
  }
}
</script>

<style></style>
