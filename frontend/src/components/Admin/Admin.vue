<template>
    <div>
        <md-app>
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
                    <json-viewer :value="users"
                                 copyable
                                 boxed
                                 sort>
                    </json-viewer>
                    <div class="md-layout md-alignment-top-left">
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
                </div>
            </md-app-content>
        </md-app>
    </div>
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
            input_send_email_status: false
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
                            this.users.forEach(user => {
                                this.users_emails.push(user.email)
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
                        } else {
                            this.$snotify.error(data.data.msg)
                        }
                    }).catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                } else {
                    this.$snotify.warning('Fill fields please')
                }
            }
        },
        // todo delete
        created() {
            this.login_user();
        }
    }
</script>

<style scoped>

</style>