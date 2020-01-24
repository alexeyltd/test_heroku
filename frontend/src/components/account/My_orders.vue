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
                <form novalidate class="md-layout md-alignment-top-center" @submit.prevent="validateUser">
                    <md-card class="md-layout-item md-size-50 md-small-size-100">
                        <md-card-header>
                            <div class="md-title">Brief</div>
                        </md-card-header>

                        <md-card-content>
                            <div class="md-layout md-gutter">
                                <div class="md-layout-item md-small-size-100">
                                    <md-field :class="getValidationClass('firstName')">
                                        <label for="first-name">Field 1</label>
                                        <md-input name="first-name" id="first-name"
                                                  v-model="form.firstName" :disabled="sending"/>
                                    </md-field>
                                </div>

                                <div class="md-layout-item md-small-size-100">
                                    <md-field :class="getValidationClass('lastName')">
                                        <label for="last-name">Field 2</label>
                                        <md-input name="last-name" id="last-name"
                                                  v-model="form.lastName" :disabled="sending"/>

                                    </md-field>
                                </div>
                            </div>

                            <div class="md-layout md-gutter">
                                <div class="md-layout-item md-small-size-100">
                                    <md-field :class="getValidationClass('gender')">
                                        <label>Type</label>
                                        <md-select v-model="form.gender" md-dense
                                                   :disabled="sending">
                                            <md-option></md-option>
                                            <md-option value="M">Type1</md-option>
                                            <md-option value="F">Type2</md-option>
                                        </md-select>
                                    </md-field>
                                </div>

                                <div class="md-layout-item md-small-size-100">
                                    <md-field>
                                        <label>Words</label>
                                        <md-input type="number"
                                                  v-model="form.age"
                                                  min="500" max="2000" step="250" value="500"/>
                                    </md-field>
                                </div>
                                <div class="md-layout-item md-small-size-100"><div class="md-title">{{form.age*0.01}}$</div></div>
                            </div>

                            <md-field :class="getValidationClass('email')">
                                <label for="email">Field 3</label>
                                <md-input type="email" name="email" id="email" autocomplete="email" v-model="form.email"
                                          :disabled="sending"/>

                            </md-field>
                        </md-card-content>

                        <md-progress-bar md-mode="indeterminate" v-if="sending"/>

                        <md-card-actions>
                            <md-button type="submit" class="md-primary" :disabled="sending">Create brief</md-button>
                        </md-card-actions>
                    </md-card>

                    <md-snackbar :md-active.sync="userSaved">The user {{ lastUser }} was saved with success!
                    </md-snackbar>
                </form>
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
    import {validationMixin} from 'vuelidate'
    import {
        required,
        email,
        minLength,
        maxLength
    } from 'vuelidate/lib/validators'


    export default {
        name: "My_orders",
        components: {Navbar},
        data: () => ({
            form_show: false,
            text_form_show: '+',
            orders: [],

            form: {
                firstName: null,
                lastName: null,
                gender: null,
                age: 500,
                email: null,
                price: 0
            },
            userSaved: false,
            sending: false,
            lastUser: null
        }),
        methods: {
            getValidationClass(fieldName) {

            },
            clearForm() {
                this.form.firstName = null;
                this.form.lastName = null;
                this.form.age = null;
                this.form.gender = null;
                this.form.email = null
            },
            saveUser() {
                this.sending = true

                // todo api
            },
            validateUser() {

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
        validations: {
            form: {
                firstName: {
                    required,
                    minLength: minLength(3)
                },
                lastName: {
                    required,
                    minLength: minLength(3)
                },
                age: {
                    required,
                    maxLength: maxLength(3)
                },
                gender: {
                    required
                },
                email: {
                    required,
                    email
                }
            }
        },
        computed: mapState([
            'user', 'login'
        ]),
    }
</script>

<style scoped>

</style>