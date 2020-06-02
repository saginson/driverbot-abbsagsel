<template>
  <v-container ma-0 pa-0>
    <v-layout row wrap>
  <div>
        
    <v-card class="justify-center" width="1920" height="850" outlined id="content2">
      <v-row no-gutters style="height: 150px;">
        <!-- Containern innehåller knapparna för att öka och sänka farten, knapparna för höger och vänster samt stopp-knappen -->
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
            <v-row>
            <v-btn
            class="white--text" 
            color="red" 
            @click="dir(1)"
            >
            <v-icon color="white" >warning</v-icon>STOPP
            </v-btn>
            <v-btn class="ma-2" 
            text icon color="orange lighten-2" 
            @click="dir(3)">
            <v-icon color="white" >arrow_back_ios</v-icon>
            </v-btn>
            
            <v-btn class="ma-2" 
            text icon color="orange lighten-2" 
            @click="dir(4)">
            <v-icon color="white" >arrow_forward_ios</v-icon>
            </v-btn>
            </v-row>
            </v-container>
            </v-row>
            
        <v-spacer></v-spacer>
        <v-card-actions>
          
          
      <v-flex xs4>
      <v-row no-gutters style="height: 150px;">
        <!-- Containern innehåller slidern -->
      <v-container color="rgb(255, 0, 0, 0.2)">
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
      
      <v-flex xs4>
        <!-- Knappen som ligger bredvid slidern för att uppdatera dess värden -->
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
let value = 700; //Används som speed, 700 är minimum då motorn annars inte orkar dra bilen
let mess = ""; //meddelandet som skickas till min topic, t.ex. f700


export default {
  data: () => ({
  loader: null,
  loading: false, //används för att få loader-funktionen på knappen som för vidare sliderns värden
    
    directions: [ //används för att få namn på ticksen i slidern
          'Backwards',
          'Stop',
          'Forward',
        ],
    
    state: 1, //variabeln som motsvarar värdet på slidern
    letters: ["b","s","f","l","r"], //de bokstäver som är först i "mess", ska motsvara t.ex. forward eller right
    overlay: false, //till knapparna
    connected: false, //visar ifall hemsidan connectat till mqtt
    client: undefined,
    user: "saga.sellin@abbindustrigymnasium.se",
    pass: "MQTTPAS",
  }),
  
  created() {
    //vad som ska hända när hemsidan först öppnas/startas
    this.connect();
    setInterval(() => {
      this.connect();
    }, 2000); //webbsidan försöker ansluta varannan sekund för att motverka avbrott
    
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
      // funktionen som innehåller det som behövs för att connecta till maqiatto
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

      this.client = mqtt.connect(url, options);
      this.client
        .on("error", function(error) {
          this.connected = false;
        })
        .on("close", function(error) {
          this.connected = false;
        });
      this.connected = true;
    },
  
    valueChange(chng) { //hastighetsändringen
      if (chng == 1){ 
        value+=100;
      };
      if (chng == 0){
        value-=100;
        if (value < 700){
          value = 700;
        };
      };

      if (value > 1024){
        value = 1024
      };      
      this.dir(this.state); //behövs för att inte skapa "undefined" istället för mitt senaste state
    },
    
    dir(thestate) { //lägger ihop meddelandet och publishar i mitt topic
      
      if (this.letters[thestate] == undefined) {
        this.letters[thestate] = "s";
      }
      this.mess = this.letters[thestate]+value;
      
      this.client.publish(
        "saga.sellin@abbindustrigymnasium.se/direction",
        this.mess
      );
      },
    
  },
};
</script>

<style scoped>
#b51 {
  justify-content: center;
  align-items: center;
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
