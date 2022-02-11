<template>
  <div class="hello">
    <div v-bind:style="{gridTemplateColumns: columns_style}" class="grid-container">
  

  <div class="grid-item" v-bind:style="{backgroundColor: is_black(g)}" v-for="(g, index) in grid" :key="index">{{g}}</div>


</div>

  <div class="across" v-for="(key, index) in across_keys" :key="index"><p>{{key}}. {{across[key]}}</p></div>
  <div class="down" v-for="(key, index) in down_keys" :key="index"><p>{{key}}. {{down[key]}}</p></div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      columns: 8,
      rows: 2,
      grid: ["M","I","S","Y"," ","G","C","A",
"U","L","E"," "," ","O","H","M",
"E","K","E"," ","S","T","U","T",
" "," ","M","A"," ","H","D"," ",
"1"," "," "," "," "," "," ","U",
"A","M","I","T"," ","I","O","N",
" ","W"," ","W","E"," ","B","S",
" ","S","K","I"," ","P","O","I",
"1","1","Y","T"," ","Y","E","N"],
across: {7: 'Same as Skee.', 5: 'One of the elements which appear at the respective poles when abody is subjected to electro-chemical decomposition. Cf. Anion,Cation.', 2: 'To stutter. [Obs.] Skelton.', 0: 'An impure yellow sulphate of iron; yellow copperas orcopiapite.', 8: "The unit of value and account in Japan. Since Japan's adoptionof the gold standard, in 1897, the value of the yen has been about 50cents. The yen is equal to 100 sen.", 1: "The standard unit in the measure of electrical resistance,being the resistance of a circuit in which a potential difference ofone volt produces a current of one ampére. As defined by theInternational Electrical Congress in 1893, and by United StatesStatute, it is a resistance substantially equal to 109 units ofresistance of the C.G.S. system of electro-magnetic units, and isrepresented by the resistance offered to an unvarying electriccurrent by a column of mercury at the temperature of melting ice14.4521 grams in mass, of a constant cross-sectional area, and of thelength of 106.3 centimeters. As thus defined it is called theinternational ohm. Ohm's law (Elec.), the statement of the fact thatthe strength or intensity of an electrical current is directlyproportional to the electro-motive force, and inversely proportionalto the resistance of the circuit.", 6: 'The plural nominative case of the pronoun of the first person;the word with which a person in speaking or writing denotes a numberor company of which he is one, as the subject of an action expressedby a verb.', 3: 'But; -- used in cautionary phrases; as, "Vivace, ma non troppopresto" (i. e., lively, but not too quick). Moore (Encyc. of Music).'},
    down: {5: "One of the higher wind instruments in the modern orchestra, yetof great antiquity, having a penetrating pastoral quality of tone,somewhat like the clarinet in form, but more slender, and sounded bymeans of a double reed; a hautboy. Oboe d'amore Etym: [It., lit.,oboe of love], and Oboe di caccia Etym: [It., lit., oboe of thechase], are names of obsolete modifications of the oboe, often foundin the scores of Bach and Handel.", 0: 'To mew; to molt. [Obs.] Quarles.', 7: 'Kine. [Scot.] See Kee, Kie, and Kine.', 4: 'To deprive of sinfulness, as a sin; to make sinless. [Obs.]Feltham.'},

    }
  },


  computed: {
    columns_style: function () {
      //return this.$props.price;
            var style_text = "1fr"
            for (let i = 0; i < this.$data.columns-1; i++) {
              style_text += " 1fr";
         }
         console.log("returning" + style_text)
      return style_text
      
    },

    across_keys: function () {
      var keys = [];
for (var key in this.$data.across) {
    keys.push(key);
  
  
}
return keys
    },
    down_keys: function () {
      var keys = [];
for (var key in this.$data.down) {
    keys.push(key);
  
  
}
return keys
    }

    

  },

  methods: {
    is_black: function (string) {
      if (string == " "){
        return "black"
      }
      else{
        return "white"
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

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

.across, .down {
  position: relative;
  text-align: left;
  left: 40vw;
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
</style>
