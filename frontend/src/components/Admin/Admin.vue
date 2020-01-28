<template>
    <md-app-content>
        <div v-if="not_login">
            <form novalidate class="md-layout md-alignment-top-center">
                <md-card>
                    <md-card-header>
                        <div class="md-title">
                            <md-tabs class="md-transparent" md-alignment="fixed">
                                <md-tab id="tab-home" md-label="Admin Panel"></md-tab>
                            </md-tabs>
                        </div>
                    </md-card-header>
                    <md-card-content>
                        <md-field>
                            <label for="email">Email</label>
                            <md-input type="email" name="email" id="email" autocomplete="email" v-model="email"
                            />
                        </md-field>
                        <md-field>
                            <label for="password">Password</label>
                            <md-input type="password" name="password" id="password" autocomplete="password"
                                      v-model="password"
                            />
                        </md-field>
                    </md-card-content>
                    <md-card-actions class="md-layout md-alignment-top-center">
                        <md-button type="button" class="md-primary" @click="login_user">Log In</md-button>
                    </md-card-actions>
                </md-card>
            </form>
        </div>
        <div v-else>
            <md-divider></md-divider>
            <div class="md-gutter md-layout md-alignment-center">
                <md-button class="md-layout-item md-title" @click="show_part('db_show')">Database
                </md-button>
            </div>
            <md-divider></md-divider>
            <div v-if='this.db_show'>
                <md-button @click="login_user()">Refresh</md-button>
                <json-viewer :value="users"
                             copyable
                             boxed
                             sort>
                </json-viewer>
            </div>

            <md-divider></md-divider>
            <div class="md-gutter md-layout md-alignment-center">
                <md-button class="md-layout-item md-title" @click="show_part('instruments_show')">Instruments
                </md-button>
            </div>
            <md-divider></md-divider>

            <div v-if='this.instruments_show' class="md-layout md-alignment-top-left">
                <md-card>
                    <md-card-header>
                        <md-card-header-text>
                            <div class="md-title">Notification</div>
                        </md-card-header-text>
                    </md-card-header>
                    <md-card-content>
                        <md-autocomplete v-model="input_email" :md-options="users_emails">
                            <label>Email</label>
                        </md-autocomplete>
                        <md-field>
                            <label>Title</label>
                            <md-input v-model="input_title"></md-input>
                        </md-field>
                        <md-field>
                            <label>Text</label>
                            <md-input v-model="input_text"></md-input>
                        </md-field>
                    </md-card-content>
                    <md-card-actions>
                        <md-checkbox v-model="input_send_email_status">Send email</md-checkbox>
                        <md-button @click="send_notification()">Send</md-button>
                    </md-card-actions>
                </md-card>
            </div>

            <md-divider></md-divider>
            <div class="md-layout md-alignment-center">
                <md-button class="md-layout-item md-title" @click="show_part('tasks_show')">Tasks
                    ({{tasks.articles.length+tasks.titles.length}})
                </md-button>
            </div>
            <md-divider></md-divider>

            <div v-if='this.tasks_show' class="md-gutter md-layout md-alignment-top-left">
                <div v-for="title in tasks.titles">
                    <div class="md-layout-item md-small-size-100">
                        <md-card>
                            <md-card-header>
                                <md-card-header-text>
                                    <div class="md-title">Create Title (task)</div>
                                    <div class="md-subhead">{{Math.ceil((new
                                        Date(title.create_date).getTime()+day_ms- new
                                        Date())/(1000*60*60))-1}} hours remaining
                                    </div>
                                </md-card-header-text>
                            </md-card-header>
                            <md-card-content>
                                <div>Suggest: {{title.topic_suggestions}}</div>
                                <div>{{title.content_length}} words, {{title.content_type}}</div>
                            </md-card-content>
                            <md-card-actions>
                                <md-button @click="show_dialog(title)">Show task</md-button>
                            </md-card-actions>
                        </md-card>
                    </div>
                </div>

                <div v-for="article in tasks.articles">
                    <div class="md-layout-item md-small-size-100">
                        <md-card>
                            <md-card-header>
                                <md-card-header-text>
                                    <div class="md-title">Create Article (task)</div>
                                    <div class="md-subhead">{{Math.ceil((new
                                        Date(article.update_date).getTime()+day_ms*3- new
                                        Date())/(1000*60*60))-1}} hours remaining
                                    </div>
                                    <div class="md-subhead">
                                        Title: {{article.title.title_text}}
                                    </div>

                                </md-card-header-text>
                            </md-card-header>
                            <md-card-content>
                                <div>{{article.brief.content_length}} words</div>
                            </md-card-content>
                            <md-card-actions>
                                <md-button @click="show_dialog(title)">Show task</md-button>
                            </md-card-actions>
                        </md-card>
                    </div>
                </div>
            </div>

            <md-divider></md-divider>
            <div class="md-gutter md-layout md-alignment-center">
                <md-button class="md-layout-item md-title" @click="show_part('query_show')">Waiting for users actions
                    ({{users_query.length}})
                </md-button>
            </div>
            <md-divider></md-divider>

            <div v-if='this.query_show' class="md-gutter md-layout md-alignment-top-left">
                <div class="md-layout-item md-title">{{users_query}}</div>
            </div>

            <md-dialog :md-active.sync="show_dialog_flag">
                <md-dialog-title>Title creation</md-dialog-title>
                <md-dialog-content>
                    <json-viewer :value="content_modal"
                                 copyable
                                 boxed
                                 sort>
                    </json-viewer>
                    <div v-if="content_modal.try_number" class="md-title">It's {{content_modal.try_number}} try!</div>
                    <md-field>
                        <label>Title</label>
                        <md-input v-model="title_create_task.title"></md-input>
                    </md-field>
                    <md-field>
                        <label>Keywords</label>
                        <md-input v-model="title_create_task.keywords"></md-input>
                    </md-field>
                    <md-field>
                        <label>Meta description</label>
                        <md-textarea v-model="title_create_task.meta_description"></md-textarea>
                    </md-field>
                </md-dialog-content>
                <md-dialog-actions>
                    <md-button class="md-primary" @click="show_dialog_flag=false">Close</md-button>
                    <md-button class="md-primary"
                               @click="create_title(content_modal.id, content_modal.article_hash_id)">Confirm title
                    </md-button>
                </md-dialog-actions>
            </md-dialog>
        </div>
    </md-app-content>
</template>

<script>
    export default {
        name: "Admin",
        data: () => ({
            users: [],
            email: null,
            password: null,
            not_login: true,
            action_name: 'add',
            obj_name: 'user',
            country: null,
            users_emails: [],
            input_email: null,
            input_text: null,
            input_title: null,
            input_send_email_status: false,
            tasks: {
                titles: [],
                articles: []
            },
            users_query: [],
            day_ms: 86400000,

            show_dialog_flag: false,
            content_modal: {},

            instruments_show: false,
            tasks_show: false,
            db_show: false,
            query_show: false,

            title_create_task: {
                title: '',
                meta_description: '',
                keywords: ''
            }
        }),
        methods: {
            login_user() {
                // todo delete
                this.email = 'admin';
                this.password = '123';
                if (this.email && this.password) {
                    this.$api.post("/admin/login", {
                        email: this.email,
                        password: this.password
                    }).then((data) => {
                        if (data.data.result === 'success') {
                            this.users = data.data.data;
                            this.users_emails = [];
                            this.tasks = {
                                titles: [],
                                articles: []
                            };
                            this.users_query = [];
                            this.users.forEach(user => {
                                this.users_emails.push(user.email);
                                user.articles.forEach(article => {
                                    if (article.approve_title_id === null && article.titles.length < 3 && article.status === 0) {
                                        if (new Date(article.update_date).getTime() <= Date.now() + this.day_ms) {
                                            article.brief[0].article_hash_id = article.id;
                                            article.brief[0].try_number = article.titles.length + 1;
                                            this.tasks.titles.push(article.brief[0])
                                        }
                                    } else if (article.approve_title_id !== null && article.status === 2) {
                                        if (new Date(article.update_date).getTime() <= Date.now() + this.day_ms * 3) {
                                            article.brief[0].article_hash_id = article.id;
                                            article.brief[0].try_number = article.titles.length + 1;
                                            article.brief = article.brief[0];
                                            article.titles.forEach(title => {
                                                if (title.id === article.approve_title_id) {
                                                    article.title = title;
                                                }
                                            });
                                            delete article.titles;
                                            this.tasks.articles.push(article)
                                        }
                                    } else if (article.status === 1 || article.status === 5) {
                                        this.users_query.push(article.brief[0])
                                    }
                                })
                            });
                            this.not_login = false;
                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                } else {
                    this.$snotify.warning('Fill fields please')
                }

            },
            send_notification() {
                if (this.input_text && this.input_title && this.input_email) {
                    this.$api.post("/notification/create", {
                        email: this.input_email,
                        notification: {
                            title: this.input_title,
                            text: this.input_text,
                            send_email_status: false
                        }
                    }).then((data) => {
                        if (data.data.result === 'success') {
                            this.$snotify.success("Success");
                            this.login_user();
                            this.input_text = '';
                            this.input_email = '';
                            this.input_title = ''
                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                } else {
                    this.$snotify.warning('Fill fields please')
                }
            },
            create_title(brief_id, article_id) {
                if (this.title_create_task.title && this.title_create_task.keywords && this.title_create_task.meta_description) {
                    this.$api.post("/title/create", {
                        brief_id: brief_id,
                        article_id: article_id,
                        title: this.title_create_task
                    }).then((data) => {
                        if (data.data.result === 'success') {
                            this.$snotify.info('Success!');
                            this.login_user()
                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                    this.show_dialog_flag = false;
                } else {
                    this.$snotify.warning('Feel all fields')
                }
            },
            show_dialog(task) {
                this.show_dialog_flag = true;
                this.content_modal = task
            },
            show_part(part) {
                this[part] = !this[part];
            }
        },
        // todo delete
        created() {
            this.login_user();
        }
    }
</script>

<style scoped>
    .badge {
        width: 19px;
        height: 19px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;
        top: 2px;
        right: 2px;
        background: red;
        border-radius: 100%;
        color: #fff;
        font-size: 10px;
        font-style: normal;
        font-weight: 600;
        letter-spacing: -.05em;
        font-family: 'Roboto Mono', monospace;
    }
</style>