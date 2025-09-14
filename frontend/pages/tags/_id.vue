<template>
  <div class="container">
    <ul class="header">
      <li class="list">当前标签：{{ $route.query.title }}</li>
    </ul>
    <div v-if="articleList.length === 0" class="not">暂无数据！</div>
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
<!--            <span><x-icon type="icon-message"></x-icon>{{ item.articleInfor.commentCount }}</span>-->
<!--            <span><x-icon type="icon-good"></x-icon>{{ item.articleInfor.xmLike.very_good }}</span>-->
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
</template>

<script>
import { mapState } from 'vuex'
import site from '../../nuxt.config'
export default {
  name: 'Tags',
  watchQuery: ['type'],
  fetch ({ params, query, store }) {
    store.commit('article/SET_CURRENT_PAGE', +params.id)
    return store.dispatch('article/getArticleList', {
      type: site.site.type,
      ordering: '-views',
      tag__tname: query.title,
      page: params.id,
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
      title: this.$route.query.title,
      meta: [
        { name: 'keywords', content: this.info.keywords },
        { name: 'description', content: this.info.description }
      ]
    }
  },
  methods: {
    _changePagination (id) {
      this.$store.commit('article/SET_CURRENT_PAGE', id)
      this.$router.push({
        name: 'tags-id',
        params: { id },
        query: {
          type: this.$route.query.type,
          title: this.$route.query.title
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
// 文章列表
.container {
  padding: $container-padding;
  background: $color-white;
  border-radius: $border-radius;

  .header {
    padding-bottom: $container-padding;
    border-bottom: 1px solid $color-main-background;
    font-size: $font-size-large;
  }

  .not {
    margin: 15px 0;
    text-align: center;
    color: $color-theme;
  }
}

@media screen and (max-width:767px) {
  // 文章列表
  .container {
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
