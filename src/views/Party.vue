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
  async mounted() {
    try {
      await this.fetchUser();
      await this.fetchParty();
      this.initializeWebSocket();
    } catch (error) {
      console.error('Error fetching user and party:', error);
    }
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
    initializeWebSocket() {
      const partyId = this.id;

      if (this.socket) {
        console.log('Closing existing WebSocket connection.');
        this.closeWebSocket();
      }
      this.socket = new WebSocket(`ws://localhost:8001/ws/poker/${partyId}/`);

      this.socket.onopen = () => {
        console.log('WebSocket connection established.');
      };

      this.socket.onmessage = (event) => {
        const message = JSON.parse(event.data);
        console.log('Message from server:', message);
        if (message.type === 'player_join') {
          console.log('New player joined the party:', message.player);
          this.fetchParty(); // Fetch party data when a new player joins
        } else if (message.action === 'update_game_state') {
          this.updateGameState(message.game_state);
        }
      };

      this.socket.onclose = (event) => {
        console.log('WebSocket connection closed:', event);
      };
    },
    updateGameState(gameState) {
      // Mettez à jour l'état de jeu localement avec les données reçues du serveur
      this.party = gameState;
      //this.updateChairPlayers();
    },
    fold() {
      console.log('Fold');
      this.sendWebSocketMessage('fold');
    },
    call() {
      console.log('Call');
      this.sendWebSocketMessage('call');
    },
    allIn() {
      console.log('All In');
      this.sendWebSocketMessage('all_in');
    },
    raise() {
      console.log(`Raise: ${this.betAmount}`);
      this.sendWebSocketMessage('raise', { betAmount: this.betAmount });
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
    sendWebSocketMessage(action, data = {}) {
      const message = {
        action: action,
        ...data
      };
      this.socket.send(JSON.stringify(message));
    },
    getChairStyle(chairId) {
      const chairPositions = [
        { top: '100%', left: '50%' },

        { top: '10%', left: '95%' }, //9e

        { top: '40%', left: '-4%' }, //2e
        { top: '73%', left: '0%' }, //3e

        { top: '100%', left: '25%' }, //4e

        { top: '100%', left: '50%' }, //5e
        { top: '100%', left: '75%' }, //6e
        { top: '75%', left: '98%' }, //7e

        { top: '40%', left: '100%' }, //8e

        { top: '10%', left: '4%' } //1e
      ];

      return {
        top: chairPositions[chairId - 1].top,
        left: chairPositions[chairId - 1].left,
        transform: 'translate(-50%, -50%)'
      };
    },
    getPlayerInfoStyle(chairId) {
      const offsets = {
        10: { top: '0%', left: '60%' }, //1e
        9: { top: '10%', left: '105%' }, //8e
        8: { top: '40%', left: '100%' }, //7e
        7: { top: '75%', left: '108%' }, //6e
        6: { top: '100%', left: '85%' }, //5e
        5: { top: '100%', left: '60%' }, //4e
        4: { top: '100%', left: '35%' }, //3e
        3: { top: '73%', left: '-10%' }, //2e
        2: { top: '40%', left: '-14%' }, //9e
        11: { top: '10%', left: '14%' }
      };
      return {
        top: offsets[chairId].top,
        left: offsets[chairId].left,
        transform: 'translate(-50%, -50%)'
      };
    },
    updateChairPlayers() {
      this.chairs.forEach((chair) => (chair.player = null));
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
      console.log('Chairs updated:', JSON.stringify(this.chairs));
      this.rotateChairs();
    },
    rotateChairs() {
      if (!this.user) {
        console.warn('User not found. Unable to rotate chairs.');
        return;
      }
      // Trouver l'index de la chaise où se trouve l'utilisateur actuel
      let userChairIndex = this.chairs.findIndex(
        (chair) => chair.player && chair.player.username === this.user.username
      );
      console.log('User chair index:', userChairIndex);

      if (userChairIndex === -1) {
        console.warn('User is not seated in any chair. Unable to rotate.');
        return;
      }

      // Calculer le décalage nécessaire pour que l'utilisateur soit sur le siège 4
      let offset = 4 - userChairIndex;
      console.log('Offset:', offset);

      // Créer une copie de la liste des chaises
      const oldChairs = this.chairs.map((chair) => ({ ...chair }));

      // Créer une nouvelle liste pour les chaises avec les joueurs réassignés
      const newChairs = [];
      for (let i = 0; i < this.chairs.length; i++) {
        let newIndex = (i + offset + this.chairs.length) % this.chairs.length;
        console.log('index:', i, 'New index:', newIndex);
        newChairs.push({
          ...this.chairs[newIndex],
          player: oldChairs[i].player
        });
        console.log('Chairs soon rotated:', JSON.stringify(this.chairs));
      }

      // Remplacer l'ancienne liste de chaises par la nouvelle
      this.chairs = newChairs;
      console.log('Chairs rotated:', JSON.stringify(this.chairs));
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
