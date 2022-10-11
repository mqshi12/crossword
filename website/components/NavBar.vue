<template>
  <!-- eslint-disable -->

  <!-- need IDs for the individual things i think to make them clickable -->
  <div class="navbar">
    <NuxtLink to="/">Home</NuxtLink>
    <NuxtLink to="archive">Archive</NuxtLink>
    <NuxtLink to="about">About</NuxtLink>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "Tutorial",
  props: {
    msg: String,
  },
  
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: black;
  font-family: "Space Mono";
  font-weight: bold;
  font-size: 25px;
  background-color: none;
  padding: 10px;
}

a:hover {
  background-color: white;
}

.navbar {
  display: flex;
  gap: 5vw;
  flex-direction: row-reverse;
  padding-top: 3vh;
  padding-right: 2vw;
}
</style>