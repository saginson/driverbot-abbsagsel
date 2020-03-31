<template>
  <div>
    <v-card class="justify-center" max-width="" max-height="" outlined>
      <v-card-actions>
        <v-row align="start" justify="space-around" no-gutters>
          <!-- <v-slider
            inverse-label
            label="Brightness"
            v-model="ljusstyrka"
            color="green"
            max="1023"
            min="4"
          ></v-slider> -->
          <!-- <v-btn @click="send">Update </v-btn> -->
          <v-switch
            label="On/Off"
            v-model="onoff_btn"
            color="green"
            @change="forward()"
          >
          </v-switch>
        </v-row>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */
var mqtt = require("mqtt"),
  url = require("url");
export default {
  data: () => ({
    // ljusstyrka: 50,
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
    //   console.log(this.connected); //under testningen behövdes denna så att användaren kunde se i konsollen ifall webbsidan connectat
    }, 2000); //webbsidan försöker ansluta varannan sekund för att motverka avbrott
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
    forward() {
      //skickar ett värde på 1 eller 0 till databas, ledstripp är av eller på
      if (this.onoff_btn == true) {
        //ifall spaken sätts på
        this.client.publish(
          "saga.sellin@abbindustrigymnasium.se/direction_forward",
          "1"
        );
        console.log("On");
      } else {
        //annars skickas 0
        this.client.publish(
          "saga.sellin@abbindustrigymnasium.se/direction_forward",
          "0"
        );
        console.log("Off");
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
</style>
