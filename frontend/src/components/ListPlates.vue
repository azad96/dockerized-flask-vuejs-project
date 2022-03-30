<template>
  <section>
    <div class="container">
      <table class="table">
        <thead>
        <tr>
          <th>Plate Number</th>
          <th>Owner Name</th>
          <th>Start Date</th>
          <th>End Date</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="plate in plates" :key="plate.id">
          <td>{{ plate.plate_number }}</td>
          <td>{{ plate.owner }}</td>
          <td>{{ plate.start_date }}</td>
          <td>{{ plate.end_date }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      plates: '',
    };
  },
  methods: {
    getPlates() {
      const path = 'http://localhost:5000/plate';
      axios.get(path)
        .then((res) => {
          this.plates = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getPlates();
  },
};
</script>


