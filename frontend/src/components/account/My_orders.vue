<template>
    <md-app>
        <md-app-toolbar>
            <navbar :login="login" :user="user"></navbar>
        </md-app-toolbar>
        <md-app-content>
            <div v-if="this.user.confirm_status===1">
                <div v-if="orders.length===0">
                    <div class="md-layout md-alignment-top-center">
                        <div class="md-title">No orders here...</div>
                    </div>
                </div>
                <div class="md-layout md-alignment-bottom-center">
                    <md-button class="md-fab md-primary" @click="show_form()">
                        <md-icon>{{text_form_show}}</md-icon>
                    </md-button>
                </div>
            </div>
            <div v-else>
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title">Confirm your account!</div>
                </div>
            </div>

            <div v-if="form_show">
                <md-card>
                    <md-card-content>
                        <md-steppers :md-active-step.sync="active" md-vertical md-linear>
                            <md-step id="first" md-label="First Step" md-description="Optional" :md-editable="false"
                                     :md-done.sync="first">
                                <p>Step 1</p>
                                <md-button class="md-raised md-primary" @click="setDone('first', 'second')">Continue
                                </md-button>
                            </md-step>

                            <md-step id="second" md-label="Second Step" :md-error="secondStepError" :md-editable="false"
                                     :md-done.sync="second">
                                <p>Step 2</p>

                                <md-button class="md-raised md-primary" @click="setDone('second', 'third')">Continue
                                </md-button>
                                <md-button class="md-raised md-primary" @click="setError()">Set error!</md-button>
                            </md-step>

                            <md-step id="third" md-label="Third Step" :md-editable="false" :md-done.sync="third">
                                <p>Step 3 </p>
                                <md-button class="md-raised md-primary" @click="setDone('third')">Done</md-button>
                            </md-step>
                        </md-steppers>
                    </md-card-content>
                </md-card>
            </div>
            <div class="md-layout md-alignment-top-center">
                <div v-for="order in orders">
                    <md-card>
                        <md-card-header>
                            <md-card-header-text>
                                <div class="md-title">Article</div>
                                <div class="md-subhead">Status</div>
                            </md-card-header-text>
                        </md-card-header>
                        <md-card-content>
                            <p>Click on button to go check order</p>
                        </md-card-content>
                        <md-card-actions>
                            <div class="md-layout md-alignment-top-center">
                                70$
                            </div>
                            <md-button @click="go_order(order)">Buy</md-button>
                        </md-card-actions>
                    </md-card>
                </div>

            </div>
        </md-app-content>
    </md-app>
</template>

<script>
    import Navbar from "../Navbar";
    import {mapState} from 'vuex';


    export default {
        name: "My_orders",
        components: {Navbar},
        data: () => ({
            form_show: false,
            text_form_show: '+',
            orders: [],

            active: 'first',
            first: false,
            second: false,
            third: false,
            secondStepError: null
        }),
        methods: {
            setDone(id, index) {
                this[id] = true;
                if (id === 'third') {
                    this.show_form();
                    this.$snotify.success('Order add!');
                    this.first = false;
                    this.second = false;
                    this.third = false;
                    this.active = 'first';
                    this.orders.push(1);
                    return;
                }
                this.secondStepError = null;

                if (index) {
                    this.active = index
                }
            },
            setError() {
                this.secondStepError = 'This is an error!'
            },
            go_order(id) {
                this.$router.push({
                    path: 'order/' + id.toString()

                })
            },
            create_article() {

            },
            show_form() {
                this.form_show = !this.form_show;
                this.text_form_show = this.form_show ? '-' : '+';
            }
        },
        computed: mapState([
            'user', 'login'
        ]),
    }
</script>

<style scoped>

</style>