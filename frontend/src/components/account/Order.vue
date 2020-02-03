<template>
    <div v-if="order">
        <div class="md-title">Stage now: {{totally_status}}</div>
        <div class="md-subheader">Last update: {{order.update_date}}</div>
        <md-steppers class="md-layout md-alignment-top-center" :md-active-step.sync="active">
            <md-step id="first" md-label="Brief" md-description="Your order info here" :md-editable="true"
                     :md-done.sync="first">
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title">BRIEF</div>
                </div>
                <md-card>
                    <md-list class="md-double-line">
                        <md-subheader>{{order.id}}</md-subheader>

                        <md-list-item>
                            <div class="md-list-item-text">
                                <span class="md-title">{{order.brief[0].content_type.toUpperCase()}}</span>
                                <span>Type</span>
                            </div>
                            <div class="md-list-item-text">
                                <span class="md-title">{{array_lang[order.brief[0].content_language]}}</span>
                                <span>Language</span>
                            </div>
                            <div class="md-list-item-text">
                                <span class="md-title">{{order.brief[0].content_length}}</span>
                                <span>Words</span>
                            </div>
                            <div class="md-list-item-text">
                                <span class="md-title">{{order.price}}$</span>
                                <span>Cost</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>

                        <md-list-item>
                            <div class="md-list-item-text">
                                <span class="md-title">{{(new Date(order.brief[0].create_date)).toLocaleDateString('en-GB')}}</span>
                                <span>Created</span>
                            </div>
                            <div class="md-list-item-text">
                                <span class="md-title">{{order.brief[0].current_domain_url}}</span>
                                <span>Domain</span>
                            </div>
                            <div class="md-list-item-text">
                                <span class="md-title">{{order.brief[0].competitors}}</span>
                                <span>Competitors</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].suggested_keywords}}</span>
                                <span>Keywords</span>
                            </div>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].target_customer}}</span>
                                <span>Target customer</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].specific_requests}}</span>
                                <span>Specific</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].topic_suggestions}}</span>
                                <span>Suggestions</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].intended_result}}</span>
                                <span>Intended result</span>
                            </div>
                        </md-list-item>
                    </md-list>
                </md-card>
            </md-step>

            <md-step id="second" md-label="Order" md-description="History of order"
                     :md-editable="true"
                     :md-done.sync="second">
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title">TITLES</div>
                </div>
                <div v-bind:key="title" v-for="title in order.titles">
                    <md-card md-with-hover v-bind:class="{ 'md-primary': title.id===order.approve_title_id }">
                        <md-ripple>
                            <md-card-header>
                                <div class="md-title">{{title.title_text}}</div>
                                <div class="md-subhead">{{title.keywords}}</div>
                            </md-card-header>
                            <md-card-content>
                                {{title.meta_description}}
                            </md-card-content>
                            <md-card-actions>
                                <div class="md-subhead">{{(new
                                    Date(title.create_date)).toLocaleDateString('en-GB')}}
                                </div>
                                <md-button v-if="order.approve_title_id===null"
                                           @click="title_approve(true, title.id)">Approve
                                </md-button>
                            </md-card-actions>
                        </md-ripple>
                    </md-card>
                </div>
                <div v-if="order.titles.length>0 && order.titles.length<3 && order.status!==0"
                     class="md-layout md-alignment-top-center">
                    <md-button v-if="order.approve_title_id===null" class="md-title"
                               @click="show_dialog_comment_flag=true">Request another (remember maximum 2 extra titles)
                    </md-button>
                </div>
                <div v-else>
                    <div class="md-layout md-alignment-top-center">
                        <md-empty-state
                                md-label="Title creation..."
                                md-description="Your title is in production">
                        </md-empty-state>
                    </div>
                </div>
            </md-step>

            <md-step id="third" md-label="Article" md-description="When article is ready"
                     :md-editable="third_editable"
                     :md-done.sync="third">
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title">ARTICLE</div>
                </div>
                <!--<p>{{order.contents}}</p>-->
                <div v-if="order.contents.length===0" class="md-layout md-alignment-top-center">
                    <md-empty-state
                            md-label="Article creation..."
                            md-description="Your article is in production">
                    </md-empty-state>
                </div>
            </md-step>
        </md-steppers>

        <md-dialog :md-active.sync="show_dialog_comment_flag">
            <md-dialog-title>Preferences</md-dialog-title>
            <md-dialog-content>
                <div class="md-subhead">Say us what's wrong!
                </div>
                <md-field>
                    <label>Commentary</label>
                    <md-textarea v-model="comment"></md-textarea>
                </md-field>
            </md-dialog-content>
            <md-dialog-actions>
                <md-button class="md-primary" @click="title_approve(false, null)">Continue
                </md-button>
            </md-dialog-actions>
        </md-dialog>
    </div>
</template>

<script>

    export default {
        name: 'Order',
        data: () => ({
            order: null,
            comment: null,
            show_dialog_comment_flag: false,
            totally_status: '',

            active: 'second',
            first: true,
            second: true,
            second_editable: false,
            third: false,
            third_editable: false,

            array_lang: {
                'en': 'English'
            },
        }),
        methods: {
            get_order(id) {
                this.$api.post("/article/get", {
                    email: this.user.email,
                    id: id
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.order = data.data.data;

                        if (this.order.status === 0) {
                            this.totally_status = this.order.titles.length + 1 + ' title creation.'
                        } else if (this.order.status === 1) {
                            this.totally_status = 'Need to choose title.'
                        } else if (this.order.status === 2) {
                            this.totally_status = 'Article creation.'
                        } else if (this.order.status === 5) {
                            this.totally_status = 'Need to approve/dis article.'
                        } else if (this.order.status === 6) {
                            this.totally_status = 'Article already complete!'
                        }

                        if (this.order.status > 1) {
                            this.third = true;
                            this.third_editable = true;
                            this.active = 'third'
                        }
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });
            },
            title_approve(approve, title_id) {
                this.$api.post("/article/title/approve", {
                    email: this.user.email,
                    approve: approve,
                    order_id: this.order.id,
                    title_id: title_id,
                    comment: this.comment
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.$snotify.info('Success');
                        this.get_order(this.$route.params.order_id)
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });
            },
            // content_approve(approve, content_id) {
            //     if (approve === false) {
            //         this.show_dialog_comment_flag = true
            //     }
            //     this.$api.post("/article/content/approve", {
            //         email: this.user.email,
            //         approve: approve,
            //         order_id: this.order.id,
            //         content_id: content_id,
            //         comment: this.comment
            //     }).then((data) => {
            //         if (data.data.result === 'success') {
            //             this.$snotify.info('Success');
            //             this.$router.push('/orders')
            //         } else {
            //             this.$snotify.error(data.data.msg)
            //         }
            //     }).catch(e => {
            //         this.$snotify.error(`Error status ${e.response.status}`);
            //     });
            // }
        },
        created() {
            this.user = this.$store.state.user;
            this.get_order(this.$route.params.order_id)
        }
    }

</script>

<style>

</style>