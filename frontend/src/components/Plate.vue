<template>
  <form @submit.prevent="$emit('on-submit', form)">
    <div class="form-group">
      <label for="email">Email</label>
      <input type="email" name="email" v-model="form.email" />
    </div>

    <div class="form-group">
      <label for="name">Name</label>
      <input type="text" name="name" v-model="form.name" />
    </div>

    <button type="submit">Submit</button>
  </form>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
    },
  },
  data() {
    return {
      form: {
        email: this.user?.email || '',
        name: this.user?.name || '',
      },
    };
  },
};
</script>
