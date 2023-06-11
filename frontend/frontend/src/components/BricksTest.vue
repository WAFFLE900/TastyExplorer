<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BricksTest",
  data() {
    return {
      msg: "Not Found",
    };
  },
  created() {
    const path = "http://127.0.0.1:5000/bricks";
    axios
      .get(path)
      .then((res) => {
        console.log(res.data);
        this.msg = res.data;
      })
      .catch((err) => {
        console.error(err);
      });
  },
};
</script>