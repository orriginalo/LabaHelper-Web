<script>
import { marked } from 'marked'
import hljs from 'highlight.js'
import 'highlight.js/styles/github-dark.css'

export default {
  props: {
    markdown: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      copyButtons: [],
    }
  },
  computed: {
    formattedMarkdown() {
      return marked(this.markdown, {
        highlight: (code, lang) => {
          const validLang = hljs.getLanguage(lang) ? lang : 'plaintext'
          return hljs.highlight(code, { language: validLang }).value
        },
        breaks: true,
      })
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.processCodeBlocks()
    })
  },
  updated() {
    this.$nextTick(() => {
      this.processCodeBlocks()
    })
  },
  methods: {
    processCodeBlocks() {
      // Удаляем старые обработчики
      this.copyButtons.forEach((btn) => {
        btn.removeEventListener('click', this.handleCopyClick)
      })
      this.copyButtons = []

      // Обрабатываем все блоки кода
      const preElements = this.$el.querySelectorAll('pre')

      preElements.forEach((pre) => {
        // Пропускаем уже обработанные блоки
        if (pre.classList.contains('processed')) return

        // Добавляем класс для предотвращения повторной обработки
        pre.classList.add('processed')

        // Создаем контейнер
        const container = document.createElement('div')
        container.className = 'code-block relative'

        // Создаем кнопку копирования
        const button = document.createElement('button')
        button.className = 'copy-button'
        button.textContent = 'Скопировать код'
        button.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></g></svg>
        `

        // Получаем чистый код (без HTML тегов)
        const code = pre.querySelector('code').textContent
        button.dataset.code = code

        // Добавляем обработчик
        button.addEventListener('click', this.handleCopyClick)
        this.copyButtons.push(button)

        // Вставляем контейнер и перемещаем в него pre
        pre.parentNode.insertBefore(container, pre)
        container.appendChild(pre)
        container.appendChild(button)

        // Подсвечиваем синтаксис
        hljs.highlightElement(pre.querySelector('code'))
      })
    },
    handleCopyClick(event) {
      const button = event.currentTarget
      const code = button.dataset.code

      navigator.clipboard
        .writeText(code)
        .then(() => {
          this.showCopyFeedback(button)
        })
        .catch((err) => {
          console.error('Ошибка при копировании:', err)
          button.textContent = 'Ошибка!'
          button.style.backgroundColor = '#EF4444'
          setTimeout(() => {
            button.innerHTML = `
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></g></svg>
            `
            button.textContent = 'Скопировать код'
            button.style.backgroundColor = '#3B82F6'
          }, 2000)
        })
    },
    showCopyFeedback(button) {
      const originalText = button.textContent
      button.style.backgroundColor = '#10B981'
      button.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="currentColor" d="m9.55 15.15l8.475-8.475q.3-.3.7-.3t.7.3t.3.713t-.3.712l-9.175 9.2q-.3.3-.7.3t-.7-.3L4.55 13q-.3-.3-.288-.712t.313-.713t.713-.3t.712.3z"/></svg>
      `

      setTimeout(() => {
        button.textContent = originalText
        button.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></g></svg>
        `
        button.style.backgroundColor = '#3B82F6'
      }, 2000)
    },
  },
}
</script>

<template>
  <main class="flex h-full justify-center w-full items-center p-2">
    <div class="w-full md:w-3/4 h-full bg-zinc-800 p-4 sm:p-6 rounded-2xl text-white transition-all">
      <article
        v-html="formattedMarkdown"
        class="prose prose-invert lg:prose-lg max-w-none text-base sm:text-lg"
      ></article>
    </div>
  </main>
</template>

<style>
.prose pre {
  background-color: #1e1e1e;
  padding: 0.1rem;
  border-radius: 8px;
  overflow: auto;
  color: white;
  margin-bottom: 2.5rem;
  margin-top: 0.3rem;
}

.prose code {
  font-size: 0.875rem;
  font-family: monospace;
  background-color: transparent;
  padding: 0;
}

.code-block {
  position: relative;
}

.copy-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: #3b82f6;
  color: white;
  padding: 5px 10px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.3s;
  border: none;
  outline: none;
  z-index: 10;
}

.copy-button:hover {
  background-color: #2563eb;
}

.prose p {
  font-size: 1rem;
}

@media (min-width: 640px) {
  .prose p {
    font-size: 1.2rem;
  }
}

.prose h1 {
  font-size: 1.6rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

@media (min-width: 640px) {
  .prose h1 {
    font-size: 2.5rem;
  }
}

.prose h2 {
  font-size: 1.3rem;
  font-weight: bold;
  margin-bottom: 0.75rem;
}

@media (min-width: 640px) {
  .prose h2 {
    font-size: 1.95rem;
  }
}

.prose h3 {
  font-size: 1.15rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  margin-top: 0.5rem;
}

@media (min-width: 640px) {
  .prose h3 {
    font-size: 1.7rem;
  }
}

</style>

