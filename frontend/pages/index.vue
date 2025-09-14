<template>
  <div class="container">
    <!-- banner start -->
    <div
      ref="bannerWrapper"
      :class="[
        'banner-wrap',
        'style-1',
      ]"
    >
      <template>
        <div class="big-banner">
          <el-carousel trigger="click" :height="bannerHeight" :interval="3000" arrow="never">
            <el-carousel-item v-for="(item, i) in info.carousel" :key="i">
              <a target="_blank" :href="item.url" class="list block">
                <img :src="item.image" :alt="item.title">
              </a>
            </el-carousel-item>
          </el-carousel>
        </div>
        <ul class="small-banner">
          <li class="list" v-for="item in info.carousel" :key="item.key">
            <a target="_blank" class="block" :href="item.url">
              <img :src="item.image" :alt="item.title">
            </a>
          </li>
        </ul>
      </template>
    </div>
    <!-- article list start -->
    <div class="article-list-wrap" >
      <ul class="header">
        <li class="list">最新文章</li>
      </ul>
      <article class="article-list" v-for="item in articleList" :key="item.key">
        <nuxt-link :to="{ name: 'details-id', params: { id: item.id } }" class="thumbnail-wrap">
          <img :src="item.image" class="thumbnail" :alt="item.title">
        </nuxt-link>
        <div class="list-content">
          <h2 class="title">
            <span class="classify" v-html="item.category.cname"></span>
            <nuxt-link :to="{ name: 'details-id', params: { id: item.id } }" class="vertical-middle" v-html="item.title"></nuxt-link>
          </h2>
          <p class="summary">{{ item.desc }}</p>
          <div class="opeartion">
            <div class="information">
              <span><x-icon type="icon-date"></x-icon>{{ item.create_at }}</span>
              <x-icon type="icon-tag1"></x-icon>
              <span v-for="(item, index) in item.tag" :key="index" >{{ item.tname }}</span>
              <span><x-icon type="icon-hot1"></x-icon>{{ item.views }}</span>

              <!--              <span><x-icon type="icon-message"></x-icon>{{ item.articleInfor.commentCount }}</span>-->
<!--              <span><x-icon type="icon-good"></x-icon>{{ item.articleInfor.xmLike.very_good }}</span>-->
            </div>
            <nuxt-link class="details-btn" :to="{ name: 'details-id', params: { id: item.id } }">阅读详情</nuxt-link>
          </div>
        </div>
      </article>
      <!-- more btn start -->
      <el-pagination
        small
        :page-size="8"
        layout="prev, pager, next, jumper"
        :current-page="currentPage"
        @current-change="_changePagination"
        :total="totalPage">
      </el-pagination>
      <!-- more btn end -->
    </div>
    <!-- article list end -->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import site from '../nuxt.config'
export default {
  name: 'Index',
  fetch ({ store }) {
    store.commit('article/SET_CURRENT_PAGE', 1)
    return store.dispatch('article/getArticleList', {
      type: site.site.type,
      ordering: '-create_at',
      page: 1,
      per_page: 8,
      _embed: true
    })
  },
  computed: {
    ...mapState(['info']),
    ...mapState('article', ['articleList', 'totalPage', 'currentPage'])
  },
  head () {
    return {
      title: `${this.info.blogName} | ${this.info.blogDescription}`,
      meta: [
        { name: 'keywords', content: this.info.keywords },
        { name: 'description', content: this.info.description }
      ]
    }
  },
  data () {
    return {
      bannerHeight: '390px'
    }
  },
  mounted () {
    this._bannerClacHeight()
    window.addEventListener('resize', this._bannerClacHeight)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this._bannerClacHeight)
  },
  methods: {
    _bannerClacHeight () {
      this.bannerHeight = `${this.$refs.bannerWrapper.offsetWidth / (900 / 405)}px`
    },
    _changePagination (id) {
      this.$router.push({
        name: 'article-id-title',
        params: { id }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
// banner
.banner-wrap {
  position: relative;

  &.style-1 {
    display: flex;
    justify-content: space-between;
    height: 320px;
  }

  &.style-2 {
    overflow: hidden;
    background-color: #fff;
    border-radius: $border-radius;

    .banner-title {
      position: absolute;
      bottom: 0;
      left: 0;
      min-width: 200px;
      max-width: 100%;
      padding: 5px 15px;
      box-sizing: border-box;
      background: rgba(0,0,0,.3);
      opacity: .9;
      @extend %ellipsis;
      color: #fff;
    }

    ::v-deep .el-carousel__arrow {
      background-color: transparent;
      font-size: 30px;
    }

    ::v-deep .el-carousel__indicators--horizontal {
      bottom: 20px;
    }
  }

  .title {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 30px;
    padding: 0 10px;
    box-sizing: border-box;
    background: rgba(0,0,0,.3);
    line-height: 30px;
    color: $color-white;
    @extend %ellipsis;
  }

  img {
    vertical-align: top;
    width: 100%;
    height: 100%;
  }

  .list {
    overflow: hidden;
    position: relative;
    border-radius: $border-radius;
  }

  .big-banner {
    width: 710px;

    img {
      height: 320px;
    }
  }

  .small-banner {
    width: 180px;

    .list {
      height: 100px;
      margin-bottom: 10px;

      &:last-of-type {
        margin-bottom: 0;
      }
    }
  }
}

@media screen and (max-width: 1024px) {
  .banner-wrap {
    &.style-1 {
      flex-wrap: wrap;
      height: auto;

      /*::v-deep .el-carousel__arrow {*/
      /*  display: block !important;*/
      /*}*/

      .big-banner {
        width: 100%;

        img {
          height: auto;
        }
      }

      .small-banner {
        display: flex;
        justify-content: space-between;
        width: 100%;
        margin-top: $container-margin;

        .list {
          width: 32%;
          height: auto;
          margin-bottom: 0;
        }

        img {
          height: auto;
        }
      }
    }

    &.style-2 {
      ::v-deep .el-carousel__arrow {
        display: block !important;
      }
    }
  }
}

@media screen and (max-width:767px) {
  .banner-wrap .list .title {
    height: 20px;
    font-size: 10px;
    line-height: 20px;
    text-indent: 8px;
  }
  // 文章列表
  .article-list-wrap {
    .article-list {
      flex-wrap: wrap;
      height: auto;

      .title {
        margin-top: 15px;
        font-size: $font-size-large;
      }

      .summary {
        height: auto;
      }

      .list-content {
        height: auto;
      }

      .opeartion {
        position: static;
        display: block;
        margin-top: 10px;
      }

      .details-btn {
        display: block;
        margin-top: 10px;
        padding: 10px 0;
        text-align: center;
      }
    }

    .thumbnail-wrap {
      width: 100%;
      margin-right: 0;
      text-align: center;

      .thumbnail {
        width: auto;
        height: auto;
        max-height: 150px;
      }
    }
  }

  // 翻页
  ::v-deep .el-pagination {
    .el-pagination__jump {
      display: none;
    }
  }
}
</style>
