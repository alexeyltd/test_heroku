import Snotify, {SnotifyPosition} from "vue-snotify";
import VueRouter from "vue-router";
import Vuex from "vuex";
import Vue from 'vue'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'

import routes from "./routes.js";
import App from "./App.vue";
import api from "./utils/api.js";

Vue.use(VueMaterial);
Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(Snotify, {
    toast: {
        position: SnotifyPosition.rightTop,
        timeout: 3000
    }
});

// you may call it in components with this.$api
Vue.prototype.$api = api;

const store = new Vuex.Store({
    state: {
        login: false,
        user: {
            first_name: "",
            last_name: "",
            email: ""
        },
        token: ""
    },
    mutations: {
        set_user(state, payload) {
            state.login = true;
            state.user = {
                first_name: payload.user.first_name,
                last_name: payload.user.last_name,
                email: payload.user.email
            };
            state.token = payload.token
        },
        unset_user(state) {
            state.login = false;
            state.user = {
                first_name: "",
                last_name: "",
                email: ""
            };
            state.token = ""
        }
    }
});

const router = new VueRouter({
    routes,
    mode: "history",
    scrollBehavior: () => ({y: 0})
});

new Vue({
    el: "#app",
    router,
    store,
    render: f => f(App)
});
