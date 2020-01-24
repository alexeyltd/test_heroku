<template>
    <div id="main">
        <md-app>
            <md-app-toolbar>
                <navbar :login="$store.state.login" :user="user"></navbar>
            </md-app-toolbar>
            <md-app-content>
                {{order}}
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
            </md-app-content>
        </md-app>
    </div>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: 'Order',
        components: {Navbar},
        data: () => ({
            user: null,
            order: null,
            active: 'first',
            first: false,
            second: false,
            third: false,
            secondStepError: null,
        }),
        methods: {
            get_order() {
                return {
                    id: this.$route.params.id,
                    name: 'name',
                    title: 'title',
                    status: 'status'
                }
            },
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
        },
        created() {
            this.user = this.$store.state.user;
            this.order = this.get_order()
        }
    }

</script>

<style>

</style>