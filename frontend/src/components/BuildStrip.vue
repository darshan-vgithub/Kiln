<script setup>
const stages = ['Idea', 'Design', 'Build', 'Ship']
</script>

<template>
  <div class="strip" role="img" aria-label="Our pipeline: idea, design, build, ship">
    <svg viewBox="0 0 1040 120" preserveAspectRatio="xMidYMid meet" class="strip-svg">
      <defs>
        <linearGradient id="traceGradient" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="var(--ember)" />
          <stop offset="100%" stop-color="var(--steel)" />
        </linearGradient>
      </defs>

      <!-- base trace: right-angled circuit path connecting four stage nodes -->
      <path
        class="trace-base"
        d="M60,60 H260 V30 H420 V90 H620 V30 H780 V60 H980"
        fill="none"
        stroke="var(--line)"
        stroke-width="2"
      />
      <!-- animated pulse trace, same path, drawn with a moving dash -->
      <path
        class="trace-pulse"
        d="M60,60 H260 V30 H420 V90 H620 V30 H780 V60 H980"
        fill="none"
        stroke="url(#traceGradient)"
        stroke-width="2.5"
        stroke-linecap="round"
      />

      <g v-for="(stage, i) in stages" :key="stage">
        <circle
          :cx="60 + i * 306.6"
          cy="60"
          r="7"
          class="node"
          :style="{ animationDelay: `${i * 0.35}s` }"
        />
      </g>
    </svg>

    <div class="labels">
      <span v-for="stage in stages" :key="stage" class="label">{{ stage }}</span>
    </div>
  </div>
</template>

<style scoped>
.strip {
  width: 100%;
  max-width: 62rem;
  margin-inline: auto;
}

.strip-svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

.trace-pulse {
  stroke-dasharray: 90 1400;
  stroke-dashoffset: 0;
  animation: travel 3.2s linear infinite;
  filter: drop-shadow(0 0 6px rgba(255, 107, 53, 0.35));
}

@keyframes travel {
  from {
    stroke-dashoffset: 1490;
  }
  to {
    stroke-dashoffset: 0;
  }
}

.node {
  fill: var(--bg);
  stroke: var(--text-muted);
  stroke-width: 1.5;
  animation: pulse-node 3.2s ease-in-out infinite;
}

@keyframes pulse-node {
  0%, 88%, 100% {
    stroke: var(--text-muted);
  }
  4%, 20% {
    stroke: var(--ember);
    filter: drop-shadow(0 0 5px rgba(255, 107, 53, 0.6));
  }
}

.labels {
  display: flex;
  justify-content: space-between;
  padding: 0 3%;
  margin-top: 0.4rem;
}

.label {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--text-muted);
}

@media (prefers-reduced-motion: reduce) {
  .trace-pulse,
  .node {
    animation: none;
  }
  .trace-pulse {
    stroke-dasharray: none;
  }
}
</style>
