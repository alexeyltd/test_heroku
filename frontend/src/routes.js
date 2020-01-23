import Index from "./components/Index.vue";
import Login from './components/login/Login.vue';
import Account from "./components/account/Account";
import My_orders from "./components/account/My_orders";
import Products from "./components/Products";
import Faq from "./components/Faq";
import userRecovery from "./components/login/userRecovery";
import Order from "./components/account/Order";
import Admin from "./components/Admin/Admin";


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
        path: "/recovery",
        component: userRecovery,
        name: "recoveryPage",
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
    },
    {
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
        path: "/order/:order_id",
        component: Order,
        name: "orderPage",
        meta: {}
    },
    {
        path: "/admin",
        component: Admin,
        name: "adminPage",
        meta: {}
    },
];

export default routes;