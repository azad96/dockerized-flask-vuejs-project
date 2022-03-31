<template>
  <section>
    <div class="container">
      <input type="text" v-model="search" placeholder="Search Plate/Owner">
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
        <tr v-for="plate in filteredPlates" :key="plate.id">
          <td>{{ plate.plate_number }}</td>
          <td>{{ plate.owner_name }}</td>
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
      search: '',
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
  computed: {
    filteredPlates: function() {
      return Object.values(this.plates).filter((plate) => {
        return plate.plate_number.toLowerCase().match(this.search) || plate.owner_name.toLowerCase().match(this.search);
      });
    }
  },
};
</script>


