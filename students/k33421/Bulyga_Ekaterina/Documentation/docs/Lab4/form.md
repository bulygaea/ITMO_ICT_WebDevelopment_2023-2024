<h1>Страница с формой для создания нового договора</h1>
<p>На странице можно выбрать юридическое лицо и физическое. Информация о страховом агенте, добавляющем эту запись, и о его страховой организации вставляются автоматически и недоступны для изменения.</p>

<img src="../form1.png">
<img src="../form2.png">

<h2>Шаблон</h2>
<pre>
<code>
&lt;LayoutAuthenticated&gt;
&lt;SectionMain&gt;
  &lt;SectionTitleLineWithButton :icon="mdiBallotOutline" title="Форма" main/&gt;
  &lt;CardBox form @submit.prevent="submit"&gt;
    &lt;FormField label="Страховой агент"&gt;
      &lt;FormControl v-model="form.name" :icon="mdiAccount" :readonly="true"/&gt;
      &lt;FormControl v-model="form.insureorganization" :readonly="true"/&gt;
    &lt;/FormField&gt;

    &lt;FormField label="Юридическое лицо"&gt;
      &lt;FormControl v-model="form.organization" :options="selectOrganization"/&gt;
    &lt;/FormField&gt;

    &lt;FormField label="Физическое лицо"&gt;
      &lt;FormControl v-model="form.client" :options="selectClient"/&gt;
    &lt;/FormField&gt;

    &lt;template #footer&gt;
      &lt;BaseButtons&gt;
        &lt;BaseButton type="submit" color="info" label="Создать" @click="submit"/&gt;
      &lt;/BaseButtons&gt;
    &lt;/template&gt;
  &lt;/CardBox&gt;
&lt;/SectionMain&gt;

&lt;/LayoutAuthenticated&gt;
</code>
</pre>

<h2>Обработчик формы</h2>
<pre>
<code>
export default {
  methods: {
    async submit() {
      const resp2 = await axios.get(`http://localhost:8000/api/organization/?fullname=${form.organization}`, {'headers': {'Authorization': `Token ${mainStore.token}`}})
      const resp3 = await axios.get(`http://localhost:8000/api/individual/?firstname=${form.client.split(' ')[0]}&lastname=${form.client.split(' ')[1]}`, {'headers': {'Authorization': `Token ${mainStore.token}`}})

      const id = response2.data[0].id;
      console.log({
        'date_from': '2024-03-20',
        'date_to': '2024-10-20',
        'organization': resp2.data[0]['code'],
        'client': resp3.data[0]['id'],
        'agent': id
      });

      axios.post(`http://127.0.0.1:8000/api/contract/`, {
        'date_from': '2024-03-20',
        'date_to': '2024-10-20',
        'organization': resp2.data[0]['code'],
        'client': resp3.data[0]['id'],
        'agent': id
      }, {'headers': {'Authorization': `Token ${mainStore.token}`}});

      this.$router.go(0);
    },
  }
}
</code>
</pre>
