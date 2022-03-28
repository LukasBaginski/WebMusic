<template>
  <div class="footerblock">
      <v-footer padless class="minus-left footer arrow-up">
        <v-col class="text-center" cols="12">
          <v-img src="/song-image/{{currentSongId}}.png"></v-img>
        </v-col>
      </v-footer>
  </div>
</template>

<script>
export default {
  name: 'FooterBlock'
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
