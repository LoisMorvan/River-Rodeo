<template>
  <div class="poker-table" v-if="user">
    <button @click="quit" class="quit-button">Quitter</button>
    <h1 class="game-id">Game ID: {{ this.id }}</h1>
    <div class="table-container">
      <div class="table">
        <img src="@/assets/poker-table.png" alt="Poker Table" class="table-image" />
        <div class="chair" v-for="chair in chairs" :key="chair.id" :style="getChairStyle(chair.id)">
          <div class="chair-container">
            <img src="@/assets/chair.png" alt="Chair" class="chair-image" />
          </div>
          <div class="player-info" :style="getPlayerInfoStyle(chair.id)">
            <span v-if="chair.player">{{ chair.player.username }}</span>
            <span v-else>Empty</span>
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

<script>
import api from '@/axiosInstances';

export default {
  data() {
    return {
      user: null,
      party: null,
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
    Promise.all([this.fetchUser(), this.fetchParty()])
      .then(() => {
        console.log('Rotation started');
        this.rotateChairs();
      })
      .catch((error) => {
        console.error('Error fetching user and party:', error);
      });
  },
  props: {
    id: {
      type: [String, Number],
      required: true
    }
  },
  methods: {
    fetchUser() {
      api
        .get(`/auth/user`)
        .then((response) => {
          this.user = response.data;
        })
        .catch((error) => {
          console.error('Error fetching user:', error);
        });
    },
    fetchParty() {
      const payload = { partyId: this.id };
      api
        .get(`/party/${this.id}/`)
        .then((response) => {
          this.party = response.data;
          this.updateChairPlayers();
        })
        .catch((error) => {
          console.error('Error fetching user:', error);
        });
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
      this.$router.push('/');
      api
        .post(`/party/quit/${this.id}/`)
        .then(() => {
          console.log('Quit party');
        })
        .catch((error) => {
          console.error('Error quitting party:', error);
        });
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
    },
    getPlayerInfoStyle(chairId) {
      const offsets = {
        2: { top: '0%', left: '60%' },
        3: { top: '10%', left: '105%' },
        4: { top: '40%', left: '110%' },
        5: { top: '75%', left: '108%' },
        6: { top: '100%', left: '85%' },
        7: { top: '100%', left: '60%' },
        8: { top: '100%', left: '35%' },
        9: { top: '73%', left: '-10%' },
        10: { top: '40%', left: '-14%' },
        11: { top: '10%', left: '14%' }
      };
      return {
        top: offsets[chairId].top,
        left: offsets[chairId].left,
        transform: 'translate(-50%, -50%)'
      };
    },
    updateChairPlayers() {
      // Mettre à jour les joueurs sur les chaises en fonction des données de la partie
      if (this.party && this.party.user_usernames) {
        this.chairs.forEach((chair, index) => {
          if (index < this.party.user_usernames.length) {
            chair.player = { username: this.party.user_usernames[index] };
          } else {
            chair.player = null;
          }
        });
      }
    },
    rotateChairs() {
      if (!this.user) {
        console.warn('User is not yet defined. Waiting for user data...');
        setTimeout(() => this.rotateChairs(), 500); // Réessayer après un court délai
        return;
      }

      // Trouver l'index de la chaise où se trouve l'utilisateur actuel
      let userChairIndex = this.chairs.findIndex(
        (chair) => chair.player && chair.player.username === this.user.username
      );

      if (userChairIndex === -1) {
        console.warn('User is not seated in any chair. Unable to rotate.');
        return;
      }

      // Calculer le décalage nécessaire pour que l'utilisateur soit sur le siège 5
      let offset = 5 - userChairIndex;

      // Effectuer la rotation circulaire des chaises en tenant compte de l'offset
      this.chairs = this.chairs.map((chair, index) => {
        let newIndex = (index + offset + this.chairs.length) % this.chairs.length;
        return {
          ...chair,
          player: index === 4 ? this.chairs[userChairIndex].player : this.chairs[newIndex].player
        };
      });
    }
  }
};
</script>

<style scoped>
.player-info {
  position: absolute;
  top: 50%;
  left: 120%;
  transform: translate(-50%, -50%);
  background-color: #333;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
}

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
