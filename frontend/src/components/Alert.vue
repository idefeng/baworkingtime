<template>
    <div>
      <b-alert variant="success" show>{{ message }}</b-alert>
    </div>
</template>

<script>
export default {
  name: 'Alert',
  props: ['message']
}
</script>

<style scoped>

</style>
