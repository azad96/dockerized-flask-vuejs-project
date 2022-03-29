<template>
  <div>
    <button type="submit">List</button>
    <button type="submit" @click="navigateToAddPlate()">Add New Button</button>
  </div>
</template>

<script>
export default {
  data() {
  },
  methods: {
    navigateToAddPlate() {
      this.$router.push('/plate');
    },
  },
};
</script>
