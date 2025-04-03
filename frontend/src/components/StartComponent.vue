<template>
  <main class="text-white font-mono h-screen flex items-center justify-center p-2">
    <div class="flex flex-col lg:grid sm:grid-cols-2 sm:grid-rows-2 gap-2 sm:gap-4 place-content-center w-full max-w-[95%]">
      <!-- Главный блок -->
      <div
        class="col-span-2 text-center bg-zinc-800 p-4 sm:p-6 rounded-2xl flex flex-col justify-center relative hover:scale-[101%] transition-transform"
      >
        <span class="absolute top-2 left-2 text-zinc-400 text-lg">1</span>
        <p class="font-bold text-3xl sm:text-5xl mb-4">LabaHelper Web</p>
        <p class="text-lg sm:text-2xl">
          На этой странице вы можете найти решенные лабораторные работы, которые были даны по курсу
          "Индивидуальный проект 2025 КЭИ"
        </p>
      </div>

      <!-- Выбор лабораторных -->
      <div
        class="text-2xl sm:text-5xl row-start-2 bg-zinc-800 p-4 sm:p-6 rounded-2xl flex items-center relative hover:scale-[101%] transition-transform"
      >
        <span class="absolute top-2 left-2 text-zinc-400 text-lg">3</span>
        <p class="text-center sm:text-left">выбери слева нужную тебе работу.</p>
      </div>

      <!-- Маркеры -->
      <div
        class="text-base sm:text-xl row-start-2 bg-zinc-800 p-4 sm:p-6 rounded-2xl flex flex-col justify-center relative hover:scale-[101%] transition-transform"
      >
        <span class="absolute top-2 left-2 text-zinc-400 text-lg">2</span>
        <p class="text-center sm:text-left">
          В коде некоторых лабораторных работ присутствуют "маркеры", обозначенные как:
        </p>
        <ul class="bg-zinc-700 p-1 my-2 rounded-xl w-min whitespace-nowrap mx-auto sm:mx-0">
          <li>`<code>!!!!!</code>`</li>
          <li>`<code>// !!!</code>`</li>
        </ul>
        <p class="text-center sm:text-left">
          Они означают, что на той же строчке где стоит маркер, если это `!!!!!`, или в коде под `// !!!`
          можно внести свои изменения. Изменить числа, надписи и т.д.
        </p>
      </div>
    </div>
  </main>
</template>
