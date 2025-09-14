<template>
  <footer :class="['footer', errorInformation.code && 'is-error', menuStatus && 'is-show-menu']">
    <div class="wrap">
      <div class="link-wrap" v-if="$route.name === 'index'">
        <a
          v-for="(item, index) in links"
          :key="index"
          :href="item.url"
          :title="item.name"
          target="_blank"
        >
          {{ item.name }}
        </a>
      </div>
      <div class="copyright">
        <div class="left">
          <ul class="footer-menu">
            <li class="list">
              <a href="/">首页</a>
            </li>
            <li class="list" v-for="(item,key) in subMenu" :key="key">
              <nuxt-link
                :to="{
                  name: 'page-id',
                  params: { id: item.id }
                }"
              >
                {{ item.title }}
              </nuxt-link>
            </li>
            <li class="list">
              <nuxt-link :to="{ name: 'phrase' }">
                本站动态
              </nuxt-link>
<!--              <a href="/phrase">本站动态</a>-->
            </li>
          </ul>
          <!-- 版权文字 -->
          <a href="http://beian.miit.gov.cn/" target="_blank"><div class="copyright-text" v-html="copyright"></div></a>
        </div>
        <p class="right">Theme by <a href="https://www.xuanmo.xin/">Xuanmo</a> && <a href="https://www.github.com/fovegage">Gage</a></p>
      </div>
    </div>
    <div class="back-top" ref="backTop" @click="backTop" :class="{ show: isShowBackTop }">
      <x-icon class="icon-back-top"></x-icon>
    </div>
  </footer>
</template>
<script>
import { mapState } from 'vuex'
export default {
  name: 'AppFooter',
  data () {
    return {
      isShowBackTop: false
    }
  },
  computed: {
    ...mapState(['menuStatus', 'links', 'subMenu', 'errorInformation']),
    ...mapState({
      copyright: state => state.info.copyright
    })
  },
  mounted () {
    let self = this
    window.addEventListener('scroll', function () {
      self.isShowBackTop = this.scrollY > 300
    })
  },
  methods: {
    backTop () {
      window.scrollTo(0, 0)
    }
  }
}
</script>
<style lang="scss" scoped>
.footer {
  margin-top: $container-margin;
  padding: 30px 0;
  background: #2d3237;
  transition: .5s;

  &.is-show-menu {
    transform: translateX(-240px);
  }

  &.is-error {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
  }
}

.link-wrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #3b424a;
  line-height: 2;

  &:after {
    content: "";
    flex: auto;
  }

  ::v-deep a {
    display: block;
    margin-right: $container-margin;
    font-size: $font-size-large;
    color: #9295a2;

    &:hover {
      color: $color-theme;
    }
  }
}

.copyright {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: $font-size-small;

  .footer-menu {
    display: flex;
    flex-wrap: wrap;

    .list {
      margin-right: 15px;
      line-height: 1.8;

      a {
        padding-right: 15px;
        border-right: 1px solid #666;
        font-size: $font-size-base;
      }

      &:last-child {
        a {
          border: 0;
        }
      }
    }
  }

  img {
    vertical-align: baseline;
  }

  .right {
    align-self: flex-end;
  }
}

.back-top {
  position: fixed;
  z-index: 99;
  right: 30px;
  bottom: 40px;
  transition: .5s;
  transform: translateX(100px);
  cursor: pointer;

  &.show {
    transform: translateX(0px);
  }

  .iconfont {
    font-size: 40px;
    color: $color-theme;
  }
}

@media screen and (max-width:1024px) {
  .copyright {
    flex-wrap: wrap;
  }

  .left {
    width: 100%;
  }

  .right {
    width: 100%;
    margin-top: $container-margin;
    text-align: right;
  }
}
</style>
