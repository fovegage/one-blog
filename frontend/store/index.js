import { UPDATE_GLOBAL_INFO, UPDATE_ERROR_MESSAGE, UPDATE_MENU_STATUS } from './mutations-types'
import site from '../nuxt.config'
export const state = () => ({
  info: {},
  menu: {},
  subMenu: {},
  links: [],
  tags: [],
  intro: [],
  base: [],
  recommend: [],
  errorInformation: {
    code: '',
    message: ''
  },
  menuStatus: false
})

export const mutations = {
  [UPDATE_GLOBAL_INFO] (state, { info, menu, subMenu, tags, intro, links, base, recommend }) {
    state.info = info
    state.menu = menu
    state.subMenu = subMenu
    state.tags = tags
    state.intro = intro
    state.links = links
    state.base = base
    state.recommend = recommend
  },

  [UPDATE_ERROR_MESSAGE] (state, data) {
    state.errorInformation = data
  },

  [UPDATE_MENU_STATUS] (state, flag) {
    state.menuStatus = flag
  }
}

export const actions = {
  // 获取公用信息
  async nuxtServerInit ({ commit }) {
    try {
      let globalInfo = await this.$axios.$get(`${process.env.baseUrl}/siteinfo/`, {
        params: {
          type: site.site.type
        },
        data: { progress: false }
      })
      let blogData = await this.$axios.$get(`${process.env.baseUrl}/blog/`, {
        params: {
          blog_type: site.site.type
        },
        data: { progress: false }
      })
      let menu = await this.$axios.$get(`${process.env.baseUrl}/categories/`, {
        params: {
          type: site.site.type,
          ordering: 'index'
        }
      });
      let intro = await this.$axios.$get(`${process.env.baseUrl}/introduce/`, {
        params: {
          type: site.site.type
        }
      });
      // globalInfo[0].carousel.map(item => {
      //   item.image = item.image.replace('http', 'https')
      // })
      // globalInfo.map(item => {
      //   item.logo = item.logo.replace('http', 'https')
      //   item.avatar = item.avatar.replace('http', 'https')
      //   item.wechat = item.wechat.replace('http', 'https')
      // })
      // 判断banner类型
      // if (globalInfo.banner.style === '1') {
      //   globalInfo.banner.big = globalInfo.banner.list[0]
      //   let [, banner1, banner2, banner3] = globalInfo.banner.list
      //   globalInfo.banner.small = [banner1, banner2, banner3]
      // }
      // console.log(globalInfo, "000000000000000000000")
      let result = {
        info: globalInfo[0],
        menu: menu,
        tags: blogData[0].blog_tag,
        intro: intro,
        subMenu: blogData[0].blog_introduce,
        links: blogData[0].blog_link,
        base: blogData[0].blog_info,
        recommend: blogData[0].recommend_introduce
      }
      commit(UPDATE_GLOBAL_INFO, result)
      return Promise.resolve(result)
    } catch (error) {
      return Promise.reject(error)
    }
  },

  // 上传图片
  async uploadImage ({ commit, rootState }, { requestData, config = {} }) {
    try {
      let { data } = await this.$axios.$post(`${process.env.baseUrl}/wp-content/themes/${rootState.info.themeDir}/xm_upload.php`, requestData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          progress: false
        },
        ...config
      })
      return Promise.resolve(data)
    } catch (error) {
      return Promise.reject(error)
    }
  },

  // 删除图片
  async deleteImage ({ commit, rootState }, requestData) {
    try {
      let { data } = await this.$axios.$post(`${process.env.baseUrl}/wp-content/themes/${rootState.info.themeDir}/xm_upload.php`, requestData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          progress: false
        }
      })
      return Promise.resolve(data)
    } catch (error) {
      return Promise.reject(error)
    }
  }
}
