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
            <md-button @click="login_user()">Refresh</md-button>
            <md-divider></md-divider>
            <div class="md-gutter md-layout md-alignment-center">
                <md-button class="md-layout-item md-title" @click="show_part('db_show')">Database
                </md-button>
            </div>
            <md-divider></md-divider>
            <div v-if='this.db_show'>
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
                <div v-bind:key="title" v-for="title in tasks.titles">
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
                                <md-button @click="show_dialog_title(title)">Show task</md-button>
                            </md-card-actions>
                        </md-card>
                    </div>
                </div>

                <div v-bind:key="article" v-for="article in tasks.articles">
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
                                <md-button @click="show_dialog_article(article)">Show task</md-button>
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
                <div v-bind:key="item" v-for="item in users_query">
                    <div class="md-layout-item md-small-size-100">
                        <md-card>
                            <md-card-header>
                                <md-card-header-text>
                                    <div class="md-title">In work</div>
                                    <div class="md-subhead">{{item.author}}</div>
                                    <div class="md-subhead">{{item.article_id}}</div>
                                </md-card-header-text>
                            </md-card-header>
                            <md-card-content>
                                <div v-if="item.status===1">Waiting for title approve</div>
                                <div v-else>Waiting for article approve</div>
                            </md-card-content>
                        </md-card>
                    </div>
                </div>
            </div>

            <md-dialog :md-active.sync="show_dialog_flag_title">
                <md-dialog-title>Title creation</md-dialog-title>
                <md-dialog-content>
                    <json-viewer :value="content_modal"
                                 copyable
                                 boxed
                                 sort>
                    </json-viewer>
                    <div v-if="content_modal.try_number" class="md-title">It's {{content_modal.try_number}} try!
                    </div>
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
                    <md-button class="md-primary" @click="show_dialog_flag_title=false">Close</md-button>
                    <md-button class="md-primary"
                               @click="create_title(content_modal.article_hash_id)">Confirm title
                    </md-button>
                </md-dialog-actions>
            </md-dialog>
            <md-dialog :md-active.sync="show_dialog_flag_article">
                <md-dialog-title>Article creation</md-dialog-title>
                <md-dialog-content>
                    <json-viewer :value="content_modal_article"
                                 copyable
                                 boxed
                                 sort>
                    </json-viewer>
                    <div v-if="content_modal_article.try_number" class="md-title">It's
                        {{content_modal_article.try_number}} try!
                    </div>
                    <md-field>
                        <label>Img</label>
                        <md-file @md-change="onImgUpload($event)"
                                 accept="image/*"/>
                    </md-field>
                    <md-field>
                        <label>Txt</label>
                        <md-file @md-change="onTxtUpload($event)"
                                 accept="text/plain"/>
                    </md-field>
                    <md-field>
                        <label>Html</label>
                        <md-file @md-change="onHtmlUpload($event)"
                                 accept="text/html"/>
                    </md-field>
                </md-dialog-content>
                <md-dialog-actions>
                    <md-button class="md-primary" @click="show_dialog_flag_article=false">Close</md-button>
                    <md-button class="md-primary" @click="create_article_content(content_modal_article.id)">Confirm
                        article
                    </md-button>
                </md-dialog-actions>
            </md-dialog>
        </div>
    </md-app-content>
</template>

<script>
    import _ from 'lodash';


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

            show_dialog_flag_title: false,
            content_modal: {},

            show_dialog_flag_article: false,
            content_modal_article: {},

            instruments_show: false,
            tasks_show: false,
            db_show: false,
            query_show: false,

            title_create_task: {
                title: '',
                meta_description: '',
                keywords: ''
            },
            article_create_task: {
                img: null,
                txt: null,
                html: null
            }
        }),
        methods: {
            onImgUpload(evt) {
                this.article_create_task.img = evt[0]
            },
            onTxtUpload(evt) {
                this.article_create_task.txt = evt[0]
            },
            onHtmlUpload(evt) {
                this.article_create_task.html = evt[0]
            },
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
                                            article.brief[0].user = user;
                                            article.brief[0].comment = article.comment;
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
                                        article.brief[0].status = article.status;
                                        article.brief[0].author = user.email;
                                        article.brief[0].article_id = article.id;
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
            create_title(article_id) {
                if (this.title_create_task.title && this.title_create_task.keywords && this.title_create_task.meta_description) {
                    this.show_dialog_flag_title = false;
                    this.$api.post("/title/create", {
                        article_id: article_id,
                        title: this.title_create_task
                    }).then((data) => {
                        if (data.data.result === 'success') {
                            this.$snotify.info('Success!');
                            this.login_user();
                            this.title_create_task = {
                                title: '',
                                meta_description: '',
                                keywords: ''
                            };
                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                } else {
                    this.$snotify.warning('Feel all fields')
                }
            },
            create_article_content(article_id) {
                if (this.article_create_task.txt && this.article_create_task.img && this.article_create_task.html) {
                    this.show_dialog_flag_article = false;
                    let formData = new FormData();
                    formData.append('article_id', article_id);
                    formData.append('html', this.article_create_task.html);
                    formData.append('txt', this.article_create_task.txt);
                    formData.append('img', this.article_create_task.img);
                    this.$api.post("/content/create", formData).then((data) => {
                        if (data.data.result === 'success') {
                            this.$snotify.info('Success!');
                            this.login_user();
                            this.article_create_task = {
                                img: null,
                                txt: null,
                                html: null
                            }
                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                } else {
                    this.$snotify.warning('Feel all fields')
                }
            },
            show_dialog_title(task) {
                this.show_dialog_flag_title = true;
                this.content_modal = task
            },
            show_dialog_article(article) {
                this.show_dialog_flag_article = true;
                this.content_modal_article = article;
                this.content_modal_article.try_number = article.contents.length + 1;
            },
            show_part(part) {
                this[part] = !this[part];
            },
            update: _.debounce(function (e) {
                this.article_create_task.text = e.target.value;
            }, 300)
        },
        // todo delete
        created() {
            this.login_user();
        },
    }
</script>

<style scoped>
</style>