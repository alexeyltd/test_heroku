<template>
    <div>
        <div v-if="this.login">
            <div v-if="this.user.confirm_status===1">
                <div v-if="orders.length===0">
                    <div class="md-layout md-alignment-top-center">
                        <md-empty-state
                                md-label="Create your first brief"
                                md-description="Creating brief.">
                        </md-empty-state>
                    </div>
                </div>
                <div class="md-layout md-alignment-bottom-center mb-3">
                    <md-button class="md-primary md-raised btn-lg" @click="form_show=true">
                        Create new brief
                    </md-button>
                </div>
            </div>
            <div v-else>
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title">Confirm your account!</div>
                </div>
            </div>

            <md-dialog :md-active.sync="form_show">
                <md-dialog-content>
                    <div class="md-layout md-gutter">
                        <div class="md-layout-item md-small-size-100">
                            <md-field>
                                <label>Content type</label>
                                <md-select v-model="form.content_type"
                                           :disabled="sending">
                                    <md-option value="article">Article</md-option>
                                    <md-option value="product_description" disabled="true">Product Description (soon)
                                    </md-option>
                                    <md-option value="guest_posting" disabled="true">Guest Posting (soon)</md-option>
                                </md-select>
                            </md-field>
                        </div>
                        <div class="md-layout-item md-small-size-100">
                            <md-field>
                                <label>Language</label>
                                <md-select v-model="form.content_language"
                                           :disabled="sending">
                                    <md-option value="en">English</md-option>
                                    <md-option value="sp" disabled="true">Spanish (soon)</md-option>
                                    <md-option value="ge" disabled="true">Germany (soon)</md-option>
                                    <md-option value="fr" disabled="true">French (soon)</md-option>
                                </md-select>
                            </md-field>
                        </div>
                    </div>
                    <md-field>
                        <label>Current domain url</label>
                        <md-input v-model="form.current_domain_url"></md-input>
                        <md-tooltip md-direction="bottom">Enter your blog/domain URL, so that our writers can see what
                            your
                            company does and study some examples of your copywriting style and tone of voice.
                        </md-tooltip>
                        <div class="md-helper-text">example.com</div>
                    </md-field>
                    <md-field>
                        <label>Topic suggestions</label>
                        <md-input v-model="form.topic_suggestions" md-autogrows></md-input>
                        <md-tooltip md-direction="bottom">Enter a topic your article/content should be focused on. What
                            do
                            you want to describe with this piece?
                        </md-tooltip>
                    </md-field>
                    <md-field>
                        <label>Intended result</label>
                        <md-textarea v-model="form.intended_result" md-autogrow></md-textarea>
                        <md-tooltip md-direction="bottom">Describe what you expect from people after they read your
                            article/content. What are the steps they should take? What emotions should your content
                            convey
                            to your readers?
                        </md-tooltip>
                    </md-field>
                    <md-field>
                        <label>Target customer</label>
                        <md-input v-model="form.target_customer"></md-input>
                        <md-tooltip md-direction="bottom">Describe the target audience for this article/content. Which
                            people do you want to reach with this piece?
                        </md-tooltip>
                    </md-field>
                    <md-chips class="md-primary pulse-on-error" v-model="form.suggested_keywords"
                              md-placeholder="Add key words (optional)" md-check-duplicated></md-chips>
                    <md-field>
                        <label>Specific requests and instructions (optional)</label>
                        <md-input v-model="form.specific_request" md-autogrow></md-input>
                        <md-tooltip md-direction="bottom">Make a note of specific things to mention or avoid in this
                            piece.
                            You can also tell us about competitors that you don’t want to mention.
                        </md-tooltip>
                    </md-field>
                    <md-field>
                        <label>Competitors (optional)</label>
                        <md-input v-model="form.competitors" md-autogrow></md-input>
                        <md-tooltip md-direction="bottom">Mention your main competitors, so that our writers can take a
                            look
                            at what they do and write about.
                        </md-tooltip>
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
                    </div>
                </md-dialog-content>
                <md-dialog-actions>
                    <div class="md-layout  md-alignment-top-center">
                        <div class="md-title">{{form.content_length*0.01}}$</div>
                    </div>
                    <md-button type="button" class="md-primary"
                               @click="create_brief" :disabled="sending">Create brief
                    </md-button>
                </md-dialog-actions>
            </md-dialog>
            <div v-if="orders.length>0 && !load_state">
                <div class="md-layout md-alignment-top-center">
                    <md-table v-model="orders" md-sort="domain" md-sort-order="asc" md-card>
                        <md-table-toolbar>
                            <h1 class="md-title">Your orders</h1>
                        </md-table-toolbar>
                        <md-table-row slot="md-table-row" slot-scope="{ item }">
                            <md-table-cell md-label="Brief" md-sort-by="brief">{{ item.id.slice(0,8)}}
                            </md-table-cell>
                            <md-table-cell md-label="Domain" md-sort-by="domain">{{ item.brief[0].current_domain_url }}
                            </md-table-cell>
                            <md-table-cell md-label="Words" md-sort-by="price">{{item.brief[0].content_length}} words
                            </md-table-cell>
                            <md-table-cell md-label="Status" md-sort-by="status">
                                {{status_table[item.status]}}
                            </md-table-cell>
                            <md-table-cell md-label="Create date" md-sort-by="create_date">{{(new
                                Date(item.create_date)).toLocaleDateString('en-GB')}}
                            </md-table-cell>
                            <md-table-cell md-label="" md-sort-by="title3">
                                <md-button @click="go_order(item)">More</md-button>
                            </md-table-cell>
                        </md-table-row>
                    </md-table>
                </div>
            </div>
            <div class="md-layout md-alignment-top-center">
                <md-progress-spinner v-if="load_state" md-mode="indeterminate"></md-progress-spinner>
            </div>
        </div>
        <div v-else>
            <div class="md-layout md-alignment-top-center">
                <md-empty-state
                        md-icon="Login"
                        md-label="Sign in account"
                        md-description="For creating brief you need to login.">
                    <md-button to="/login" class="md-primary md-raised">Login</md-button>
                </md-empty-state>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapState} from 'vuex';

    export default {
        name: "My_orders",
        data: () => ({
            form_show: false,
            text_form_show: '+',
            orders: [],
            status_table: {
                0: 'Title creation',
                1: 'Title approve',
                2: 'Article creation',
                5: 'Article approve',
                6: 'Complete'
            },
            form: {
                content_type: 'article',
                content_language: 'en',
                current_domain_url: '',
                content_length: 500,
                topic_suggestions: '',
                intended_result: '',
                target_customer: '',
                suggested_keywords: ['Example keyword'],
                specific_request: '',
                competitors: ''
            },
            sending: false,
            load_state: false
        }),
        methods: {
            get_orders() {
                this.load_state = true;
                this.$api.post("/article/get", {
                    email: this.user.email,
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.orders = data.data.data;
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                    this.load_state = false;
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                    this.load_state = false;

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
                this.form_show = false;
                this.form.suggested_keywords = this.form.suggested_keywords.join('; ');
                this.$api.post("/brief/create", {
                    email: this.user.email,
                    brief: this.form
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.$snotify.info('Brief created!');
                        this.get_orders();
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });
                this.clear_form();
                this.form.suggested_keywords = [];
            },
            go_order(order) {
                this.$router.push({
                    path: 'order/' + order.id,
                })
            },
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