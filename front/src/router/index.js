import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'
import Error404 from '../views/404.vue'

import store from '../store'
import MainAdmin from '../components/admin/Main.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/admin',
        component: MainAdmin,
        meta: {
            requiresAuth: true,
        },
        children: [
            {
                path: '/imgsize',
                name: 'ImgSize',
                component: () => import('../views/admin/ImgSize.vue')
            },

            {
                path: '*',
                name: '404_admin',
                component: Error404
            },

        ]
    },

    {
        path: '/',

        component: Login,
        children: [
            {
                path: '/',
                 name: 'Login',
                component: Login,
            }, {
                path: '/login',
                component: Login,
            }

        ]
    },

    {
        path: '/logout',
        name: 'Logout',
        component: Logout

    },
    {
        path: '*',
        name: '404',
        component: Error404
    },
];

const router = new VueRouter({
    mode: 'history',
    routes
});


router.beforeEach((to, from, next) => {
    // проверяем есть ли токен
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!store.getters.isAuthenticated) {
            next({
                name: 'Login',
            })
        } else {
            next()
        }


    } else {
        next()
    }
});


export default router
