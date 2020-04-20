import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme: {
    themes: {
      dark: {
        primary: '#FB8C00',
        accent: '#FF4081',
        secondary: '#21CFF3',
        success: '#4CAF50',
        info: '#2196F3',
        warning:'#ffe18d',
        error: '#FF5252'
      },
      light: {
        primary: '#137021',
        accent: '#ff9542',
        secondary: '#549ebb',
        success: '#5ccb67',
        info: '#4caa95',
        warning:'#ff3e95',
        error: '#FF5252'
      },
    },
  },

});