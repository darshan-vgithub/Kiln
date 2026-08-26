<script setup>
const year = new Date().getFullYear()
</script>

<template>
  <footer class="footer">
    <div class="inner">
      <span class="brand">Kiln</span>
      <span class="copy">© {{ year }} Kiln. All rights reserved.</span>
      <div class="social">
        <a href="#" aria-label="GitHub">GitHub</a>
        <a href="#" aria-label="LinkedIn">LinkedIn</a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  border-top: 1px solid var(--line);
  padding: 1.8rem clamp(1.25rem, 4vw, 3rem);
}

.inner {
  max-width: 74rem;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  color: var(--text-muted);
  font-size: 0.86rem;
}

.brand {
  font-family: var(--font-display);
  font-weight: 600;
  color: var(--text);
}

.social {
  display: flex;
  gap: 1.1rem;
}

.social a {
  text-decoration: none;
  color: var(--text-muted);
}

.social a:hover {
  color: var(--text);
}
</style>
