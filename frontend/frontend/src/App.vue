<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
/* 會影響所有頁面的css */

html,
body {
  width: 100%;
  height: 100%;
  margin: 0 auto;
  padding: 0 auto;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

/* body {
  margin: 0;
} */

@import url('http://fonts.googleapis.com/css?family=Noto+Sans+TC:100,300,400,500,700,900');

/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
