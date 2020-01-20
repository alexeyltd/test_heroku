<template>
    <md-app>
        <md-app-toolbar>
            <navbar :login="login" :user="user"></navbar>
        </md-app-toolbar>
        <md-app-content>
            <div class="md-layout md-alignment-top-center">
                <md-card>
                    <md-card-header>
                        <md-card-header-text>
                            <div class="md-title">Article</div>
                            <div class="md-subhead">Key words</div>
                        </md-card-header-text>
                    </md-card-header>

                    <md-card-actions>
                        <div class="md-layout md-alignment-top-center">
                            70$
                        </div>
                        <md-button>Buy</md-button>
                    </md-card-actions>
                </md-card>
                <md-card>
                    <md-card-header>
                        <md-card-header-text>
                            <div class="md-title">Article</div>
                            <div class="md-subhead">Key words</div>
                        </md-card-header-text>
                    </md-card-header>

                    <md-card-actions>
                        <div class="md-layout md-alignment-top-center">
                            70$
                        </div>
                        <md-button>Buy</md-button>
                    </md-card-actions>
                </md-card>
                <md-card>
                    <md-card-header>
                        <md-card-header-text>
                            <div class="md-title">Article</div>
                            <div class="md-subhead">Key words</div>
                        </md-card-header-text>
                    </md-card-header>

                    <md-card-actions>
                        <div class="md-layout md-alignment-top-center">
                            70$
                        </div>
                        <md-button>Buy</md-button>
                    </md-card-actions>
                </md-card>
            </div>
            <div class="md-layout md-alignment-bottom-center">
                <md-button class="md-primary">Add brief</md-button>
            </div>
        </md-app-content>
    </md-app>
</template>

<script>
    import Navbar from "../Navbar";

    export default {
        name: "My_orders",
        components: {Navbar},
        data: () => ({
            login: false,
            user: null,
        }),
        methods: {},
        created() {
            this.user = this.$store.state.user;
            this.login = this.$store.state.login;
            // todo get orders
        }
    }
</script>

<style scoped>

</style>