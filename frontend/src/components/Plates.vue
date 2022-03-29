<template>
  <form @submit.prevent="$emit('on-submit', form)">

    <div class="form-group">
      <input type="text" placeholder="Plate Number" v-model="form.plate"/>
    </div>

    <div class="form-group">
      <input type="text" placeholder="Owner Name" v-model="form.name"/>
    </div>

    <div class="form-group">
      <datepicker v-model="state.start_date"></datepicker>
    </div>

    <div class="form-group">
      <datepicker v-model="state.end_date"></datepicker>
    </div>

    <button type="submit" @click="addPlate()">Add Plate</button>

  </form>
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
      console.log(moment(this.form.start_date).format('YYYY-MM-DDT00:00:00Z'));
    },
  },
  components: {
    Datepicker,
  },
};
</script>
