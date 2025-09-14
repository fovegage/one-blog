<template>
  <section class="container">
    <!-- 文章内容开始 -->
    <article class="section article">
      <h2 class="title" v-html="detail.title"></h2>
      <div class="other-info">
        <p>
          <span class="author">
            <x-icon type="icon-author"></x-icon> {{ detail.nickname }}
          </span>
          <time class="time m-l-5px">
            <x-icon type="icon-date"></x-icon> {{ detail.create_at }}
          </time>
        </p>
        <p>
          <span class="text m-l-10px">
            <x-icon type="icon-note1"></x-icon> {{detail.category.cname}}
          </span>
          <x-icon type="icon-tag1"></x-icon>
          <span v-for="(item, index) in detail.tag" :key="index" >
             {{ item.tname }}
          </span>

          <span class="m-l-5px">
            <x-icon type="icon-hot1"></x-icon> {{ detail.views }}
          </span>
<!--          <span class="m-l-5px">-->
<!--            <x-icon type="icon-message-f"></x-icon>{{ detail.articleInfor.commentCount }}-->
<!--          </span>-->
        </p>
      </div>
      <div ><img style="border-radius: 15px" src="https://pic.downk.cc/item/5e63b43d98271cb2b8f86955.jpg" alt=""></div>
      <div class="m-content" id="articleContent" ref="articleContent" v-html="getContent"></div>
    </article>
    <div class="section copyright">
      <p><strong>版权声明: </strong> 本站文章除特别声明外，均为本站原创。转载请注明出处，谢谢。</p>
      <p class="m-t-10px"><strong>本文地址: </strong><a :href="fullPath+'/details/'+detail.id">{{fullPath}}/details/{{ detail.id }}</a></p>
    </div>
    <!-- 文章内容结束 -->

<!--    <div class="section operation">-->
      <!-- 点赞开始 -->
<!--      <ul class="opinion">-->
<!--        <li class="list" v-for="(item, key) in opinion" :key="key" @click="_updateOpinion(key)">-->
<!--          <span class="block total">-->
<!--            <x-icon type="icon-loading" v-show="item.isShowLaoding"></x-icon> {{ item.data }}人-->
<!--          </span>-->
<!--          <img :src="item.src" width="40" height="40" alt="">-->
<!--          <span class="block">{{ item.text }}</span>-->
<!--        </li>-->
<!--      </ul>-->
      <!-- 点赞结束 -->

      <!-- 分享开始 -->
<!--      <div class="share text-center">-->
<!--        <span class="text">分享到：</span>-->
<!--        <a :href="`https://connect.qq.com/widget/shareqq/index.html?url=${domain}/details/${$route.params.id}&title=${detail.title}&summary=${detail.desc}`" target="_blank">-->
<!--          <svg-icon iconName="#icon-QQ"></svg-icon>-->
<!--        </a>-->
<!--        <a :href="`https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=${domain}/details/${$route.params.id}&title=${detail.title}&summary=${detail.desc}`" target="_blank">-->
<!--          <svg-icon iconName="#icon-Qzone"></svg-icon>-->
<!--        </a>-->
<!--        <a :href="`https://service.weibo.com/share/share.php?url=${domain}/details/${$route.params.id}%230-tsina-1-21107-397232819ff9a47a7b7e80a40613cfe1&title=${detail.title}&appkey=1343713053&searchPic=true#_loginLayer_1473259217614`" target="_blank">-->
<!--          <svg-icon iconName="#icon-xinlang"></svg-icon>-->
<!--        </a>-->
<!--        <a href="javascript:;" class="create-poster-btn" @click="isShowPoster = true">-->
<!--          <svg-icon iconName="#icon-shengchengerweima"></svg-icon>-->
<!--        </a>-->
<!--      </div>-->
      <!-- 分享结束 -->

      <!-- 标签开始 -->

      <!-- 标签结束 -->

      <!-- 切换上下一篇文章 -->
<!--      <div class="relative-link-wrap">-->
<!--        <div class="prev">-->
<!--          <p v-if="detail.pre_link === ''">已是第一篇文章！</p>-->
<!--          <p v-else>上一篇：<nuxt-link :to="{ name: 'details-id', params: { id: detail.pre_link } }">{{ detail.title }}</nuxt-link></p>-->
<!--        </div>-->
<!--        <div class="next">-->
<!--          <p v-if="detail.next_link === ''">已是最后一篇文章！</p>-->
<!--          <p v-else>下一篇：<nuxt-link :to="{ name: 'details-id', params: { id: detail.next_link } }">{{ detail.title }}</nuxt-link></p>-->
<!--        </div>-->
<!--      </div>-->
      <!-- 切换结束 -->
<!--    </div>-->
    <!-- 作者信息 -->
<!--    <div class="section author-introduct">-->
<!--      &lt;!&ndash; 头像 &ndash;&gt;-->
<!--      <img :src="detail.articleInfor.other.authorPic" class="phone-hide" width="100">-->
<!--      <div class="right">-->
<!--        &lt;!&ndash; 昵称 &ndash;&gt;-->
<!--        <div class="header">-->
<!--          <img :src="detail.articleInfor.other.authorPic" class="phone-show" width="25">-->
<!--          <p class="inline-block name">-->
<!--            作者简介：<x-icon type="icon-about-f"></x-icon><span class="f-s-14px">{{ detail.articleInfor.author }}</span>-->
<!--          </p>-->
<!--          <div v-if="info.isOpenReward" class="reward" @click="isShowReward = true">-->
<!--            <svg-icon iconName="#icon-dashang"></svg-icon>打赏-->
<!--          </div>-->
<!--          &lt;!&ndash; 打赏详情 &ndash;&gt;-->
<!--          <reward v-model="isShowReward" :content="rewardContent"></reward>-->
<!--        </div>-->
<!--        &lt;!&ndash; 简介 &ndash;&gt;-->
<!--        <p class="author-summary">{{ detail.articleInfor.other.authorTro }}</p>-->
<!--        &lt;!&ndash; 社交信息 &ndash;&gt;-->
<!--        <ul class="author-link">-->
<!--          <li class="list">-->
<!--            <nuxt-link :to="{ name: 'index' }">-->
<!--              <svg-icon iconName="#icon-icon-test"></svg-icon>-->
<!--            </nuxt-link>-->
<!--          </li>-->
<!--          <template v-for="(item, key) in authorOtherInfo">-->
<!--            <li v-if="key === 'wechatNum'" class="list" :key="item.key" @click="_showWechatNum(item.url)">-->
<!--              <a href="javascript:;">-->
<!--                <svg-icon :iconName="item.icon"></svg-icon>-->
<!--              </a>-->
<!--            </li>-->
<!--            <li v-else :key="item.key" class="list">-->
<!--              <a :href="key == 'email' ? `mailto:${item.url}` : item.url" target="_blank">-->
<!--                <svg-icon :iconName="item.icon"></svg-icon>-->
<!--              </a>-->
<!--            </li>-->
<!--          </template>-->
<!--        </ul>-->
<!--      </div>-->
<!--    </div>-->
    <!-- 评论列表 -->
<!--    <div class="section comment">-->
<!--      <h2 class="comment-title" v-html="`共 ${detail.articleInfor.commentCount} 条评论关于 “${detail.title.rendered}”`"></h2>-->
<!--      <client-only>-->
<!--        <comments :comment-status="detail.comment_status"/>-->
<!--      </client-only>-->
<!--    </div>-->
    <!-- 生成海报 -->
<!--    <client-only placeholder="Loading...">-->
<!--      <create-poster v-model="isShowPoster" :content="posterContent"/>-->
<!--    </client-only>-->
  </section>
</template>
<script>
import { mapState, mapActions } from 'vuex'
import marked from 'marked'
import nuxt from '../../nuxt.config.js'
// import Comments from '~/components/Comment'
// import Reward from '~/components/Reward'
// import CreatePoster from '~/components/CreatePoster'
export default {
  name: 'Details',
  fetch ({ params, error, store }) {
    // store.dispatch('article/updateArticleViewCount', { id: params.id })
    return store.dispatch('article/getArticleDetail', params.id)
  },
  components: {
    // Comments,
    // Reward,
    // CreatePoster
  },
  data () {
    return {
      isShowReward: false,
      isShowPoster: false,
      fullPath: nuxt.site.domain,
      domain: nuxt.site.domain,
      rewardContent: {},
      posterContent: {},
      changValue: null,
      authorOtherInfo: {
        github: {
          icon: '#icon-GitHub'
        },
        qq: {
          icon: '#icon-qq1'
        },
        wechatNum: {
          icon: '#icon-weixin5'
        },
        sina: {
          icon: '#icon-xinlang1'
        },
        email: {
          icon: '#icon-youxiang'
        }
      }
    }
  },
  computed: {
    ...mapState(['info']),
    ...mapState('article', ['detail', 'viewCount', 'opinion']),
    getContent: function () {
      let self = this;
      self.readmeContent = marked(this.detail.content || '', {
        sanitize: true
      });
      return this.readmeContent
    }
  },
  // mounted: function () {
  //   // console.log(this.$refs);
  //   // for (let key in this.$refs) {
  //   //   console.log(this.$refs[key])
  //   // }
  //   setTimeout(() => {
  //     this.changValue = 1;
  //     this.$nextTick(() => {
  //       this.calculateHeight();
  //     });
  //   },0);
  //   // this.$refs.articleList.a = '1'
  //   // console.log()
  //   // console.log(this.$refs.articleList.getElementById('#content-m a'))
  //   // document.getElementById('#content-m a').attr('href','http://tianlongbabu.com');
  //   // $('#qiaofeng').attr('href','http://tianlongbabu.com');
  //   // this.$refs.articleList.style.attr('href', 'http://tianlongbabu.com');
  //   // console.log()
  // },
  head () {
    let keywords = []
    this.detail.tag && this.detail.tag.forEach(item => keywords.push(item.tname))
    return {
      title: `${this.detail.title} | ${this.info.blogName}`,
      meta: [
        { hid: 'keywords', name: 'keywords', content: keywords.join(',') },
        { hid: 'description', name: 'description', content: this.detail.desc }
      ],
      style: [
        { cssText: this.info.detailsCss, type: 'text/css' }
      ]
    }
  },
  // created () {
  //   this.fullPath = `${this.info.domain.replace(/\/$/, '')}${this.$route.path}`
  //   let other = this.detail.articleInfor.other
  //
  //   // 合并作者数据
  //   for (let key in this.authorOtherInfo) {
  //     this.authorOtherInfo[key].url = other[key]
  //   }
  //
  //   // 打赏数据
  //   this.rewardContent = {
  //     thumbnail: this.detail.articleInfor.other.authorPic,
  //     text: this.info.rewardText,
  //     alipay: this.info.alipay,
  //     wechatpay: this.info.wechatpay
  //   }
  // },
  // methods: {
  //   calculateHeight: function () {
  //     console.log(1111111111111)
  //   }
  // },
  mounted () {
    // console.log(this.$refs.articleContent.getElementsByTagName('a'))
    var i;
    let aArray = this.$refs.articleContent.getElementsByTagName('a');
    for (i = 0; i < aArray.length; i++) {
      aArray[i].target = '_blank';
      if (aArray[i].href.startsWith(nuxt.site.domain) || aArray[i].href.startsWith('https://pan')) {
        continue
      } else {
        aArray[i].href = '/go/' + '?target=' + aArray[i].href + '&pid=' + this.detail.id;
      }
    }
    // for (let key in aArray) {
    //   // aArray[key] = '/go/'
    //   console.log(aArray[key])
    // }
    // aArray.filter(item => {
    //   item.href: '/go/'+ item.href
    // })
    // console.log(aArray[0])
    // console.log(typeof aArray)
    // aArray.forEach(v => {
    //   console.log(v);
    // });
    // console.log(this.$refs.articleContent.getElementsByTagName('a'))
    // for per in this.$refs.articleContent.getElementsByTagName('a')
    // console.log()
    //
    // setTimeout(() => {
    //   this.changValue = 1;
    //   this.$nextTick(() => {
    //     this.calculateHeight();
    //   });
    // }, 0);
    // 海报内容
    this.posterContent = {
      imgUrl: this.detail.image,
      title: this.detail.title,
      summary: this.detail.desc,
      time: this.detail.create_at,
      // qrcodeLogo: this.detail.articleInfor.other.authorPic.replace(/(https?:\/\/([a-z\d-]\.?)+(:\d+)?)?(\/.*)/gi, `${this.info.domain}$4`),
      qrcodeText: this.info.blogName,
      id: this.$route.params.id
    }

    // eslint-disable-next-line
    process.browser && document.querySelectorAll('pre code').forEach(block => Prism.highlightElement(block))
  },
  beforeDestroy () {
    document.querySelectorAll('.prism-previewer').forEach(item => (item.style.display = 'none'))
  },
  methods: {
    ...mapActions('article', ['updateOpinion']),

    // 发表意见
    async _updateOpinion (key) {
      if (localStorage.getItem(`xm_link_${this.$route.params.id}`)) {
        this.$message({
          title: '您已经发表过意见了！',
          type: 'warning'
        })
      } else {
        this.$store.commit('article/UPDATE_OPINION_LOADING', {
          key,
          flag: true
        })
        await this.updateOpinion({
          id: this.$route.params.id,
          key
        })
        this.$store.commit('article/UPDATE_OPINION_LOADING', {
          key,
          flag: false
        })
        localStorage.setItem(`xm_link_${this.$route.params.id}`, true)
      }
    },

    // 显示微信号码
    _showWechatNum (num) {
      this.$message({
        title: `微信号：${num}`,
        showClose: true,
        showImg: true,
        center: true,
        wrapCenter: true,
        width: 280,
        imgUrl: this.detail.articleInfor.other.wechatPic,
        duration: 0
      })
    }
  }
}
</script>
<style lang="scss" >
  @import "@/assets/scss/markdown.scss";
.section {
  margin-top: $container-margin;
  padding: $container-padding;
  background: $color-white;
  border-radius: $border-radius;
}

.article {
  margin-top: 0;

  .title {
    padding: 10px 0;
    font-size: 20px;
    text-align: center;
  }

  .other-info {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;
    padding-bottom: 5px;
    border-bottom: 1px solid $color-border;
    text-align: center;
    color: $color-sub-text;

    .iconfont {
      vertical-align: baseline;
    }
  }

  // 正文
  .content-details {
    line-height: 2;
    word-break: break-all;

    ::v-deep a {
      color: $color-theme;
    }

    ::v-deep h2{
      margin-top: 10px;

      .iconfont {
        vertical-align: bottom;
      }
    }

    ::v-deep h1,
    ::v-deep h2{
      font-size: $font-size-large;
    }

    ::v-deep h4,
    ::v-deep h5,
    ::v-deep h6{
      font-size: $font-size-small;
    }

    ::v-deep img {
      height: auto !important;
      box-shadow: 0 0 10px #d2d2d2;
    }
  }
}

.opinion {
  display: flex;
  justify-content: center;
  margin-bottom: $container-margin;
  text-align: center;

  .list {
    width: 50px;
    margin: 0 20px;
    cursor: pointer;
  }

  .total {
    font-size: $font-size-small;
  }

  .icon-loading {
    vertical-align: baseline;
  }
}

// 分享按钮
.share {
  margin-bottom: $container-margin;

  .iconfont-colour {
    width: 25px;
    height: 25px;
    vertical-align: bottom;
    margin: 0 5px;
  }
}

// 文章标签
.tag-wrap {
  margin-bottom: $container-margin;

  .iconfont {
    margin-right: 3px;
    font-size: 20px;
  }
}

// 上一篇、下一篇
.relative-link-wrap {
  .next {
    float: right;
    margin-top: -22px;
  }
}

// 作者信息
.author-introduct {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;

  .right {
    flex: 1;
  }

  .header {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    margin-bottom: 5px;
    padding-bottom: 5px;
    border-bottom: 1px solid $color-border;
  }

  .reward {
    margin-left: 10px;
    cursor: pointer;

    .iconfont-colour {
      vertical-align: bottom;
    }
  }

  .name {
    font-size: $font-size-large;
  }

  img {
    margin-right: 10px;
    border-radius: $border-radius;
  }
}

.author-link {
  display: flex;
  flex-wrap: wrap;
  margin-top: 10px;

  .list {
    box-sizing: border-box;
    margin-right: 10px;
    margin-bottom: 5px;
    padding: 5px;
    border-radius: $border-radius;
    background: $color-sub-background;
    font-size: $font-size-small;
  }

  .iconfont-colour {
    width: 20px;
    height: 20px;
    vertical-align: middle;
  }
}

.comment-title {
  margin-bottom: 10px;
  padding: 10px 0;
  border-radius: $border-radius;
  background: $color-sub-background;
  font-size: $font-size-large;
  text-align: center;
}

// 代码高亮
::v-deep div.code-toolbar {
  overflow: hidden;
  width: 100%;
  margin: 20px 0;
  padding-top: 30px;
  border-radius: $border-radius;

  pre {
    margin: 0;
    border: {
      width: 0 1px 1px;
      style: solid;
      color: $color-main-background;
    }
  }

  code {
    border: 0;
    box-shadow: none;
    background-size: 4em 4em;
    line-height: 2;
  }

  .line-numbers .line-numbers-rows {
    border-color: $color-main-background;
  }

  .toolbar {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 30px;
    background: #358ccb;
    opacity: 1;

    span {
      background: none;
      box-shadow: none;
      border-radius: 0;
      color: #fff;
    }
  }

  .toolbar-item {
    padding-left: 20px;

    span:hover {
      color: $color-white;
    }

    &:before {
      content: "\e7ae";
      font-family: "iconfont";
      color: $color-white;
    }
  }
}

@media screen and (max-width:767px) {
  .opinion {
    justify-content: space-between;

    .list {
      margin: 0;
    }
  }

  .create-poster-btn {
    display: none;
  }
  .relative-link-wrap {
    .prev{
      display: none;
    }
    .next {
      /*margin-top: 1px;*/
    }
  }
}
</style>
