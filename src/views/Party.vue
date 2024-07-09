<script>
export default {
  data() {
    return {
      chairs: [
        { id: 2, player: null },
        { id: 3, player: null },
        { id: 4, player: null },
        { id: 5, player: null },
        { id: 6, player: null },
        { id: 7, player: null },
        { id: 8, player: null },
        { id: 9, player: null },
        { id: 10, player: null }
      ],
      betAmount: 0
    };
  },
  mounted() {
    console.log('Party ID:', this.id);
    // Utilisez this.id pour charger les détails de la partie à partir de l'API, par exemple
  },
  props: {
    id: {
      type: [String, Number],
      required: true
    }
  },
  methods: {
    sit(chairId) {
      console.log(`Sitting on chair ${chairId}`);
    },
    fold() {
      console.log('Fold');
    },
    call() {
      console.log('Call');
    },
    allIn() {
      console.log('All In');
    },
    raise() {
      console.log(`Raise: ${this.betAmount}`);
    },
    quit() {
      console.log('Quit');
    },
    getChairStyle(chairId) {
      const chairPositions = [
        { top: '0%', left: '50%' },
        { top: '10%', left: '95%' },
        { top: '40%', left: '100%' },
        { top: '75%', left: '98%' },
        { top: '100%', left: '75%' },
        { top: '100%', left: '50%' },
        { top: '100%', left: '25%' },
        { top: '73%', left: '0%' },
        { top: '40%', left: '-4%' },
        { top: '10%', left: '4%' }
      ];

      return {
        top: chairPositions[chairId - 1].top,
        left: chairPositions[chairId - 1].left,
        transform: 'translate(-50%, -50%)'
      };
    }
  }
};
</script>

<template>
  <div class="poker-table">
    <button @click="quit" class="quit-button">Quitter</button>
    <h1 class="game-id">Game ID: {{ this.id }}</h1>
    <div class="table-container">
      <div class="table">
        <img src="@/assets/poker-table.png" alt="Poker Table" class="table-image" />
        <div class="chair" v-for="chair in chairs" :key="chair.id" :style="getChairStyle(chair.id)">
          <div class="chair-container">
            <img src="@/assets/chair.png" alt="Chair" class="chair-image" />
            <button @click="sit(chair.id)" class="sit-button">Sit</button>
          </div>
        </div>
        <div class="dealer">
          <img src="@/assets/dealer.png" alt="Dealer" class="dealer-image" />
        </div>
      </div>
    </div>
    <div class="controls">
      <button @click="fold">Fold</button>
      <button @click="call">Call</button>
      <button @click="allIn">All In</button>
      <div class="raise-control">
        <input type="range" v-model="betAmount" min="0" max="1000" />
        <span>{{ betAmount }}</span>
        <button @click="raise">Raise</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.poker-table {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #2b2b2b;
  color: white;
  position: relative;
}

.quit-button {
  position: absolute;
  top: 20px;
  left: 20px;
  padding: 10px 20px;
  background-color: #ff4500;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.quit-button:hover {
  background-color: #ff6347;
}

.game-id {
  position: absolute;
  top: 20px;
  right: 20px;
}

.table-container {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin-bottom: 20px;
}

.table {
  width: 100%;
  padding-bottom: 50%;
  position: relative;
}

.table-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
}

.chair {
  position: absolute;
}

.chair-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.chair-image {
  width: 100px;
  height: 100px;
}

.sit-button {
  position: absolute;
  padding: 5px 10px;
  background-color: #ff4500;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.sit-button:hover {
  background-color: #ff6347;
}

.dealer {
  position: absolute;
  top: -11%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.dealer-image {
  width: 150px; /* Ajustez la taille selon vos besoins */
  height: auto; /* Conserve les proportions de l'image */
}

.controls {
  display: flex;
  gap: 10px;
  position: absolute;
  bottom: 20px;
  right: 20px;
}

.raise-control {
  display: flex;
  align-items: center;
  gap: 10px;
}

button {
  padding: 10px 20px;
  background-color: #ff4500;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #ff6347;
}
</style>
