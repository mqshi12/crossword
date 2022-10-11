<template>
  <!-- eslint-disable -->

  <!-- need IDs for the individual things i think to make them clickable -->
  <div v-if="user_crossword" class="hello">
    <button class="show_answers" v-on:click="showAnswers">Show Answers</button>
    <div class="crossword_and_definitions">
      <div class="crossword_wrapper">
        <div v-for="(row, row_index) in done_crossword">
          <div
            v-bind:style="{
              backgroundColor: is_black(done_crossword[row_index][col_index]), width: get_crossword_box_dimensions(), height: get_crossword_box_dimensions(),
            }"
            class="individual_box"
            v-for="(col, col_index) in row"
          >
          
          
            <p class="grid_number">
              {{
                grid_numbers[row_index][col_index] != 0
                  ? grid_numbers[row_index][col_index] + "."
                  : " "
              }}
            </p>
            
          
            <input
              minlength="0"
              maxlength="1"
              autocomplete="off"
              v-model="user_crossword[row_index][col_index]"
              class="crossword_input_box"
            />
          </div>
        </div>
      </div>

      <div class="definitions">
        <div class="across_definitions">
          <p><b>Across:</b></p>
          <div
            class="across"
            v-for="(key, index) in Object.keys(across_definitions)"
            :key="index"
          >
            <p class="definition_p">{{ key }}. {{ across_definitions[key] }}</p>
          </div>
        </div>

        <div class="down_definitions">
          <p><b>Down:</b></p>
          <div
            class="down"
            v-for="(key, index) in Object.keys(down_definitions)"
            :key="index"
          >
            <p class="definition_p">{{ key }}. {{ down_definitions[key] }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import $ from 'jquery'
export default {
  name: "Crossword",
  props: {
    done_crossword: null,
    grid_numbers: null,
    down_definitions: null,
    across_definitions: null,
  },
  watch: {
    // whenever question changes, this function will run
    user_crossword(newCrossword, oldCrossword) {
      var temp = []
      for ( var i = 0; i < newCrossword.length; i++){
        var uppercase = newCrossword[i].map(element => {
        return element.toUpperCase();
});
        temp.push(uppercase)
      }

      //console.log("temp is", temp)
      //console.log("done_crossword is", this.$props.done_crossword)

      var crossword_done = true

      for (var a = 0; a < temp.length; a++){
        for (var b = 0; b < temp[0].length; b++){
          console.log("temp[a][b] is", temp[a][b])
          if (temp[a][b] != this.$props.done_crossword[a][b]){
            console.log("setting crossword_done to false")
            crossword_done = false
          }
        }
      }

      if (crossword_done){
        alert("Congratulations! You finished today's Mrossword!")
      }
      
    }
  },

  data() {
    return {

      /*user_crossword: [["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""]], */

    user_crossword: null,
    };
  },
  computed: {
    columns_style: function () {
      //return this.$props.price;
      var style_text = "1fr";
      for (let i = 0; i < this.$data.columns - 1; i++) {
        style_text += " 1fr";
      }
      console.log("returning" + style_text);
      return style_text;
    },
    across_keys: function () {
      var keys = [];
      for (var key in this.$data.across) {
        keys.push(key);
      }
      return keys;
    },
    down_keys: function () {
      var keys = [];
      for (var key in this.$data.down) {
        keys.push(key);
      }
      return keys;
    },
  },


  mounted: function () {

    
    console.log("iN MOUNTED OF CROSSWORD");
    
    console.log("done crossword is")
    console.log(this.$props.done_crossword)
    
    console.log("grid_numbers is", this.$props.grid_numbers)
    console.log("1, 1 is", this.$props.grid_numbers[1][1])
    
    
    this.initializeUserCrossword();
  },
  methods: {

    initializeUserCrossword: function() {
      console.log("top of initialize");
      var num_rows = this.$props.done_crossword.length;

      var num_columns = this.$props.done_crossword[0].length;
      console.log(num_rows, num_columns)
      var user_crossword_temp = []

      for(var a = 0; a < num_rows; a++){
        var t = []
        for(var i = 0; i < num_columns; i++){
          t.push("")
        }
        user_crossword_temp.push(t)
      }

    this.$data.user_crossword = user_crossword_temp;
    console.log("end of initialize", this.$data.user_crossword);
    },

    showAnswers: function() {
      this.$data.user_crossword = this.$props.done_crossword;
    },

    is_black: function (string) {
      if (string == " ") {
        return "black";
      } else {
        return "white";
      }
    },

    get_crossword_box_dimensions: function() {
      var browser_width = $(window).width()
      var total_crossword = browser_width*0.1;
      var num_rows = this.$props.done_crossword.length;
    
      var ratio = parseInt(total_crossword/num_rows)
      /*
      if (ratio > 10){
        ratio = 10
      }*/
      return ratio.toString() + 'px';
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.crossword_input_box {
  width: 25px;
  position: absolute;
  font-family: "Courier";
}
::-webkit-scrollbar {
  width: 7px;
}

button {
  background-color: transparent;
  border: 1px solid black;
  font-family: "Courier";
  font-size: 15px;
  text-decoration: underline;
  padding: 1vw;
}

button:hover {
  background-color: white;
}
/* Track */

/* Handle */
::-webkit-scrollbar-thumb {
  background: black;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.definitions {
  height: 69vh;
  border: 1px solid black;
  overflow: hidden;
  width: 35vw;
  font-family: "Monument Grotesk";
  font-weight: normal;
  line-height: 120.8%;
}

b {
  font-family: "Monument Grotesk";
  font-weight: bold;
}

.across_definitions {
  height: 34.5vh;
  border: 1px solid black;
  overflow-y: scroll;
  overflow-x: hidden;
}

.across {
  overflow-wrap: break-word;
  word-wrap: break-word;
  border-bottom: 1px solid black;
}

.down_definitions {
  height: 34.5vh;
  border: 1px solid black;
  overflow-y: scroll;
  overflow-x: hidden;
}

.down {
  overflow-wrap: break-word;
  word-wrap: break-word;
  border-bottom: 1px solid black;
}

.definition_p {
  width: 35vw;
  padding-bottom: 5px;
}

.definition_p:hover {
  background-color: white;
}

.crossword_and_definitions {
  display: flex;
}
.crossword_wrapper {
  display: flex;
}

input {
  border: none;
  background-image: none;
  background-color: transparent;
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
  font-size: 25px;
  margin-left: -8px;
  text-transform: uppercase;
}

input:focus {
  outline: none;
  border: none;
  background-image: none;
  background-color: transparent;
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
}

.grid_number {
  display: relative;
  float: left;
  font-weight: normal;
  font-size: 10px;
  margin-left: -15px;
  margin-top: -15px;
}

.individual_box {
  /*
  width: 20px;
  height: 20px;
  */
  padding: 20px;
  border: 1px solid rgba(0, 0, 0, 1);
  font-family: "Space Mono";
  font-weight: normal;
}

.grid-container {
  display: grid;
  grid-gap: 0px;
  /*grid-template-columns: auto auto auto;*/
  /*padding: 10px;*/
  position: absolute;
}
.grid-item {
  /*background-color: white;*/
  border: 1px solid rgba(0, 0, 0, 1);
  padding: 20px;
  font-size: 30px;
  text-align: center;
  width: 1vw;
  height: 1vw;
  aspect-ratio: 1;
  font-family: "Courier";
  color: black;
}
.across,
.down {
  position: relative;
  text-align: left;
  width: 40vw;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

@media only screen and (max-width: 600px) and (orientation: portrait) {
  .crossword_and_definitions {
    display: block;
  }

  .definitions {
    width: 100%;
  }

  .definition_p {
    width: 100%;  
    margin: 2vw;
  }

  .across {
    width: 100%;
  }
  .down {
    width: 100%;
  }

  .individual_box {
    width: 1px !important;
    height: 1px !important;
  }

  .crossword_input_box {
    width: 20px;
    font-size: 22px;
    margin-top: -10px;
  }


}
</style>