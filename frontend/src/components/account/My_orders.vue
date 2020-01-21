<template>
    <md-app>
        <md-app-toolbar>
            <navbar :login="login" :user="user"></navbar>
        </md-app-toolbar>
        <md-app-content>
            <div class="md-layout md-alignment-bottom-center">
                <md-button class="md-fab md-primary" @click="show_form()">
                    <md-icon>{{text_form_show}}</md-icon>
                </md-button>
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
                <div v-for="id in card_number">
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
                            <md-button>Buy</md-button>
                        </md-card-actions>
                    </md-card>
                </div>
            </div>
        </md-app-content>
    </md-app>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: "My_orders",
        components: {Navbar},
        data: () => ({
            login: false,
            user: null,
            form_show: false,
            text_form_show: '+',
            card_number: 2,

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
                    this.card_number++;
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

            create_article() {

            },
            show_form() {
                this.form_show = !this.form_show;
                this.text_form_show = this.form_show ? '-' : '+';
            }
        },
        created() {
            this.user = this.$store.state.user;
            this.login = this.$store.state.login;
            // todo get orders
        }
    }
</script>

<style scoped>

</style>