<template>
    <section>
        <div class="container">
            <header class="section page-header page-header-2">
                <section class="section parallax-container "
                         data-parallax-img="images/bg-image-3.jpg">
                    <div class="parallax-content">
                        <!-- FScreen-->
                        <div class="page-header-2-inner">
                            <div class="container">
                                <div class="row row-50 justify-content-between align-items-center">
                                    <div class="col-md-7">
                                        <div class="unit unit-spacing-2 page-header-2-inner-aside">
                                            <div class="unit-body wow clipInLeft">
                                                <h2 class="heading-mod-1"><span class="font-weight-extra-black">We Provide Quality Content Writing Services</span><br><span
                                                        class="font-weight-extra-light">for growing your business</span>
                                                </h2>
                                            </div>
                                        </div>
                                        <h4 class="text-default wow clipInLeft" data-wow-delay=".1s">At OrderLoo, we
                                            provide SEO Optimised <br class="d-none d-sm-block">blog/article posts and
                                            product descriptions in < 24hours. </h4> <a
                                            class="button button-secondary button-shadow button-winona wow clipInLeft"
                                            href="#works" data-wow-delay=".2s" style="margin-top: 20px;">Learn
                                        More</a>
                                    </div>
                                    <div class="col-md-5 d-none d-md-block text-center">
                                        <div class="wow fadeIn" data-wow-delay=".22s"><img
                                                src="../images/image-1-425x512.png" alt="" width="425" height="512"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </header>
            <!-- why choose us-->
            <section class="section section-md  text-center" id="features">
                <div class="container">
                    <h3 class="wow fadeIn">Why Choose Us</h3>
                    <carousel autoplay="true" :nav="false"
                              :items="1" >
                        <article class="box-modern wow fadeIn bg-gray-100 bg-image-1" data-anime="circles-2">
                            <div class="box-modern-media">
                                <div class="box-modern-icon mdi mdi-briefcase-check"></div>
                                <svg class="box-modern-circle" width="108" height="112.72" viewBox="0 0 108 112.72">
                                    <path d="M515,1214c-35.111-14.09-39.563-53.64-27.663-74.7,13.724-24.28,56.907-48.28,87.663-28.3s4.8,42.96-9,63S554.57,1224.96,515,1214Z"
                                          transform="translate(-481.406 -1103.56)"></path>
                                </svg>
                            </div>
                            <p class="box-modern-title">Unique Content Writing</p>
                            <div class="box-modern-text">
                                <p>We seamlessly create unique content for rising to the top of search engine
                                    rankings</p>
                            </div>
                        </article>
                        <!-- Box Modern-->
                        <article class="box-modern wow fadeIn bg-gray-100 bg-image-1" data-anime="circles-2">
                            <div class="box-modern-media">
                                <div class="box-modern-icon mdi mdi-crown"></div>
                                <svg class="box-modern-circle" width="108" height="112.72" viewBox="0 0 108 112.72">
                                    <path d="M515,1214c-35.111-14.09-39.563-53.64-27.663-74.7,13.724-24.28,56.907-48.28,87.663-28.3s4.8,42.96-9,63S554.57,1224.96,515,1214Z"
                                          transform="translate(-481.406 -1103.56)"></path>
                                </svg>
                            </div>
                            <p class="box-modern-title">SEO Optimised Content</p>
                            <div class="box-modern-text">
                                <p>At OrderLoo we are dedicated to providing quality SEO Optimised Content.</p>
                            </div>
                        </article>
                        <!-- Box Modern-->
                        <article class="box-modern wow fadeIn bg-gray-100 bg-image-1" data-anime="circles-2">
                            <div class="box-modern-media">
                                <div class="box-modern-icon mdi mdi-diamond"></div>
                                <svg class="box-modern-circle" width="108" height="112.72" viewBox="0 0 108 112.72">
                                    <path d="M515,1214c-35.111-14.09-39.563-53.64-27.663-74.7,13.724-24.28,56.907-48.28,87.663-28.3s4.8,42.96-9,63S554.57,1224.96,515,1214Z"
                                          transform="translate(-481.406 -1103.56)"></path>
                                </svg>
                            </div>
                            <p class="box-modern-title">Express Shipping Services</p>
                            <div class="box-modern-text">
                                <p>We offer titles, meta descriptions and keywords in less than 24 hours</p>
                            </div>
                        </article>
                    </carousel>
                </div>
            </section>
            <!-- about us-->
            <section class="section section-md">
                <div class="container">
                    <div class="row row-50 align-items-center">
                        <div class="col-md-8 col-lg-7">
                            <h3>Get unique SEO Optimised Content with express shipping in the best market rates</h3>
                            <p class="text-gray-900">Here at OrderLoo we trully believe that time is money. Based on
                                that, our main goal is to bring to our clients unique, and SEO optimised content
                                specialised for each request with guaranteed express delivery.</p>
                        </div>
                        <div class="col-md-4 col-lg-5">
                            <div class="figure-1"><img src="../images/image-2-491x428.png" alt="" width="491"
                                                       height="428"/>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- How We Work-->
            <section class="section section-md text-center" id="works">
                <div class="container">
                    <h3>How does it work?</h3>
                    <div class="row justify-content-center justify-content-lg-between">
                        <div class="col-md-10 col-lg-5 col-xl-4">
                            <div class="section-md">
                                <h3>Order any size content for your blog or article</h3>
                                <p class="big offset-top-3">We offer high quality SEO Optimised Content for your blog or
                                    website based on your needs.</p><a
                                    class="button button-primary-outline button-winona">
                                <router-link to="/faq">View More</router-link>
                            </a>
                            </div>
                        </div>
                        <div class="col-md-10 col-lg-7">
                            <div class="timeline-classic timeline-classic_1">
                                <div class="timeline-classic-item">
                                    <div class="timeline-classic-item-inner">
                                        <div class="timeline-classic-item-decoration"></div>
                                        <p class="timeline-classic-title"><span class="text-primary">Send a brief</span>
                                        </p>
                                        <div class="timeline-classic-text">
                                            <p>Complete a form with your brief details to place an order.</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="timeline-classic-item">
                                    <div class="timeline-classic-item-inner">
                                        <div class="timeline-classic-item-decoration"></div>
                                        <p class="timeline-classic-title"><span
                                                class="text-primary">Receive a title</span></p>
                                        <div class="timeline-classic-text">
                                            <p>After your brief is sent, you’ll receive a title for your future article
                                                within 24 hours.</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="timeline-classic-item">
                                    <div class="timeline-classic-item-inner">
                                        <div class="timeline-classic-item-decoration"></div>
                                        <p class="timeline-classic-title"><span
                                                class="text-primary">Title is approved</span></p>
                                        <div class="timeline-classic-text">
                                            <p>After you approve the title, a copywriter will begin creating an article
                                                and send it to you within 3 working days.</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="timeline-classic-item">
                                    <div class="timeline-classic-item-inner">
                                        <div class="timeline-classic-item-decoration"></div>
                                        <p class="timeline-classic-title"><span class="text-primary">Download your article</span>
                                        </p>
                                        <div class="timeline-classic-text">
                                            <p>When you approve the article, you’ll be able to download the article & an
                                                image, and publish on your website.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- Subscribe to Get Notified!-->
            <section class="section section-md">
                <div class="container">
                    <div class="row row-50 justify-content-lg-between">
                        <div class="col-md-6 col-lg-6 wow clipInLeft">
                            <p class="heading heading-alternate-1">Subscribe to Get Notified!</p>
                            <p class="big">Sign up to receive updates and fresh news from us.</p>
                            <form class="rd-form rd-mailform form-inline form-shadow block-11 ot30"
                                  data-form-output="form-output-global" data-form-type="subscribe" method="post"
                            >
                                <div class="form-wrap">
                                    <input class="form-input" id="subscribe-form-email" type="email" name="email"
                                           data-constraints="@Email @Required">
                                    <label class="form-label" for="subscribe-form-email">Enter Your E-mail</label>
                                </div>
                                <div class="form-button">
                                    <button class="button button-primary button-winona" type="button">Subscribe</button>
                                </div>
                            </form>
                        </div>
                        <div class="col-md-6 col-xl-5 wow clipInLeft">
                            <p class="heading heading-alternate-1">Time to Get Started</p>
                            <p class="big">Improve your business results with OrderLoo!</p>
                            <div class="group ot30">
                                <p class="button button-secondary button-winona">
                                    <router-link to="/login">Get a Quote</router-link>
                                </p>
                                <p class="button button-default-outline button-winona">
                                    <router-link to="/login">Register Now!</router-link>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </section>
</template>

<script>
    import carousel from 'vue-owl-carousel2'

    export default {
        name: "Index",
        components: {carousel}
    }
</script>

<style scoped>
    @import "../css/bootstrap.css";
    @import "../css/style.css";
</style>