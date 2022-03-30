<template>
  <section>
    <div class="container">
      <button type="submit" @click="navigateToListPlates()">List Plates</button>
      <button type="submit" @click="navigateToAddPlate()">Add a New Plate</button>
    </div>
  </section>
</template>

<script>
export default {
  methods: {
    navigateToAddPlate() {
      this.$router.push('/add-plate');
    },
    navigateToListPlates() {
      this.$router.push('/list-plates');
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  font-family: "Montserrat";
}

section {
  height: 100vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.container {
  width: 90%;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  box-shadow: 0px 0px 20px #00000033;
  border-radius: 8px;
}

.date-block {
  display: inline-block;
  width: 60%;
  padding: 5px;
  font-size: 18px;
  margin-top: 5px;
  margin-left: 10px;
  font-size: 20px;
}

.form-group {
  margin-top: 20px;
  font-size: 20px;
  color: #9e9e9e;
}

.form-group input {
  width: 60%;
  padding: 5px;
  font-size: 18px;
  border: 1px solid rgba(128, 128, 128, 0.199);
  margin-top: 5px;
  margin-left: 10px;
}

textarea {
  resize: vertical;
}

button {
  width: 100%;
  border: none;
  padding: 20px;
  font-size: 24px;
  border-radius: 8px;
  cursor: pointer;
  margin-top: 10px;
}
</style>
