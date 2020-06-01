<template>
  <v-container ma-0 pa-0>
    <v-layout row wrap>
  <div>
      <!-- <v-flex> -->
    <v-card class="justify-center" width="1920" height="850" outlined id="content2">
      <v-card-actions>
        <!-- <v-row align="start" justify="space-around" no-gutters> -->
          <!-- <v-slider
            inverse-label
            label="Brightness"
            v-model="ljusstyrka"
            color="green"
            max="1023"
            min="4"
          ></v-slider> -->
          <!-- <v-btn 
          @click="dir"
          state = 1>Forward </v-btn>
          <v-btn 
          @click="dir"
          state = 2>Backwards </v-btn>
          <v-btn
          @click="dir"
          state = 0>Stop </v-btn> -->



        <!-- <v-container grid-list-md> -->
          <v-row no-gutters style="height: 150px;">
          <v-container color="rgb(255, 0, 0, 0.2)">
            <v-btn class="ma-2" 
            text icon color="orange lighten-2" 
            @click="valueChange(0)">
            <v-icon color="white" >trending_down</v-icon>
            </v-btn>

            <v-btn class="ma-2" 
            text icon color="orange lighten-2" 
            @click="valueChange(1)">
            <v-icon color="white" >trending_up</v-icon>
            </v-btn>

            </v-container>
            </v-row>
          <v-spacer></v-spacer>
      <v-flex xs4>
      <!-- <v-col
        cols="1"
        style="min-width: 500px; max-width: 100%;"
        class="flex-grow-1 flex-shrink-0"
      > -->
      <v-row no-gutters style="height: 150px;">
      <v-container color="rgb(255, 0, 0, 0.2)">
        <!-- <v-row
      class="mb-6"
    > -->
    <!-- <v-col lg="2" cols="1"> -->
      <v-slider
        vertical
        v-model="state"
        :tick-labels ="directions"
        max="2"
        min="0"
        step="1"
        ticks="always"
        tick-size="3"
        color="white"
        dark
        height="300"
      ></v-slider>
      </v-container>
      </v-row>
      </v-flex>
      
      <!-- </v-row> -->
      <!-- </v-container> -->
      <v-flex xs4>
        <v-card id="gon">helo</v-card>
        <v-btn 
          dark
          :loading="loading"
          :disabled="loading"
          class="ma-2" 
          text icon color="orange lighten-2"
          @click= "overlay = !overlay;loader = 'loading';dir(state)">
        <v-icon color="white" >cloud_upload</v-icon>
        </v-btn>
        </v-flex>
        <v-flex>

          <!-- <v-card class="justify-end">
          <v-slider
            inverse-label
            label="Brightness"
            v-model="ljusstyrka"
            color="green"
            max="1023"
            min="4"
          ></v-slider>
          </v-card> -->

        </v-row>
        </v-flex>
      </v-card-actions>
    </v-card>
    <span v-hotkey="keymap"></span>
  </div>
   </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */
var mqtt = require("mqtt"),
  url = require("url");
let value = 0;
let mess = "";
let letters = ["b","s","f","l","r"];

export default {
  data: () => ({
  loader: null,
  loading: false,
    
    directions: [
          'Backwards',
          'Stop',
          'Forward',
        ],
    
    switchy: 0,
    state: 1,
    absolute: true,
    opacity: 1,
    overlay: false,
    onoff_btn: false,
    connected: false,
    client: undefined,
    user: "saga.sellin@abbindustrigymnasium.se",
    pass: "MQTTPAS",
    message: ""
  }),
  
  created() {
    //vad som ska hända när hemsidan först öppnas/startas
    this.connect();
    setInterval(() => {
      this.connect();
      console.log(this.connected); //under testningen behövdes denna så att användaren kunde se i konsollen ifall webbsidan connectat
      // console.log("helo");
    }, 2000); //webbsidan försöker ansluta varannan sekund för att motverka avbrott
    // console.log("heloo");
    this.dir();
    setInterval(() => {
      this.dir();
      // console.log("helooo");
    }, 100);
  },
  watch: {
        loader () {
          const l = this.loader
          this[l] = !this[l]

          setTimeout(() => (this[l] = false), 500)

          this.loader = null
        },
      },
  methods: {
    connect() {
      // funktionen som styr själva processen att connecta till vår databas
      var mqtt_url = "maqiatto.com";
      var url = "mqtt://" + mqtt_url;
      var options = {
        port: 8883,
        clientId:
          "mqttjs_" +
          Math.random()
            .toString(16)
            .substr(2, 8), //i och med detta skapas ett slumpmässigt client id
        username: this.user,
        password: this.pass
      };

    //   console.log("connecting");
      this.client = mqtt.connect(url, options);
    //   console.log("connected?"); //ifall webbsidan lyckats koppla upp sig syns bara "connecting, connected?", annars kommer även "disconnected"
      this.client
        .on("error", function(error) {
          console.log("disconnected");
          this.connected = false;
        //   console.log(this.Alert, this.connected);
        })
        .on("close", function(error) {
          console.log("disconnected");
          this.connected = false;
        });
      this.connected = true;
    },
    // dis(){ //för att själv orsaka avbrott för att se hur koden beter sig när det händer
    //   this.client.end()
    // },

    // send() {
    //   //i funktionen skickas sliderns värden till vår databas i vårt topic "brightness" genom client.publish
    //   this.message = this.ljusstyrka;
    //   this.client.publish(
    //     "kandes.isayas@abbindustrigymnasium.se/brightness",
    //     this.message.toString()
    //   );
    // },

  
    valueChange(chng) {
      if (chng == 1){ 
        value+=10;
      };
      if (chng == 0){
        value-=10;
        // if (value < 0){
        //   value = 0;
        // };
      };

      if (value > 1024){
        value = 1024
      };      
      this.dir();
    },
    
    dir(thestate) {
      this.mess = this.letters[thestate]+value;
      console.log(this.letters)
      console.log(value);
      this.client.publish(
        "saga.sellin@abbindustrigymnasium.se/direction",
        // this.mess
        value
      );
      },
    
      // toggle () {
      // this.show = !this.show
      // },
      // show () {
      //   this.show = true
      // },
      // hide () {
      //   this.show = false
      // }
      // signoflife(){
      //   console.log("helo")
      // },
  },
  computed: {
    keymap () {
      return {
        // 'a': signoflife()
      }
    }
  }
};
</script>

<style scoped>
#b51 {
  justify-content: center;
  align-items: center;
}
#content{
  background-image: url("https://s3.envato.com/files/236520857/MG_VH_CITY_ROAD_LOOP_PREW_500x300.jpg");
  background-size: 700px 100px;
}
#content2{
  background-image: url("https://cutewallpaper.org/21/background-full-hd-1920x1080/Download-wallpaper-1920x1080-road-marking-trees-sky-full-.jpg");
  background-size: 1920px 850px;
}
#beblack{
  color: white;
}
#gon{
  opacity: 0;
}
</style>
