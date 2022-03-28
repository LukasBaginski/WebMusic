<template>
  <div class="library">
    <h1 v-on:click="clicktest">click me!</h1>
  </div>
</template>

<script>
export default {
  name: 'LibraryContent',
  props: {
    msg: String
  },
  methods: {
    clicktest() {
      console.log("clicktest clicked lolol");
      this.emitter.emit("testevent", "testlol");
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
