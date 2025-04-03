<template>
  <main class="text-white font-mono h-screen flex items-center justify-center">
    <div class="grid grid-cols-2 grid-rows-2 gap-4 place-content-center">
      <div
        class="col-span-2 text-center bg-zinc-800 p-6 rounded-2xl flex flex-col justify-center relative hover:scale-[101%] transition-transform"
      >
        <span class="absolute top-2 left-2 text-zinc-400 text-lg">1</span>
        <p class="font-bold text-5xl mb-4">LabaHelper Web</p>
        <p class="text-2xl">
          На этой странице вы можете найти решенные лабораторные работы, которые были даны по курсу
          "Индивидуальный проект 2025 КЭИ"
        </p>
      </div>

      <div
        class="text-5xl row-start-2 bg-zinc-800 p-6 rounded-2xl flex items-center relative hover:scale-[101%] transition-transform"
      >
        <span class="absolute top-2 left-2 text-zinc-400 text-lg">3</span>
        <p>выбери слева нужную тебе работу.</p>
      </div>

      <div
        class="text-xl row-start-2 bg-zinc-800 p-6 rounded-2xl flex flex-col justify-center relative hover:scale-[101%] transition-transform"
      >
        <span class="absolute top-2 left-2 text-zinc-400 text-lg">2</span>
        <p>В коде некоторых лабораторных работ присутствуют "маркеры", обозначенные как:</p>
        <ul class="bg-zinc-700 p-1 my-2 rounded-xl w-min whitespace-nowrap">
          <li>`<code>!!!!!</code>`</li>
          <li>`<code>// !!!</code>`</li>
        </ul>
        <p>
          Они означают, что в месте где стоит маркер если это `!!!!!` или в код находящимся под `//
          !!!` можно внести свои изменения. Изменить числа, надписи и т.д.
        </p>
      </div>
    </div>
  </main>
</template>
