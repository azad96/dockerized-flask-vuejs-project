<template>
  <section>
    <div class="container">
      <form @submit.prevent="addPlate()" method="post">

        <div class="form-group">
          <label for="plate-number">Plate number:</label>
          <input type="text" v-model="info.plate_number" required/>
        </div>

        <div class="form-group">
          <label for="owner-name">Owner name:</label>
          <input type="text" v-model="info.owner_name"/>
        </div>

        <div class="form-group">
          <label for="start-date">Start date:</label>
          <input type="datetime-local" v-model="info.start_date" class="datepicker">
        </div>

        <div class="form-group">
          <label for="end-date">End date:</label>
          <input type="datetime-local" v-model="info.end_date" class="datepicker">
        </div>

        <button type="submit">Add Plate</button>

      </form>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
  data() {
    return {
      info: {
        plate_number: '',
        owner_name: '',
        start_date: '',
        end_date: '',
      },
      response_data: '',
    };
  },
  methods: {
    addPlate() {
      let plateInfo = JSON.stringify({
          plate_number: this.info.plate_number,
          owner_name: this.info.owner_name,
          start_date: this.info.start_date ? moment(this.info.start_date).format('YYYY-MM-DDThh:mm:ss') : '',
          end_date: this.info.end_date ? moment(this.info.end_date).format('YYYY-MM-DDThh:mm:ss') : '',
      })
      console.log(plateInfo)
      const path = 'http://localhost:5000/plate';
      axios.post(path, plateInfo)
        .then((response) => {
          this.response_data = response
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
};
</script>


