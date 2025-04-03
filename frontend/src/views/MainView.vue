<script>
import axios from 'axios'
import LabaComponent from '@/components/LabaComponent.vue'
import { marked } from 'marked'
import StartComponent from '@/components/StartComponent.vue'

export default {
  name: 'MainView',
  components: {
    LabaComponent,
    StartComponent,
  },
  data() {
    return {
      sections: [],
      activeSection: null, // Секция по умолчанию
      sidebarOpen: true,
    }
  },
  methods: {
    toggleSidebar () {
      this.sidebarOpen = !this.sidebarOpen;
      console.log(this.sidebarOpen);
    },
    async nullActiveSection() {
      this.activeSection = null
    },
    async setActiveSection(section_id) {
      // Найдем секцию по ID
      const section = this.sections.find((s) => s.id === section_id)
      if (section) {
        this.activeSection = section // Устанавливаем активную секцию
      }
    },
  },
  computed: {
    formattedMarkdown() {
      return this.activeSection ? marked(this.activeSection.markdown) : ''
    },
  },
  async mounted() {
    try {
      const response = await axios.get('https://api.orriginalo.ru/api/labs') // Получаем данные
      console.log('Респонсе: ', response.data)

      this.sections = response.data['labs']
      // Установим активную секцию по умолчанию
      // this.setActiveSection(this.sections[0].id)
    } catch (err) {
      console.error(err)
    }

    console.log('Компонент загружен!')
  },
}
</script>

<template>
  <main class="flex bg-zinc-700 h-full">
    <!-- Кнопка открытия сайдбара -->
    <button
      @click="toggleSidebar"
      class="text-xl fixed top-2 left-3 z-50 px-1 pb-0.5 text-white cursor-pointer"
    >
      ☰
    </button>

    <!-- Левая панель -->
    <div
      class="sticky bg-zinc-800 flex flex-col items-start p-4 space-y-2 h-screen transition-all duration-300 ease-in-out md:w-80"
      :class="{
        'left-0 top-0 w-80 z-40': sidebarOpen,
        'hidden': !sidebarOpen,
      }"
    >
      <div class="mt-5">
        <span class="text-xl text-neutral-500">orriginalo/</span><br />
        <span
          class="text-2xl font-black text-white hover:cursor-pointer"
          :onClick="nullActiveSection"
        >
          LabaHelper <br />
          Web
        </span>
      </div>
      <div class="space-y-2 overflow-y-auto rounded-xl py-2">
        <button
          v-for="section in sections"
          :key="section.id"
          @click="setActiveSection(section.id)"
          class="w-full text-left p-2 text-white rounded-md hover:cursor-pointer focus:outline-none transition-all"
          :class="
            activeSection != null && section.id === activeSection.id
              ? 'bg-zinc-400'
              : 'bg-zinc-700 hover:bg-zinc-500'
          "
        >
          {{ section.name }}
        </button>
      </div>
    </div>

    <!-- Контент -->
    <div class="flex-1 overflow-y-auto h-full">
      <div class="bg-zinc-900 w-full h-full flex flex-col items-center p-4">
        <LabaComponent v-if="activeSection != null" :markdown="activeSection.markdown" />
        <StartComponent v-else />
      </div>
    </div>
  </main>
</template>


<style scoped>
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    z-index: 40;
    background-color: #27272a;
    transition: transform 0.3s ease-in-out;
  }
  .sidebar-hidden {
    transform: translateX(-100%);
  }
}
</style>
