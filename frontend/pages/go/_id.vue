<template>
  <div style="text-align: center; margin-left: 20px; margin-right: 20px">
    <h1 style="color: red; font-size: 25px; margin: 30px 0 0 0"><a href="/">返回首页</a>，<a :href="url" style="color: -webkit-link; text-decoration: underline">立即访问</a>，页面将在60秒后自动跳转......</h1>
    <div style="color: red; font-size: 25px; margin: 60px 0 0 0"  v-for="(item , idx) in posts" :key="idx">
      <a :href="'/details/'+item.id" style="color: -webkit-link; text-decoration: underline" >{{item.title}}</a>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import site from "../../nuxt.config";
export default {
  name: "Go",
  layout: 'blank',
  data () {
    return {
      url: '/',
      pid: 1,
      posts: []
    }
  },
  // mounted () {
  //   console.log(1211111111111111111)
  //   window.location.href = '/'
  // }
  // fetch (ctx) {
  //   console.log(ctx.route.query.target);
  //   // ctx.route.redirect(ctx.route.query.target)
  //   // window.location.href = this.$route.query.target
  // },
  mounted () {
    this.setUserInfo();
    let _this = this;
    setTimeout(function () {
      _this.setUserInfo();
    }, 100)
  },
  methods: {
    setUserInfo: function () {
      let url = this.$route.query.target;
      let pid = this.$route.query.pid;
      this.pid = pid;
      this.url = url;
      // console.log(this.$store.state.recommend)
      setTimeout("javascript:location.href='" + url + "'", 30000 * 2)
      // setTimeout("javascript:location.href='" + url + "'", 20);
      // window.location.href = url
    }
  },
  // computed: {
  //   ...mapState({
  //     recommend: state => state.recommend
  //   }),
  //   getRecommend () {
  //     console.log( state.recommend)
  //   }
  // }
  async asyncData (ctx) {
    let url = ctx.route.query.pid;
    const {status, data} = await ctx.$axios.get(`${process.env.baseUrl}/recommend/`, {
      params: {
        params: {
          url: url
        }
      }
    });
    if (status === 200) {
      let posts = data.data[0].link_post;
      // console.log(posts)
      // this.posts = posts;
      // console.log(JSON.parse(posts))
      return {
        posts: JSON.parse(posts)
      }
    }
  }
}
</script>

<style scoped>
  /*.error-container {*/
  /*  display: flex;*/
  /*  flex-direction: column;*/
  /*  justify-content: center;*/
  /*  margin-top: 200px;*/
  /*  position: fixed;*/
  /*  top: 60px;*/
  /*  left: 0;*/
  /*  z-index: -1;*/
  /*  width: 100%;*/
  /*  height: 100%;*/
  /*  opacity: 0;*/
  /*  background: rgba(0, 0, 0, 0.5)*/

  /*.error-code {*/
  /*  font-size: 30px;*/
  /*}*/
  /*}*/
</style>
