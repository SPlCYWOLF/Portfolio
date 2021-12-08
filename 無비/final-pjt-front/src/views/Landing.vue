<template>
  <transition name="fade">
  <div v-if="showLanding" class="landing-page">
    <transition name="fade"><div v-if="explanation" class="explanation">(영화 추천 사이트입니다ㅎ;)</div></transition>
    <div class="fade-in-text">無</div>    
      <div class="awesome-button">
        <link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet">
        <a @mouseover="explanation=true" @mouseleave="explanation=false" class="jebal" href="javascript:void(0)" >
          <span class="enter" @click="hasLanded">Enter</span>
          <div class="wave"></div>
        </a>
      </div>  
      <div class="fade-in-box">
        <img style="width: 100%; height:auto;" src="@/assets/landing2.jpg"/>
      </div>
  </div>
  </transition>
  
</template>

<script>
export default {
  name: 'Landing',
  data: function () {
    return {
      explanation: false,
      showLanding: true,
    }
  },
  methods: {
    hasLanded: function () {
      this.showLanding = false,
      this.$emit('landed')
    },
  }
  
}
</script>

<style>
  @import '../assets/styles/LandingSrc.css';
</style>