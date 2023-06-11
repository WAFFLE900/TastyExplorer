<template>
    <div>
        <div class="nav">
            <a href="./homepage_2">
                <img src="../assets/brickslogo.svg" alt="">
            </a>
            <div class="tribtn">
                <div class="btn">試用</div>
                <a href="./login_2" class="btn nav_login_btn" style="background-color: #b82c30; border-color: #b82c30; color: #ffffff;">登入</a>
                <a href="./register_2" class="btn" style="margin-right: 0px;">註冊</a>
            </div>
        </div>
        <div class="bg">
            <div class="middle">
                <p class="title">登入</p>
                <div class="enter">
                    <input required autofocus class="account" placeholder="帳號/Email">
                    <div class="wrong"></div>
                    <input v-if="showpassword" required class="password" type="text" placeholder="密碼">
                    <input v-else required class="password" type="password" placeholder="密碼">
                    <img v-if="showpassword" id="eye_on" src="../assets/eye/eye_on.svg" alt="" @click="eyebtn">
                    <img v-else id="eye_off" src="../assets/eye/eye_origin.svg" alt="" @click="eyebtn">
                    <div class="wrong"></div>
                </div>
                <div class="login_btn">登入</div>
                <div class="keep_login">
                    <img src="../assets/checkbox/CheckBox_off.svg" class="keep_login_checkbox keep_login_checkbox_off" v-if="checked" @click="check_btn">
                    <img src="../assets/checkbox/CheckBox_on.svg" class="keep_login_checkbox keep_login_checkbox_on" v-else @click="check_btn">
                    <p style="user-select: none; cursor: pointer;" @click="check_btn">保持登入</p>
                </div>
                <div class="forget_password">忘記密碼</div>
                <div class="line">
                    <div class="left_line"></div>
                    <div class="right_line"></div>
                    <p>或</p>
                </div>
                <div class="other_resource">
                    <a href="">
                        <div>
                            <img src="../assets/Google_login.svg" alt="">
                            <p>Google 登入</p>
                        </div>
                    </a>
                    <a href="">
                        <div id="FB_login_btn">
                            <img src="../assets/FB_login.svg" alt="">
                            <p>Facebook 登入</p>
                        </div>
                    </a>
                </div>
                <div class="register">
                    <p>還沒有帳戶？</p>
                    <a href="./register_2">
                        <p>註冊</p>
                    </a>
                </div>
            </div>
        </div>
        <div class="bottom">
            <a href="" class="privacy"># <span style="text-decoration: underline;">隱私權政策</span></a>
            <a href="" class="contact"># 聯絡我們 <span style="color: #b6aeae;">bricks@gmail.com</span></a>
            <div class="photo"># Photo by <a href="https://unsplash.com/@charlesdeluvio">charlesdeluvio</a> on Unsplash
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login_2',
    data() {
        return {
            showpassword: false,
            checked: true,
        };
    },
    methods: {
        eyebtn() {
            this.showpassword = !this.showpassword;
        },
        check_btn() {
            this.checked = !this.checked;
        },
    },
    created() {

    }
}
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
}

.nav {
    width: 100vw;
    height: 65px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.nav img {
    height: 32.06px;
    width: auto;
    position: absolute;
    top: 16.47px;
    left: 5.21%;
}

.tribtn {
    width: 284px;
    height: 41px;
    position: absolute;
    top: 12px;
    right: 5.21%;
}

.btn {
    width: 76px;
    height: 39px;
    border: 1px solid #120405;
    background-color: white;
    border-radius: 10px;
    float: left;
    margin-right: 25px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    line-height: 39px;
    font-family: 'Noto Sans TC';
    text-align: center;
    letter-spacing: 1.25px;
    user-select: none;
    text-decoration: none;
    color: black;
}

.btn:hover{
    background-color: rgba(242, 238, 238, 1);
}

.nav_login_btn:hover{
    background-color: rgba(212, 128, 131, 1)!important;
}


.bg {
    background-image: url(../assets/bricks_bg.svg);
}

@media screen and (min-width: 1920px) {
    .middle {
        width: 576px;
        height: 654px;
        position: absolute;
        top: 145px;
        left: 50%;
        transform: translate(-50%);
    }

    .bg {
        height: 950px;
    }

    .privacy {
        left: 540px;
    }

    .contact {
        left: 688px;
    }

    .photo {
        right: 540px;
    }
}

@media screen and (min-width: 1600px) and (max-width: 1920px) {
    .middle {
        width: 470px;
        height: 654px;
        position: absolute;
        top: 145px;
        left: 50%;
        transform: translate(-50%);
    }

    .bg {
        height: 950px;
    }

    .privacy {
        left: 380px;
    }

    .contact {
        left: 528px;
    }

    .photo {
        right: 380px;
    }
}

@media screen and (max-width: 1600px) {
    .middle {
        width: 416px;
        height: 654px;
        position: absolute;
        top: 145px;
        left: 50%;
        transform: translate(-50%);
    }

    .bg {
        height: 770px;
    }

    .privacy {
        left: 300px;
    }

    .contact {
        left: 448px;
    }

    .photo {
        right: 300px;
    }
}

.title {
    width: 100%;
    height: 182px;
    font-size: 58px;
    text-align: center;
    font-family: 'Noto Sans TC';
    letter-spacing: -0.5px;
    font-weight: 400;
    line-height: 182px;
    user-select: none;
}

.enter {
    width: 100%;
    height: 172px;
    position: absolute;
    top: 202px;
}

input {
    width: 99.8%;
    height: 45px;
    border: 1.5px solid #c7c2c2;
    border-radius: 12px;
    font-size: 18px;
    font-family: 'Noto Sans TC';
    font-weight: 500;
    letter-spacing: 1.25px;
    text-indent: 33.5px;
}

input::placeholder {
    color: #b6aeae;
}

.wrong {
    margin-top: 6px;
    width: 92%;
    height: 22px;
}

.password {
    margin-top: 21px;
}

.enter img {
    position: absolute;
    top: 108px;
    right: 28px;
    height: 24px;
    cursor: pointer;
    z-index: 90;
    user-select: none;
}

#eye_off:hover {
    content: url(../assets/eye/eye_origin_hover.svg);
}

#eye_on:hover {
    content: url(../assets/eye/eye_on_hover.svg);
}

.login_btn {
    width: 100%;
    height: 48px;
    background-color: #b82c30;
    border-radius: 14px;
    position: absolute;
    top: 394px;
    font-size: 18px;
    font-weight: 500;
    font-family: 'Noto Sans TC';
    color: white;
    line-height: 48px;
    text-align: center;
    cursor: pointer;
    user-select: none;
}

.keep_login {
    width: 110px;
    height: 32px;
    position: absolute;
    top: 450px;
    left: 8px;
    font-size: 18px;
    font-family: 'Noto Sans TC';
    line-height: 32px;
    font-weight: 500;
    letter-spacing: 1.25px;
    text-align: right;
    color: #3b3838;
}

.keep_login_checkbox{
    float: left;
    margin-top: 7px;
    margin-left: 8px;
    cursor: pointer;
}

.keep_login_checkbox_off:hover{
    content: url(../assets/checkbox/CheckBox_off_hover.svg);
    margin-top: 2px;
    margin-left: 3px;
}

.keep_login_checkbox_on:hover{
    content: url(../assets/checkbox/CheckBox_on_hover.svg);
    margin-top: 2px;
    margin-left: 3px;
}

.forget_password {
    width: auto;
    height: 32px;
    line-height: 32px;
    color: #c65659;
    font-size: 18px;
    font-family: 'Noto Sans TC';
    position: absolute;
    top: 450px;
    right: 8px;
    cursor: pointer;
    font-weight: 500;
    user-select: none;
}

.line {
    height: 33px;
    width: 100%;
    position: relative;
    top: 307px;
    font-size: 18px;
    font-weight: 500;
    font-family: 'Noto Sans TC';
    line-height: 33px;
    color: #b6aeae;
    text-align: center;
    user-select: none;
}

.left_line {
    width: 47%;
    height: 16px;
    border-bottom: 1px solid #b6aeae;
    float: left;
}

.right_line {
    width: 47%;
    height: 16px;
    border-bottom: 1px solid #b6aeae;
    float: right;
}

.other_resource {
    width: 100%;
    height: 48px;
    position: absolute;
    top: 538px;
}

.other_resource div {
    width: 171px;
    height: 46px;
    border: 1px solid #b6aeae;
    border-radius: 14px;
    font-size: 18px;
    line-height: 46px;
    color: #b6aeae;
    font-weight: 500;
    font-family: 'Noto Sans TC';
    letter-spacing: 1.25px;
    float: left;
    position: relative;
    text-indent: 44px;
    background-color: white;
}

#FB_login_btn {
    width: 195px;
    float: right;
}

.other_resource a img {
    width: 24px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    left: 12px;
}

.register {
    width: 201px;
    height: 32px;
    position: absolute;
    bottom: 0px;
    left: 50%;
    transform: translate(-50%);
}

.register p {
    font-size: 18px;
    font-weight: 500;
    line-height: 32px;
    color: #b6aeae;
    letter-spacing: 1.25px;
    font-family: 'Noto Sans TC';
    float: left;
    margin-right: 12px;
}

.register a p {
    color: #c65659;
}

.bottom {
    width: 100vw;
    height: 65px;
    position: fixed;
    bottom: 0px;
    box-shadow: 0px -4px 8px rgba(0, 0, 0, 0.1);
    background-color: white;
}

.privacy {
    width: 116px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    cursor: pointer;
    color: #120406;
    text-decoration: none;
}

.contact {
    width: 271px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    cursor: pointer;
    color: #120406;
    text-decoration: none;
}

.photo {
    width: 357px;
    height: 23px;
    font-size: 19px;
    font-family: 'Noto Sans TC';
    line-height: 23px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    letter-spacing: 0.15px;
    color: #c7c2c2;
}

.photo a {
    color: #c7c2c2;
}
</style>