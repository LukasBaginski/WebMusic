<template>
  <div class="footerblock">
    <v-footer padless class="minus-left footer arrow-up">
      <v-img
        max-height="150"
        max-width="250"
        :src="songImage"
      ></v-img>
      <v-col class="text-center" cols="12">
        test
      </v-col>
    </v-footer>
  </div>
</template>

<script>
// v-img src: /song-image/{{currentSongId}}.png
export default {
  name: 'FooterBlock',
  data() {
    return {
      songImage: require("../assets/test.jpg") // still not showing up: https://stackoverflow.com/questions/53112247/vuetify-issue-why-doesnt-the-v-img-component-display-anything-despite-the-ima
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
.footer {
  position: fixed;
  bottom: 0;
}
.arrow-up {
  width: 0;
  height: 0;
  border-left: 140px solid transparent;
  border-right: 200px solid transparent;
  border-bottom: 100px solid #42b983;
}
.left {
  position: fixed;
  left: 0;
}
.minus-left {
  position: fixed;
  left: -140px;
}
</style>
