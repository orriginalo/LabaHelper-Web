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
    }
  },
  methods: {
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
      const response = await axios.get('https://api.orriginalo/api/labs') // Получаем данные
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
    <!-- Левая панель с кнопками -->
    <div class="bg-zinc-800 w-80 flex flex-col items-start p-4 space-y-2 h-screen sticky top-0">
      <div>
        <span class="text-xl text-neutral-500">orriginalo/</span><br />
        <span
          class="text-2xl font-black text-white hover:cursor-pointer"
          :onClick="nullActiveSection"
        >
          LabaHelper <br />
          Web
        </span>
      </div>
      <div class="space-y-2 overflow-y-auto">
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
    <!-- Контент активной секции -->
    <div class="flex-1 overflow-y-auto h-full">
      <div class="bg-zinc-900 w-full h-full flex flex-col items-center p-4">
        <LabaComponent v-if="activeSection != null" :markdown="activeSection.markdown" />
        <StartComponent v-else />
      </div>
    </div>
  </main>
</template>
