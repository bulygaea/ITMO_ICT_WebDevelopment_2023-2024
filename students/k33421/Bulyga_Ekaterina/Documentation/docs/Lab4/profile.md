<h1>Страница профиля</h1>
<p>На странице профиля можно изменить свой логин.</p>

<img src="../profile.png">

<h2>Шаблон</h2>
<pre>
<code>
&lt;LayoutAuthenticated&gt;
&lt;SectionMain&gt;
  &lt;SectionTitleLineWithButton :icon="mdiAccount" title="Мой профиль" main/&gt;

  &lt;UserCard class="mb-6" /&gt;

  &lt;div class="center grid-cols-1:grid-cols-2 gap-6"&gt;
    &lt;CardBox is-form @submit.prevent="updateProfile"&gt;
      &lt;FormField label="Новый логин" help="Обязательное поле"&gt;
        &lt;FormControl
          :icon="mdiAsterisk"
          v-model="form.username"
          name="username"
          type="username"
          autocomplete="username"
        /&gt;
      &lt;/FormField&gt;

      &lt;template #footer&gt;
        &lt;BaseButtons&gt;
          &lt;BaseButton color="info" type="submit" label="Сохранить" /&gt;
        &lt;/BaseButtons&gt;
      &lt;/template&gt;
    &lt;/CardBox&gt;
  &lt;/div&gt;
&lt;/SectionMain&gt;
&lt;/LayoutAuthenticated&gt;
</code>
</pre>

<h2>Шаблон карточки пользователя</h2>
<pre>
<code>
&lt;CardBox&gt;
&lt;BaseLevel type="justify-around lg:justify-center"&gt;
  &lt;UserAvatarCurrentUser class="sm:mx-0.1" /&gt;
  &lt;div class="space-y-3 text-center md:text-left lg:mx-4"&gt;
    &lt;h1 class="text-2xl"&gt;
      Привет, &lt;b&gt;{{ fullName }}&lt;/b&gt;!
    &lt;/h1&gt;
    &lt;div class="flex justify-center md:block"&gt;
      &lt;PillTag label="Подтвержден" color="info" :icon="mdiCheckDecagram" /&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/BaseLevel&gt;
&lt;/CardBox&gt;
</code>
</pre>

<h2>Код для извлечения информации о текущем пользователе</h2>
<pre>
<code>
export default {
  data() {
    return {
      userProfile: {},
      form: {
        firstName: '',
        lastName: '',
      },
    };
  },
  computed: {
    fullName() {
      return `${this.form.firstname} ${this.form.lastname}`;
    },
  },
  async created() {
    await this.fetchUserProfile();
  },
  methods: {
    async fetchUserProfile() {
      try {
        const mainStore = useMainStore();
        const response = await axios.get(`http://localhost:8000/api/insureagent/?username=${mainStore.userName}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
        this.userProfile = response.data;
        this.form.firstname = this.userProfile[0].firstname;
        this.form.lastname = this.userProfile[0].lastname;
      } catch (error) {
        console.error("There was an error fetching the user's profile:", error);
      }
    },
  },
};
</code>
</pre>

<h2>Обработка изменения логина</h2>
<pre>
<code>
export default {
  data() {
    return {
      userProfile: {},
      form: {
        username: mainStore.userName,
      },
    };
  },
  methods: {
    async updateProfile() {
      try {

        const payload = {
          username: this.form.username,
        };
        const resp = await api.get(`/insureagent/?username=${mainStore.userName}`, {headers: {"Authorization": `Token ${mainStore.token}`}});
        const id = resp.data[0].id;
        await api.patch(`/insureagent/${id}/`, payload, {headers: {"Authorization": `Token ${mainStore.token}`}});
        mainStore.userName = payload.username;
        this.$router.go(0);
      } catch (error) {
        console.error("There was an error updating the user's profile:", error);
      }
    },
  },
};
</code>
</pre>
