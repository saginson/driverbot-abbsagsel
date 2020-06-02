<template>
  <v-app>
    <Toolbar/>
    <v-content>
    <router-view/>
    </v-content>
  </v-app>
</template>


<script>
import Toolbar from './components/Toolbar'

export default {
  name: 'App',
  components: {
    Toolbar,
  },
  data () {
    return {
      addnew:false,
      //
    }
  }
}
</script>

<style>
#toolbar{
  background-image: url("https://s3.envato.com/files/236520857/MG_VH_CITY_ROAD_LOOP_PREW_500x300.jpg");
}
</style>
