<template>
  <div>
    <b-col>
      <div class="card" id="carditem" style="width: 300px; height:500px; margin:15px" @click="goDetail(searchItem.multi_id,searchItem.media_type)">
        <img v-if="searchItem.poster_path == 'https://image.tmdb.org/t/p/originalNone'" src="../assets/quokka.png" style="width: 270px; height:400px; margin-top: 10px">
        <img v-else
          :src="searchItem.poster_path"
          class=""
          alt="..."
          style="width: 270px; height:400px; margin-top: 10px"
        />
        <div class="card-body">
          <div>
            {{ searchItem.title }}
          </div>
          <div v-if="!ottlist">
            {{ ottlist }}
          </div>
          <div v-else>
            {{ ottlist.join(' / ') }}
          </div>
        </div>  
      </div>
    </b-col>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "SearchResListItem",
  props: {
    searchItem: Object,
  },
  data() {
    return {
      ottlist : []
    }
  },
  methods: {
    goDetail(id, type) {
      this.$router.push({ name: "detail", params: { id:id , media_type: type} })
    },
    getOTT(id, type){
      console.log(id, type)
      // let url = "http://127.0.0.1:8000/movies/"
      let url = `${this.$store.state.url}`+"movies/"
      this.type = type
      if (type === 'movie') {
        url = url + 'movieprovider/' 
      } 
      else if (type === 'tv') {
        url = url + 'tvprovider/'
      }
      axios({
        url: url+id+'/',
        method : 'get' 
      })
      .then((res) => {
        for (const i of res.data) {
          this.ottlist.push(i.provider_name)
        }
        this.message = ""
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    this.getOTT(this.searchItem.multi_id,this.searchItem.media_type)
  }
}
</script>

<style>
#carditem {
  text-align: center;
  display: block;
  flex-flow: column nowrap;
  justify-content: center;
  margin: 0px 20px;
}
</style>
