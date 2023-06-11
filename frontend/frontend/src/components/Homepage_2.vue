<template>
    <div>
        <div class="nav" style="background-color: transparent;">
            <a href="./homepage_2">
                <img src="../assets/brickslogo.svg" alt="">
            </a>
            <div class="tribtn">
                <div class="btn">試用</div>
                <a href="./login_2" class="btn nav_login_btn" style="background-color: #b82c30; border-color: #b82c30; color: #ffffff;">登入</a>
                <a href="./register_2" class="btn" style="margin-right: 0px;">註冊</a>
            </div>
        </div>
        <div class="first_bg">
            <div class="slogan">
                <div class="first_line">
                    <p style="float: left;">一磚一磚</p>
                    <p style="float: right;">建<span style="letter-spacing: 0;">造</span></p>
                </div>
                <p class="second_line">你的專<span style="letter-spacing: 0;">案</span></p>
                <p class="third_line">為大學生設計的專案管理工<span style="letter-spacing: 0;">具</span></p>
                <a href="" class="try_now_first">立即試用</a>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
}

.nav {
    width: 100vw;
    height: 65px;
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
    background-color: transparent;
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

.first_bg{
    background-image: url(../assets/homepage_bg.svg);
    width: 100%;
    height: 1080px;
    background-size: cover;
    margin-top: -65px;
    background-position: top;
}

.slogan{
    width: 880px;
    height: 368px;
    position: relative;
    left: 50%;
    transform: translate(-50%);
    top: 265px;
    font-family: 'Noto Sans TC';

}

.first_line{
    font-size: 47px;
    font-weight: 400;
    height: 56.4px;
    width: 444px;
    line-height: 56.4px;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    letter-spacing: 12px;
    top: 0px;
}

.second_line{
    font-size: 93px;
    font-weight: 700;
    height: 112px;
    width: 444px;
    line-height: 112px;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    letter-spacing:24px;
    top: 68px;
}

.third_line{
    font-size: 33px;
    font-weight: 400;
    height: 40px;
    width: auto;
    line-height: 40px;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    letter-spacing: 0.25px;
    top: 200px;
}

.try_now_first{
    width: 272px;
    height: 48px;
    background-color: #b82c30;
    border-radius: 14px;
    position: absolute;
    bottom: 0px;
    left: 50%;
    transform: translate(-50%);
    text-decoration: none;
    font-size: 18px;
    font-weight: 500;
    color: white;
    line-height: 48px;
    text-align: center;
    letter-spacing: 1.25px;
}

</style>