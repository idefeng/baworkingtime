import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import DashBoard from '@/components/Dashboard'
import About from '@/components/About'
import NotFound from '@/components/NotFound'
import Users from '@/components/Users'
import Projects from '@/components/Projects'
import UsersCheck from '@/components/UsersCheck'
import WorkDiary from '@/components/WorkDiary'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Dashboard',
      name: 'DashBoard',
      component: DashBoard
    },
    {
      path: '/Users',
      name: 'Users',
      component: Users
    },
    {
      path: '/Projects',
      name: 'Projects',
      component: Projects
    },
    {
      path: '/UsersCheck',
      name: 'UsersCheck',
      component: UsersCheck
    },
    {
      path: '/WorkDiary',
      name: 'WorkDiary',
      component: WorkDiary
    },
    {
      path: '/About',
      name: 'About',
      component: About
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})
