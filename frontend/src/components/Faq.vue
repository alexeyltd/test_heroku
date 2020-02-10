<template>
    <section class="section section-md">
        <div class="container">
            <div class="md-layout md-gutter">
                <md-list class="md-layout-item md-size-30">
                    <md-list-item>
                        <md-button href="#q1" class="md-primary">Go to Subpage 1</md-button>
                    </md-list-item>
                    <md-list-item>
                        <md-button href="#q2" class="md-primary">Go to Subpage 2</md-button>
                    </md-list-item>
                    <md-list-item>
                        <md-button href="#q3" class="md-primary">Go to Subpage 3</md-button>
                    </md-list-item>
                </md-list>
                <div class="md-layout-item md-size-70">
                    <md-card id='q1'>
                        <md-card-header>
                            <div class="md-title">Card without hover effect</div>
                        </md-card-header>
                        <md-card-content>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                            Dolores, sed accusantium quasi non.
                        </md-card-content>
                    </md-card>
                    <md-card id='q2'>
                        <md-card-header>
                            <div class="md-title">Card without hover effect</div>
                        </md-card-header>
                        <md-card-content>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                            Dolores, sed accusantium quasi non.
                        </md-card-content>
                    </md-card>
                    <md-card id='q3'>
                        <md-card-header>
                            <div class="md-title">Card without hover effect</div>
                        </md-card-header>
                        <md-card-content>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio.
                            Dolores, sed accusantium quasi non.
                        </md-card-content>
                    </md-card>
                </div>
            </div>
            <div class="md-layout md-alignment-top-center">
                <md-button class="md-primary" href="#">Go to begin</md-button>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: "Faq",
        data: () => ({
            login: false,
            user: null
        }),
        methods: {},
        created() {
            this.user = this.$store.state.user;
            this.login = this.$store.state.login;
        }
    }
</script>

<style scoped>
    @import "../css/bootstrap.css";
    /*@import "../css/style.css";*/
</style>