<template>
  <div class="account-view">
    <div class="tabs">
      <button :class="{ active: activeTab === 'account' }" @click="activeTab = 'account'">
        My Account
      </button>
      <button :class="{ active: activeTab === 'history' }" @click="activeTab = 'history'">
        History of the Games
      </button>
    </div>
    <div class="tab-content">
      <MyAccountComponent v-if="activeTab === 'account'" />
      <HistoryOfGamesComponent v-if="activeTab === 'history'" />
    </div>
  </div>
</template>

<script>
import MyAccountComponent from '@/components/Account/MyAccountComponent.vue';
import HistoryOfGamesComponent from '@/components/Account/HistoryOfGamesComponent.vue';

export default {
  components: {
    MyAccountComponent,
    HistoryOfGamesComponent
  },
  data() {
    return {
      activeTab: 'account'
    };
  }
};
</script>

<style scoped>
html,
body,
.account-view,
.tab-content {
  height: 100%;
  margin: 0;
  padding: 0;
}

.account-view {
  display: flex;
  flex-direction: column;
}

.tabs {
  display: flex;
  margin-bottom: 20px;
}

.tabs button {
  flex: 1;
  padding: 10px 0;
  background: none;
  border: 5px solid #cd1313;
  cursor: pointer;
  text-align: center;
  color: white;
}

.tabs button.active {
  background: #cd1313;
  border-bottom: none;
}

.tab-content {
  flex: 1;
  border: 1px solid #ddd;
  padding: 20px;
  overflow: auto;
}
</style>
