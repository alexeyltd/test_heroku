<template>
    <div class="md-layout md-alignment-top-center">
        <md-card>
            <div v-if="order.status<=1">
                <div v-if="order.status===0">
                    <div>Need to wait title {{order.titles.length+1}}</div>
                </div>
                <div v-else-if="order.status===1 && order.titles.length<3">
                    <md-card-header>
                        <div class="md-title">Title approve stage {{order.titles.length}}</div>
                    </md-card-header>
                    <md-card-content>
                        <div class="md-layout">{{order.titles[order.titles.length-1].title_text}}
                        </div>
                        <div>{{order.titles[order.titles.length-1].keywords}}</div>
                        <div>{{order.titles[order.titles.length-1].meta_description}}</div>
                    </md-card-content>
                    <md-card-actions>
                        <md-button @click="show_dialog_comment_flag=true">Reject</md-button>
                        <md-button @click="title_approve(true, order.titles[order.titles.length-1].id)">Accept
                        </md-button>
                    </md-card-actions>
                </div>
                <div v-else>
                    <div v-for="title in order.titles">
                        <md-card-header>
                            <div class="md-title">{{title.title_text}}</div>
                        </md-card-header>
                        <md-card-content>
                            <div class="md-layout">
                            </div>
                            <div>{{title.keywords}}</div>
                            <div>{{title.meta_description}}</div>
                        </md-card-content>
                        <md-card-actions>
                            <md-button @click="title_approve(true, title.id)">Accept
                            </md-button>
                        </md-card-actions>
                    </div>
                </div>
            </div>
            <div v-else>
                <div v-if="order.status>1 && order.status<5">Need to wait article {{order.contents.length+1}}
                </div>
                <div v-else-if="order.status===5 && order.contents.length<3">
                    <md-card-header>
                        <div class="md-title">Article approve stage {{order.contents.length}}</div>
                    </md-card-header>
                    <md-card-content>
                        <div class="md-layout">{{order.contents[order.contents.length-1].text}}
                        </div>
                        <div>{{order.contents[order.contents.length-1].img}}</div>
                    </md-card-content>
                    <md-card-actions>
                        <md-button @click="show_dialog_comment_flag=true">Reject</md-button>
                        <md-button @click="content_approve(true, order.contents[order.contents.length-1].id)">Accept
                        </md-button>
                    </md-card-actions>
                </div>
                <div v-else-if="order.status===5 && order.contents.length===3">
                    <div v-for="content in order.contents">
                        <md-card-header>
                            <div class="md-title">Content</div>
                        </md-card-header>
                        <md-card-content>
                            <div>{{content.text}}</div>
                            <div>{{content.img}}</div>
                        </md-card-content>
                        <md-card-actions>
                            <md-button @click="content_approve(true, content.id)">Accept
                            </md-button>
                        </md-card-actions>
                    </div>
                </div>
                <div v-else-if="order.status===6">Article already complete</div>
            </div>
        </md-card>

        <md-card v-if="show_dialog_comment_flag===true">
            <md-card-header>Commentary</md-card-header>
            <md-card-content>
                <div class="md-card-header-text">Say us what's wrong!
                </div>
                <md-field>
                    <label>Commentary</label>
                    <md-textarea v-model="comment"></md-textarea>
                </md-field>
            </md-card-content>
            <md-card-actions>
                <md-button v-if="order.status===1" class="md-primary" @click="title_approve(false, null)">Continue
                </md-button>
                <md-button v-if="order.status===5" class="md-primary" @click="content_approve(false, null)">Continue
                </md-button>
            </md-card-actions>
        </md-card>
    </div>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: 'Order',
        components: {Navbar},
        data: () => ({
            order: null,
            comment: null,
            show_dialog_comment_flag: false
        }),
        methods: {
            get_order(id) {
                this.$api.post("/article/get", {
                    email: this.user.email,
                    id: id
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.order = data.data.data;
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });
            },
            title_approve(approve, title_id) {
                if (approve === false) {
                    this.show_dialog_comment_flag = true
                }
                this.$api.post("/article/title/approve", {
                    email: this.user.email,
                    approve: approve,
                    order_id: this.order.id,
                    title_id: title_id,
                    comment: this.comment
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.$snotify.info('Success');
                        this.$router.push('/orders')
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });
            },
            content_approve(approve, content_id) {
                if (approve === false) {
                    this.show_dialog_comment_flag = true
                }
                this.$api.post("/article/content/approve", {
                    email: this.user.email,
                    approve: approve,
                    order_id: this.order.id,
                    content_id: content_id,
                    comment: this.comment
                }).then((data) => {
                    if (data.data.result === 'success') {
                        this.$snotify.info('Success');
                        this.$router.push('/orders')
                    } else {
                        this.$snotify.error(data.data.msg)
                    }
                }).catch(e => {
                    this.$snotify.error(`Error status ${e.response.status}`);
                });
            }
        },
        created() {
            this.user = this.$store.state.user;
            this.get_order(this.$route.params.order_id)
        }
    }

</script>

<style>

</style>