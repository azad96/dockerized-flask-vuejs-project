<template>
  <section>
    <div class="container">
      <input type="text" style="margin-bottom: 20px" v-model="search" placeholder="Search by Plate/Owner">
      <sorted-table :values="filteredPlates">
        <thead>
        <tr>
          <th scope="col" style="text-align: center; width: 20rem;">
            <sort-link name="plate_number">Plate Number</sort-link>
          </th>
          <th scope="col" style="text-align: center; width: 20rem;">
            <sort-link name="owner_name">Owner Name</sort-link>
          </th>
          <th scope="col" style="text-align: center; width: 20rem;">
            <sort-link name="start_date">Start Date</sort-link>
          </th>
          <th scope="col" style="text-align: center; width: 20rem;">
            <sort-link name="end_date">End Date</sort-link>
          </th>
        </tr>
        </thead>
        <template #body="sort">
          <tbody>
          <tr v-for="plate in sort.values" :key="plate.id">
            <td>{{ plate.plate_number }}</td>
            <td>{{ plate.owner_name }}</td>
            <td>{{ plate.start_date }}</td>
            <td>{{ plate.end_date }}</td>
          </tr>
          </tbody>
        </template>
      </sorted-table>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      plates: [],
      search: '',
    };
  },
  methods: {
    getPlates() {
      const path = 'http://localhost:5000/plate';
      axios.get(path)
        .then((res) => {
          this.plates = Object.keys(res.data).map((key) => {
            return res.data[key]
          })
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
    filteredPlates: function () {
      return this.plates.filter((plate) => {
        return plate.plate_number.toLowerCase().match(this.search) || plate.owner_name.toLowerCase().match(this.search);
      });
    }
  },
};
</script>


