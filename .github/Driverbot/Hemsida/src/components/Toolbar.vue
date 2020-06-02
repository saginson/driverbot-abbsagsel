<template>
  <v-row >
    <v-col
      v-for="(bar, i) in bars"
      :key="i"
      cols="12"
      sm="12"
      md="6"
      class="my-4">
      <v-card flat height="70px">
        <v-toolbar :color="bar.class" :dark="bar.dark" >
          <!-- router-link som ej används -->
          <router-link id=b45 :to="{ path: '/' }">Home</router-link>
          <v-spacer></v-spacer>
          <v-col cols="12" sm="3" name: column>
          </v-col>
        </v-toolbar>
      </v-card>
    </v-col>
  </v-row>
</template>




<script>
  export default {
    name: 'Toolbar',
    data: () => ({
      bars: [
        { class: '', dark: true },
      ],
    }),
 }


</script>

 <style> 
 /* Color, placement och pictures*/
#b45{
  font-size: 26px;
  text-decoration: none;
  color: #FAFAFA;
  /* font-family: "Arial Black"; */
}

</style>