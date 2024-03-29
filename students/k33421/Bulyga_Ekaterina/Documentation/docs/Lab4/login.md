<h1>Страница входа в систему</h1>
<p>Впервые открыв сайт, мы встречаем страницу входа. В ней реализовано получение токена и дальнейшее его сохранение в память браузера.</p>

<img src="../login.png">

<h2>Шаблон</h2>
<pre>
<code>
&lt;CardBox :class="cardClass" is-form @submit.prevent="onLogin"&gt;
&lt;FormField label="Логин" help="Введите логин"&gt;
  &lt;FormControl
    v-model="loginForm.username"
    :icon="mdiAccount"
    name="login"
    autocomplete="username"
    for="login"
  /&gt;
&lt;/FormField&gt;
&lt;FormField label="Пароль" help="Введите пароль"&gt;
  &lt;FormControl
    v-model="loginForm.password"
    :icon="mdiAsterisk"
    type="password"
    name="password"
    for="password"
    autocomplete="current-password"
  /&gt;
&lt;/FormField&gt;
&lt;template #footer&gt;
  &lt;BaseButtons&gt;
    &lt;BaseButton type="submit" color="info" label="Войти" @click="onLogin"/&gt;
  &lt;/BaseButtons&gt;
&lt;/template&gt;
&lt;/CardBox&gt;
</code>
</pre>

<h2>Обработка нажатия на клавишу "Войти"</h2>
<pre>
<code>
import axios from 'axios';
import {useMainStore} from "@/stores/main";

const mainStore = useMainStore()


export default {
  data() {
    return {
      loginForm: {
        username: '',
        password: '',
      },
      rules: {
        required: value => !!value || 'Required.'
      },
    };
  },
  methods: {
    async onLogin() {
        try {
          axios.post(`http://127.0.0.1:8000/auth/token/login/?username=${this.loginForm.username}&password=${this.loginForm.password}`, {'email': '', 'username': this.loginForm.username, 'password': this.loginForm.password})
          .then(response => {
            mainStore.setUser(response.data);
          })
          if (mainStore.userName !== '') {
            this.$router.push({name: 'tables'});
          }
        } catch (error) {
          console.error(error);
        }
      }
    }
};
</code>
</pre>

<h2>Код обработки информации о пользователе</h2>
<pre>
<code>
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import router from "@/router";

export const useMainStore = defineStore('main', () => {
  const token = ref('');
  const userName = ref('');

  if (localStorage.getItem('auth_token')) {
    setUser({'auth_token': localStorage.getItem('auth_token')})
  }

  const isFieldFocusRegistered = ref(false)

  function setUser(payload) {
    if (payload.auth_token) {
      token.value = payload.auth_token;
      localStorage.setItem('auth_token', payload.auth_token);
      axios.get('http://127.0.0.1:8000/auth/users/me', {headers: {'Authorization': `Token ${token.value}`}})
        .then(resp => userName.value = resp.data.username)
    }
  }

  function unsetUser() {
    localStorage.removeItem('auth_token');
    token.value = '';
    localStorage.setItem('logout', 'true');
  }

  return {
    isFieldFocusRegistered,
    setUser,
    token,
    userName,
    unsetUser,
  }
})
</code>
</pre>
