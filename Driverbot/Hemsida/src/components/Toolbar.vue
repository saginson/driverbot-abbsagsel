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
          <!-- här har jag använt mig av en router-link istället, vilket skickar användaren till "/" som jag då gjort till startsidan i router.js -->
          <router-link id=b45 :to="{ path: '/' }">Home</router-link>
          <v-spacer></v-spacer>
          <v-col cols="12" sm="3" name: column>
            <!-- genom to="help" skickas användaren till routen "help" -->
            <v-btn icon to="help">
              <!-- <v-icon>mdi-information</v-icon> -->
            </v-btn>
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