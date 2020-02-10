import Snotify, {SnotifyPosition} from "vue-snotify";
import VueRouter from "vue-router";
import Vuex from "vuex";
import Vue from 'vue'
import JsonViewer from 'vue-json-viewer';

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
// import 'vue-material/dist/theme/default-dark.css'


import routes from "./routes.js";
import App from "./App.vue";
import api from "./utils/api.js";

Vue.use(JsonViewer);
Vue.use(VueMaterial);
Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(Snotify, {
    toast: {
        position: SnotifyPosition.rightTop,
        timeout: 3000
    }
});

Vue.prototype.$api = api;

const store = new Vuex.Store({
    state: {
        login: false,
        user: {
            first_name: "",
            last_name: "",
            email: "",
            confirm_status: 0
        },
        token: ""
    },
    mutations: {
        set_user(state, payload) {
            state.login = true;
            state.user = {
                first_name: payload.user.first_name,
                last_name: payload.user.last_name,
                email: payload.user.email,
                confirm_status: payload.user.confirm_status
            };
            state.token = payload.token;
            localStorage.user = JSON.stringify(state.user);
            localStorage.login = state.login;
            localStorage.token = state.token;
        },
        unset_user(state) {
            state.login = false;
            state.user = {
                first_name: "",
                last_name: "",
                email: "",
                confirm_status: 0
            };
            state.token = "";
            localStorage.clear();
        },
        set_user_from_localstorage(state) {
            state.login = true;
            state.token = localStorage.getItem('token');
            state.user = JSON.parse(localStorage.getItem('user'))
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
