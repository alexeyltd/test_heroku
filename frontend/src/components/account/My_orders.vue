<template>
    <div>
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
            <form novalidate class="md-layout md-alignment-top-center">
                <md-card class="md-layout-item md-size-50 md-small-size-100">
                    <md-card-header>
                        <div class="md-title">Brief</div>
                    </md-card-header>

                    <md-card-content>
                        <div class="md-layout md-gutter">
                            <div class="md-layout-item md-small-size-100">
                                <md-field>
                                    <label>Content type</label>
                                    <md-select v-model="form.content_type"
                                               :disabled="sending">
                                        <md-option></md-option>
                                        <md-option value="article">Article</md-option>
                                    </md-select>
                                </md-field>
                            </div>
                            <div class="md-layout-item md-small-size-100">
                                <md-field>
                                    <label>Language</label>
                                    <md-select v-model="form.content_language"
                                               :disabled="sending">
                                        <md-option></md-option>
                                        <md-option value="en">English</md-option>
                                    </md-select>
                                </md-field>
                            </div>
                        </div>
                        <md-field>
                            <label>Current domain url</label>
                            <md-input v-model="form.current_domain_url"></md-input>
                        </md-field>
                        <md-field>
                            <label>Topic suggestions</label>
                            <md-input v-model="form.topic_suggestions" md-autogrows></md-input>
                        </md-field>
                        <md-field>
                            <label>Intended result</label>
                            <md-input v-model="form.intended_result" md-autogrow></md-input>
                        </md-field>
                        <md-field>
                            <label>Target customer</label>
                            <md-input v-model="form.target_customer"></md-input>
                        </md-field>
                        <md-field>
                            <label>Suggested keywords</label>
                            <md-input v-model="form.suggested_keywords"></md-input>
                        </md-field>
                        <md-field>
                            <label>Specific request(s)</label>
                            <md-input v-model="form.specific_request" md-autogrow></md-input>
                        </md-field>
                        <md-field>
                            <label>Competitors</label>
                            <md-input v-model="form.competitors" md-autogrow></md-input>
                        </md-field>
                        <div class="md-layout md-gutter">
                            <div class="md-layout-item md-small-size-100">
                                <md-field>
                                    <label>Words</label>
                                    <md-input type="number"
                                              v-model="form.content_length"
                                              min="500" max="2000" step="250" value="500"/>
                                </md-field>
                            </div>
                            <div class="md-layout-item md-small-size-100">
                                <div class="md-title">{{form.content_length*0.01}}$</div>
                            </div>
                        </div>
                    </md-card-content>

                    <md-card-actions>

                        <md-button type="button" class="md-primary"
                                   @click="create_brief" :disabled="sending">Create brief
                        </md-button>
                    </md-card-actions>
                </md-card>
            </form>
        </div>
        <div v-if="orders.length>0">
            <div class="md-layout md-alignment-top-center">
                <div v-for="order in orders">
                    <md-card>
                        <md-card-header>
                            <md-card-header-text>
                                <div class="md-title">Article</div>
                                <div class="md-subhead">{{order.id}}</div>
                            </md-card-header-text>
                        </md-card-header>
                        <md-card-content>
                            <div v-if="order.status<=1">
                                <div v-if="order.status===0">
                                    <div>Need to wait title {{order.titles.length+1}}</div>
                                </div>
                                <div v-else-if="order.status===1 && order.titles">
                                    Need to approve new title!
                                </div>
                                <div v-else>
                                    Need to choose title from 3 variants
                                </div>
                            </div>
                            <div v-else>
                                <div v-if="order.status>1 && order.status<5">Need to wait article
                                    {{order.contents.length}}
                                </div>
                                <div v-else-if="order.status===5 && order.contents.length<3">Need to approve/reject
                                    article
                                    {{order.contents.length}}
                                </div>
                                <div v-else-if="order.status===5 && order.contents.length===3">
                                    Need to choose content from 3 variants
                                </div>
                                <div v-else-if="order.status===6">Article already complete</div>
                            </div>
                        </md-card-content>
                        <md-card-actions>
                            <div class="md-layout md-alignment-top-center">
                                {{order.price}}$
                            </div>
                            <md-button @click="go_order(order)">Go</md-button>
                        </md-card-actions>
                    </md-card>
                </div>
            </div>
        </div>
    </div>
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

            form: {
                content_type: 'article',
                content_language: 'en',
                current_domain_url: '',
                content_length: 500,
                topic_suggestions: '',
                intended_result: '',
                target_customer: '',
                suggested_keywords: '',
                specific_request: '',
                competitors: ''
            },
            sending: false,
        }),
        methods: {
            get_orders() {
                this.$api.post("/article/get", {
                    email: this.user.email,
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.orders = data.data.data;
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });
            },
            clear_form() {
                this.form = {
                    content_type: 'article',
                    content_language: 'en',
                    current_domain_url: '',
                    content_length: 500,
                    topic_suggestions: '',
                    intended_result: '',
                    target_customer: '',
                    suggested_keywords: '',
                    specific_request: '',
                    competitors: ''
                }
            },
            create_brief() {
                this.$api.post("/brief/create", {
                    email: this.user.email,
                    brief: this.form
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.$snotify.info('Brief created!');
                        this.show_form();
                        // this.get_orders();
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });

            },
            go_order(order) {
                this.$router.push({
                    path: 'order/' + order.id,
                })
            },
            show_form() {
                this.clear_form();
                this.form_show = !this.form_show;
                this.text_form_show = this.form_show ? '-' : '+';
            }
        },
        computed: mapState([
            'user', 'login'
        ]),
        created() {
            this.get_orders();
        }
    }
</script>

<style scoped>

</style>