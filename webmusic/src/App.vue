<template>
  <LibraryContent msg="Welcome to Your Vue.js App"/>
  <FooterBlock />
</template>

<script>
import LibraryContent from './components/LibraryContent.vue';
import FooterBlock from './components/FooterBlock.vue';

export default {
  name: 'App',
  components: {
    LibraryContent,
    FooterBlock
  },
  data:() => ({
    currentSongId: ""
  }),

  mounted() {
    /*EventBus.$on("TESTEVENT", (payload) => {
      console.log("Test!!!!!!!!!!!! mit payload: " + payload);
    });*/
    this.emitter.on("testevent", payload => {
      console.log("test1234:" + payload);
    })
  },

  methods: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
