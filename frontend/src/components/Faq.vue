<template>
    <section class="section section-md">
        <div class="container">
            <div class="md-layout md-gutter">
                <md-list class="md-layout-item md-size-30">
                    <md-list-item>
                        <md-button href="#q1" class="md-primary">When ready?</md-button>
                    </md-list-item>
                    <md-list-item>
                        <md-button href="#q2" class="md-primary">How I know?</md-button>
                    </md-list-item>
                </md-list>
                <div class="md-layout-item md-size-70">
                    <md-card id='q1' class="mb-2" md-with-hover>
                        <md-card-header>
                            <md-card-header-text><strong>When will my content order be ready?</strong>
                            </md-card-header-text>
                            <md-card-expand-trigger>
                                <md-button class="md-fab md-mini md-primary">
                                    <md-icon>+</md-icon>
                                </md-button>
                            </md-card-expand-trigger>
                        </md-card-header>
                        <md-card-expand>
                            <md-card-expand-content>
                                <md-card-content>
                                    The content writing process takes two steps:
                                    ->Creating a title and meta-description takes 2 working days from placing an order
                                    with completed brief details;
                                    ->Creating a content piece takes 10 working days from your approval of the title and
                                    meta-description.
                                    Revising title and meta-description and introducing changes to the content piece
                                    takes additional time.
                                </md-card-content>
                            </md-card-expand-content>
                        </md-card-expand>
                    </md-card>
                    <md-card id='q2' class="mb-2" md-with-hover>
                        <md-card-header>
                            <md-card-header-text><strong>How will I know that my title and meta-description are ready
                                for review?</strong>
                            </md-card-header-text>
                            <md-card-expand-trigger>
                                <md-button class="md-fab md-mini md-primary">
                                    <md-icon>+</md-icon>
                                </md-button>
                            </md-card-expand-trigger>
                        </md-card-header>
                        <md-card-expand>
                            <md-card-expand-content>
                                <md-card-content>
                                    A notification will be sent to the email address that you specified during
                                    registration. Your order will also be marked as ‘Ready for Review’ on your
                                    <a class="md-primary">
                                        <router-link to="/orders">Orders</router-link>
                                    </a>
                                    .
                                </md-card-content>
                            </md-card-expand-content>
                        </md-card-expand>
                    </md-card>
                    <md-card id='q3' class="mb-2" md-with-hover>
                        <md-card-header>
                            <md-card-header-text><strong>How will I know that my content order is written and ready for
                                review?</strong>
                            </md-card-header-text>
                            <md-card-expand-trigger>
                                <md-button class="md-fab md-mini md-primary">
                                    <md-icon>+</md-icon>
                                </md-button>
                            </md-card-expand-trigger>
                        </md-card-header>
                        <md-card-expand>
                            <md-card-expand-content>
                                <md-card-content>
                                    You can request changes 3 times each for both title & meta-description and the
                                    content piece.
                                </md-card-content>
                            </md-card-expand-content>
                        </md-card-expand>
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
</style>