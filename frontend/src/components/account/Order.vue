<template>
    <div class="md-layout md-alignment-top-center">
        <md-card>
            <div v-if="order.status===0 && order.approve_title_id===null">
                <md-card-header>
                    <div class="md-title">Title in production...</div>
                </md-card-header>
                <md-card-content>
                    <div>Need to wait title {{order.titles.length+1}}</div>
                </md-card-content>
            </div>
            <div v-else-if="order.status===1 && order.approve_title_id===null">
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
                    <md-button @click="title_approve(false, null)">Reject</md-button>
                    <md-button @click="title_approve(true, order.titles[order.titles.length-1].id)">Accept</md-button>
                </md-card-actions>
            </div>
            <div v-else-if="order.status===2 && order.approve_title_id===null">
                <md-card-header>
                    <div class="md-title">Title choice stage</div>
                </md-card-header>
                <md-card-content>
                    <div>Need to choice from titles</div>
                    <div>{{order.titles}}</div>
                </md-card-content>
                <md-card-actions>
                    <md-button @click="title_approve(true, order.titles[0].id)">Choose 1</md-button>
                    <md-button @click="title_approve(true, order.titles[1].id)">Choose 2</md-button>
                    <md-button @click="title_approve(true, order.titles[2].id)">Choose 3</md-button>
                </md-card-actions>
            </div>
            <div v-else-if="order.status===2||order.status===3||order.status===4">Need to wait article</div>
            <div v-else-if="order.status===5">Need to approve article</div>
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
                this.$api.post("/article/approve/title", {
                    email: this.user.email,
                    approve: approve,
                    order_id: this.order.id,
                    title_id: title_id
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