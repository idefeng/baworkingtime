import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import About from '@/components/About'
import NotFound from '@/components/NotFound'
import Users from '@/components/Users'
import Projects from '@/components/Projects'
import UsersCheck from '@/components/UsersCheck'

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
