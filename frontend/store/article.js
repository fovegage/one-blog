import site from '../nuxt.config'
import {
  UPDATE_ARTICLE_LIST,
  SET_ARTICLE_DETAIL,
  SET_TOTAL_PAGE,
  SET_CURRENT_PAGE,
  UPDATE_VIEW_COUNT,
  UPDATE_OPINION,
  UPDATE_OPINION_LOADING
} from './mutations-types'

export const state = () => ({
  articleList: [],
  detail: {},
  totalPage: 0,
  currentPage: 1,
  viewCount: 0,
  opinion: {
    very_good: {
      src: require('~/assets/images/like_love.png'),
      isShowLaoding: false,
      text: 'Love'
    },
    good: {
      src: require('~/assets/images/like_haha.png'),
      isShowLaoding: false,
      text: 'Haha'
    },
    commonly: {
      src: require('~/assets/images/like_wow.png'),
      isShowLaoding: false,
      text: 'Wow'
    },
    bad: {
      src: require('~/assets/images/like_sad.png'),
      isShowLaoding: false,
      text: 'Sad'
    },
    very_bad: {
      src: require('~/assets/images/like_angry.png'),
      isShowLaoding: false,
      text: 'Angry'
    }
  }
})

export const mutations = {
  [UPDATE_ARTICLE_LIST] (state, data) {
    state.articleList = data
  },

  [SET_ARTICLE_DETAIL] (state, data) {
    state.detail = data
  },

  [SET_TOTAL_PAGE] (state, n) {
    state.totalPage = n
  },

  [SET_CURRENT_PAGE] (state, n) {
    state.currentPage = n
  },

  [UPDATE_VIEW_COUNT] (state, n) {
    state.viewCount = n
  },

  [UPDATE_OPINION] (state, data) {
    Object.keys(state.opinion).map(key => {
      state.opinion[key].data = data[key]
    })
  },

  [UPDATE_OPINION_LOADING] (state, { key, flag }) {
    state.opinion[key].isShowLaoding = flag
  }
}

export const actions = {
  // 获取文章列表
  async getArticleList ({ rootState, commit }, requestData) {
    try {
      // ${process.env.baseUrl}
      let data = await this.$axios.$get(`${process.env.baseUrl}/posts`, {
        params: requestData,
        data: { progress: false }
      });
      // data.results.map(item => {
      //   item.image = item.image.replace('http', 'https')
      // })
      // console.log(data.results)
      // data.results.map(item => {
      // // .replace(/https?:\/\/(\w+\.)+\w+(:\d+)?/, '')
      // //   replace('T', ' ')
      // //     ? item.image : rootState.info.thumbnail
      //   item.thumbnail = item.image
      //   item.date = item.create_at
      // })
      // console.log(data)
      commit(UPDATE_ARTICLE_LIST, data.results)
      commit(SET_TOTAL_PAGE, data.count)
      return Promise.resolve(data)
    } catch (error) {
      return Promise.reject(error)
    }
  },

  // 获取文章详情
  async getArticleDetail ({ commit, rootState }, id) {
    try {
      // const domainRegexp = /(https?:\/\/([a-z\d-]\.?)+(:\d+)?)?(\/.*)/gi
      let { data } = await this.$axios.$get(`${process.env.baseUrl}/posts/${id}`, {
        params: {
          type: site.site.type,
          ordering: '-create_at'
        },
        data: { progress: false }
      })
      // data.date = data.date.replace('T', ' ')
      // data.articleInfor.other.authorPic = data.articleInfor.other.authorPic.replace(domainRegexp, '$4')
      // data.articleInfor.thumbnail = data.articleInfor.thumbnail
      //   ? data.articleInfor.thumbnail.replace(domainRegexp, '$4')
      //   : rootState.info.thumbnail
      commit(SET_ARTICLE_DETAIL, data)
      // commit(UPDATE_OPINION, data.articleInfor.xmLike)
      return Promise.resolve(data)
    } catch (error) {
      return Promise.reject(error)
    }
  },
  // 发表意见
  async updateOpinion ({ commit }, requestData) {
    try {
      let { data } = await this.$axios.$post(`${process.env.baseUrl}/wp-json/xm-blog/v1/like`, requestData, {
        headers: {
          progress: false
        }
      })
      commit(UPDATE_OPINION, data)
      return Promise.resolve(data)
    } catch (error) {
      return Promise.reject(error)
    }
  }
}
