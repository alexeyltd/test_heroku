<template>
    <footer class="section footer-classic">
        <div class="footer-classic-divider hr container">
            <hr/>
        </div>
        <div class="footer-classic-main">
            <div class="container">
                <div class="row row-50 justify-content-lg-between">
                    <!--<div class="col-sm-7 col-lg-3 col-xl-2">-->
                        <!--<div class="box-style-1"><a class="brand" href="index.html"><img-->
                                <!--class="brand-logo-dark" src="images/logo-default-370x84.png" alt=""-->
                                <!--width="185" height="42"/></a>-->
                            <!--<p><span style="max-width: 250px;">We provide quality marketing and PR services to our clients.</span>-->
                            <!--</p>-->
                            <!--<md-button class="md-primary"-->
                                       <!--to="/login">Sign In-->
                            <!--</md-button>-->
                        <!--</div>-->
                    <!--</div>-->
                    <!--<div class="col-sm-5 col-lg-3 col-xl-2">-->
                        <!--<h4 class="footer-classic-title">Quick Links</h4>-->
                        <!--<ul class="list footer-classic-list">-->
                            <!--<li><a href="about-us.html">About Us</a></li>-->
                            <!--<li><a href="careers.html">Careers</a></li>-->
                            <!--<li><a href="services.html">Services</a></li>-->
                        <!--</ul>-->
                    <!--</div>-->
                    <div class="col-sm-7 col-lg-5 col-xl-3">
                        <h4 class="footer-classic-title">Navigation</h4>
                        <ul class="list footer-classic-list footer-classic-list_2-cols">
                            <li><a class="md-primary">
                                <router-link to="/home">Home</router-link>
                            </a></li>
                            <li><a class="md-primary">
                                <router-link to="/login">Sign Up</router-link>
                            </a></li>
                            <li><a class="md-primary">
                                <router-link to="/privacy">Privacy politics</router-link>
                            </a></li>
                            <li><a class="md-primary">
                                <router-link to="/faq">FAQ</router-link>
                            </a></li>
                        </ul>
                    </div>
                    <div class="col-sm-5 col-lg-9 col-xl-2">
                        <h4 class="footer-classic-title">Contacts</h4>
                        <div class="row row-20 row-sm-35">
                            <div class="col-6 col-sm-12 col-lg-8 col-xl-12">
                                <div class="row row-10 text-default">
                                    <div class="col-lg-6 col-xl-12"><a href="mailto:#">info@demolink.org</a>
                                    </div>
                                    <div class="col-lg-6 col-xl-12"><a class="big" href="tel:#">+1-853-234-65</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="hr container">
            <hr/>
        </div>
        <div class="footer-classic-aside">
            <div class="container">
                <p class="rights"><span>&copy;&nbsp; </span><span
                        class="copyright-year"></span><span>&nbsp;</span><span>Exeltive</span><span>.&nbsp;</span><a
                        class="md-primary">
                    <router-link to="/privacy">Privacy politics</router-link>
                </a></p>
            </div>
        </div>
    </footer>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
    @import "../css/bootstrap.css";
    @import "../css/style.css";
</style>