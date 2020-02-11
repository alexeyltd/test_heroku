<template>
    <div v-if="order" class="container">
        <md-card>
            <md-card-header>
                <div class="md-layout md-alignment-top-center md-title">Stage now: {{totally_status}}
                </div>
                <div v-if="status_time>0" class="md-layout md-alignment-top-center md-subhead">Hours remaining:
                    {{status_time}}
                </div>
            </md-card-header>
            <md-card-content>
                <md-progress-bar md-mode="buffer" :md-value="progress_count"
                                 :md-buffer="progress_buffer"></md-progress-bar>
            </md-card-content>
        </md-card>
        <md-steppers class="md-layout md-alignment-top-center mt-2" :md-active-step.sync="active">
            <md-step id="first" md-label="Brief" md-description="Your order info here" :md-editable="true"
                     :md-done.sync="first">
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title mb-2">BRIEF</div>
                </div>
                <md-card>
                    <md-list class="md-double-line">
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.id.slice(0,8)}}</span>
                                <span>Id</span>
                            </div>
                            <div class="md-list-item-text">
                                <span>{{(new Date(order.brief[0].create_date)).toLocaleDateString('en-GB')}}</span>
                                <span>Created</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].content_type.toUpperCase()}}</span>
                                <span>Type</span>
                            </div>
                            <div class="md-list-item-text">
                                <span>{{array_lang[order.brief[0].content_language]}}</span>
                                <span>Language</span>
                            </div>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].content_length}}</span>
                                <span>Words</span>
                            </div>
                            <div class="md-list-item-text">
                                <span>{{order.price}}$</span>
                                <span>Cost</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].current_domain_url}}</span>
                                <span>Domain</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].competitors}}</span>
                                <span>Competitors</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
                            <div class="md-list-item-text">
                                <span>{{order.brief[0].suggested_keywords}}</span>
                                <span>Keywords</span>
                            </div>
                        </md-list-item>
                        <md-divider></md-divider>
                        <md-list-item>
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

            <md-step id="second" md-label="Titles" md-description="Titles here"
                     :md-editable="true"
                     :md-done.sync="second">
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title mb-2">TITLES</div>
                </div>
                <div v-if="order.status!==0">
                    <div v-bind:key="title" v-for="title in order.titles">
                        <md-card md-with-hover
                                 v-bind:class="{ 'md-primary': title.id===order.approve_title_id }">
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
                </div>
                <div v-if="order.titles.length>0 && order.titles.length<3 && order.status===1"
                     class="md-layout md-alignment-top-center">
                    <md-button class="md-title"
                               @click="show_dialog_comment_flag=true">Request another (remember maximum 2 extra titles)
                    </md-button>
                </div>
                <div v-else-if="order.status===0">
                    <div class="md-layout md-alignment-top-center">
                        <md-empty-state
                                md-label="Title creation..."
                                :md-description="'Your title is in production: '+ this.status_time+' hours remaining.' ">
                        </md-empty-state>
                    </div>
                </div>
            </md-step>

            <md-step id="third" md-label="Article" md-description="Whole set for now"
                     :md-editable="third_editable"
                     :md-done.sync="third">
                <div class="md-layout md-alignment-top-center">
                    <div class="md-title mb-2">ARTICLE</div>
                </div>
                <div v-if="order.status===2" class="md-layout md-alignment-top-center">
                    <md-empty-state
                            md-label="Article creation..."
                            :md-description="'Your article is in production: '+ this.status_time+' hours remaining.' ">
                    </md-empty-state>
                </div>
                <div v-else-if="order.status<2" class="md-layout md-alignment-top-center">
                    <md-empty-state
                            md-label="Before choose a title!"
                            md-description="Need to approve title firstly">
                    </md-empty-state>
                </div>
                <div v-else>
                    <div v-if="order.status===5" class="md-layout md-alignment-top-center">
                        <md-button class="md-primary" :md-ripple="false"
                                   @click="content_approve(true, order.contents[order.contents.length-1].id)">Approve
                            article
                        </md-button>
                        <md-button class="md-accent" :md-ripple="false"
                                   @click="show_dialog_comment_flag=true">Reject article
                        </md-button>
                    </div>
                    <div v-else class="md-layout md-alignment-top-center">
                        <a class="md-button md-primary" :href="'/api/v1/files/zip/'+order.id+'.zip'" :md-ripple="false">Download
                            archive with article (html, txt, img)
                        </a>
                    </div>
                    <md-card v-if="order.status!==2">
                        <md-card-header class="">
                            <div class="md-title md-layout md-alignment-top-center"> {{order.titles[0].title_text}}
                            </div>
                            <div class="md-subhead md-layout md-alignment-top-center"> {{order.titles[0].keywords}}
                            </div>
                            <div class="md-subhead md-layout md-alignment-top-center">
                                {{order.titles[0].meta_description}}
                            </div>
                        </md-card-header>
                        <md-card-media><img :src="'/api/v1/files/img/'+order.id+'.jpg'" alt="Image">
                        </md-card-media>
                        <md-card-content>
                            <div v-html="order.contents[order.contents.length-1].html">
                            </div>
                        </md-card-content>
                    </md-card>
                </div>
            </md-step>
        </md-steppers>

        <md-dialog :md-active.sync="show_dialog_comment_flag">
            <md-dialog-title>Preferences</md-dialog-title>
            <md-dialog-content md-fullscreen>
                <div class="md-subhead">Say us what's wrong!
                </div>
                <md-field>
                    <label>Commentary</label>
                    <md-textarea v-model="comment"></md-textarea>
                </md-field>
            </md-dialog-content>
            <md-dialog-actions>
                <md-button v-if="order.status===1" class="md-primary" @click="title_approve(false, null)">Continue
                </md-button>
                <md-button v-if="order.status===5" class="md-primary" @click="content_approve(false, null)">Continue
                </md-button>
            </md-dialog-actions>
        </md-dialog>
    </div>
    <div v-else>
        <div class="md-layout md-alignment-top-center">
            <md-progress-spinner md-mode="indeterminate"></md-progress-spinner>
        </div>
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
            progress_count: 20,
            progress_buffer: 35,
            status_time: 0,
            day_ms: 86400000,

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
                            this.totally_status = this.order.titles.length + 1 + ' title creation';
                            this.progress_count = 15;
                            this.progress_buffer = 35;
                            this.status_time = Math.ceil((new Date(this.order.update_date).getTime() + this.day_ms - new Date()) / (1000 * 60 * 60)) - 1
                        } else if (this.order.status === 1) {
                            this.totally_status = 'Need to choose title';
                            this.progress_count = 35;
                            this.progress_buffer = 60;
                        } else if (this.order.status === 2) {
                            this.progress_count = 60;
                            this.progress_buffer = 80;
                            this.totally_status = 'Article creation';
                            this.status_time = Math.ceil((new Date(this.order.update_date).getTime() + this.day_ms * 3 - new Date()) / (1000 * 60 * 60)) - 1

                        } else if (this.order.status === 5) {
                            this.progress_count = 80;
                            this.progress_buffer = 100;
                            this.totally_status = 'Need to approve/dis article'
                        } else if (this.order.status === 6) {
                            this.progress_count = 100;
                            this.totally_status = 'Article already complete'
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
                this.show_dialog_comment_flag = false;
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
            content_approve(approve, content_id) {
                this.show_dialog_comment_flag = false;

                this.$api.post("/article/content/approve", {
                    email: this.user.email,
                    approve: approve,
                    order_id: this.order.id,
                    content_id: content_id,
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
        },
        created() {
            this.user = this.$store.state.user;
            this.get_order(this.$route.params.order_id)
        },
    }

</script>

<style>

</style>