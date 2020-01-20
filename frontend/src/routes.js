import Index from "./components/Index.vue";
import Login from './components/login/Login.vue';
import Account from "./components/account/Account";
import My_orders from "./components/account/My_orders";
import Products from "./components/Products";
import Faq from "./components/Faq";
import Dashboard from "./components/account/Dashboard";
import Settings from "./components/account/Settings";
import Notifications from "./components/account/Notifications";


const routes = [
    {
        path: "/",
        component: Index,
        name: "indexPage",
        meta: {}
    },
    {
        path: "/login",
        component: Login,
        name: "loginPage",
        meta: {}
    },
    {
        path: "/account",
        component: Account,
        name: "accountPage",
        meta: {}
    },
    {
        path: "/orders",
        component: My_orders,
        name: "ordersPage",
        meta: {}
    }, {
        path: "/products",
        component: Products,
        name: "productsPage",
        meta: {}
    },
    {
        path: "/faq",
        component: Faq,
        name: "faqPage",
        meta: {}
    },
    {
        path: "/dashboard",
        component: Dashboard,
        name: "dashboardPage",
        meta: {}
    },
    {
        path: "/notification",
        component: Notifications,
        name: "notificationPage",
        meta: {}
    },
    {
        path: "/settings",
        component: Settings,
        name: "settingsPage",
        meta: {}
    },

];

export default routes;