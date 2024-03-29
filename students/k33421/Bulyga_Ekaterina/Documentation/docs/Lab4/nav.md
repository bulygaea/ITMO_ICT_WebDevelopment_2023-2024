<h1>Меню слева и сверху</h1>
<p>Навигация слева и сверху реализована одинаково за исключением особенностей, связанный с их разметкой на странице. Рассмотрим подробнее, как работает меню слева.</p>

<img src="../nav.png">

<h2>Шаблон</h2>
<pre>
<code>
&lt;aside
id="aside"
class="lg:py-2 lg:pl-2 w-60 fixed flex z-40 top-0 h-screen transition-position overflow-hidden"
&gt;
&lt;div class="aside lg:rounded-2xl flex-1 flex flex-col overflow-hidden dark:bg-slate-900"&gt;
  &lt;div class="aside-brand flex flex-row h-14 items-center justify-between dark:bg-slate-900"&gt;
    &lt;div class="text-center flex-1 lg:text-left lg:pl-6 xl:text-center xl:pl-0"&gt;
      &lt;b class="font-black"&gt;Меню&lt;/b&gt;
    &lt;/div&gt;
    &lt;button class="hidden lg:inline-block xl:hidden p-3" @click.prevent="asideLgCloseClick"&gt;
      &lt;BaseIcon :path="mdiClose" /&gt;
    &lt;/button&gt;
  &lt;/div&gt;
  &lt;div
    class="flex-1 overflow-y-auto overflow-x-hidden aside-scrollbars dark:aside-scrollbars-[slate]"
  &gt;
    &lt;AsideMenuList :menu="menu" @menu-click="menuClick" /&gt;
  &lt;/div&gt;

  &lt;ul&gt;
    &lt;AsideMenuItem :item="logoutItem" @click="onClick" /&gt;
  &lt;/ul&gt;
&lt;/div&gt;
&lt;/aside&gt;
</code>
</pre>

<h2>Обработка выхода из аккаунта</h2>
<p>Код ниже запускает функцию <code>unset()</code>, которая представлена в описании страницы входа.</p>
<pre>
<code>
export default {
  methods: {
    async onClick() {
      mainStore.unsetUser();
      this.$router.go(0);
    }
  }
}
</code>
</pre>

<p>После того, как пользователь вышел из аккаунта, зайти на страницы напрямую по ссылке будет невозможно, т.к. в каждой странице есть проверка наличия токена.</p>

<pre>
<code>
const mainStore = useMainStore();

if (mainStore.token === '') {
  mainStore.token = localStorage.getItem('auth_token');
  router.push({path: '/'});
}
</code>
</pre>
