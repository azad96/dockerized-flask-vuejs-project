<template>
  <section>
    <div class="container">
      <form @submit.prevent="$emit('on-submit', info)">

        <div class="form-group">
           <label for="plate">Plate number:</label>
          <input type="text" v-model="info.plate" required/>
        </div>

        <div class="form-group">
          <label for="name">Owner name:</label>
          <input type="text" v-model="info.name"/>
        </div>

        <div class="form-group">
          <label for="start_date">Start date:</label>
          <datepicker v-model="info.start_date"></datepicker>
        </div>

        <div class="form-group">
          <label for="end_date">End date:</label>
          <datepicker v-model="info.end_date"></datepicker>
        </div>

        <button type="submit" @click="addPlate()">Add Plate</button>

      </form>
    </div>

  </section>
</template>

<script>
import Datepicker from 'vuejs-datepicker';
import moment from 'moment';

export default {
  data() {
    return {
      info: {
        plate: '',
        name: '',
        start_date: Date.now(),
        end_date: Date.now(),
      },
    };
  },
  methods: {
    addPlate() {
      let plateInfo = {
        plateNumber: this.info.plate,
        ownerName: this.info.name,
        startDate: moment(this.info.start_date).format('YYYY-MM-DDT00:00:00Z'),
        endDate: moment(this.info.end_date).format('YYYY-MM-DDT00:00:00Z'),
      }
      console.log(plateInfo)
    },
  },
  components: {
    Datepicker,
  },
};
</script>


