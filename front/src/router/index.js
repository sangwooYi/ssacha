import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Intro from '@/views/intro/Intro'
import Introduce from '@/views/intro/Introduce'
import Mbti from '@/views/intro/mbti'
import Recommend from '@/views/recommendation/Recommend'
import RecommendDetail from '@/views/recommendation/RecommendDetail'
import RecommendSearch from '@/views/recommendation/RecommendSearch' 
import Community from '@/views/community/Community'
import CreateCommunity from '@/views/community/CreateCommunity'
import CommunityDetail from '@/views/community/CommunityDetail'
import CommunityDetailUpdate from '@/views/community/CommunityDetailUpdate'

Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/Signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/Profile',
    name: 'Profile',
    component: Profile,
  },  
  {
    path: '/',
    name: 'Intro',
    component: Intro,
    
  },
  {
    path: '/intro/Introduce',
    name: 'Introduce',
    component: Introduce,
  },  
  {
    path: '/intro/mbti',
    name: 'Mbti',
    component: Mbti,
  }, 
  {
    path: '/accounts/Login',
    name: 'Login',
    component: Login,
  },  
  {
    path: '/recommendation/Recommend',
    name: 'Recommend',
    component: Recommend,
  },
  {
    path: '/recommendation/RecommendDetail/:movie_pk',
    name: 'RecommendDetail',
    component: RecommendDetail,
  },    
  {
    path: '/recommendation/RecommendSearch/:keyword',
    name: 'RecommendSearch',
    component: RecommendSearch,
  },        
  {
    path: '/community/Community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/CreateCommunity',
    name: 'CreateCommunity',
    component: CreateCommunity,
  },
  {
    path: '/community/CommunityDetail/:community_pk',
    name: 'CommunityDetail',
    component: CommunityDetail,
  },
  {
    path: '/community/CommunityDetailUpdate/:community_pk',
    name: 'CommunityDetailUpdate',
    component: CommunityDetailUpdate,
  },  
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router