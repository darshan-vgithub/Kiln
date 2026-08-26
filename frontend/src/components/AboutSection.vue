<script setup>
import Darshan from '../assets/team/Darshan.png'
import Ritesh from '../assets/team/Ritesh.jpeg'
import Vivek from '../assets/team/Vivek.jpeg'
import Keyur from '../assets/team/Keyur.jpeg'
const team = [
  {
    name: 'Keyur Ramani',
    role: 'Founder & Financial Engineer',
    bio: 'The brains behind the operation — finance, strategy, and product design.',
    initials: 'KR',
    photo: Keyur,
  },
  {
    name: 'Darshan Venkatesh Murthy',
    role: 'Founder & Full Stack Engineer',
    bio: 'Building the product and making sure it works for you.',
    initials: 'DV',
    photo: Darshan,
  },
  {
    name: 'Ritesh Ghorpade',
    role: 'Founder | Data Engineer | Product Manager',
    bio: 'APIs, databases, and infrastructure that hold up under real traffic.',
    initials: 'RG',
    photo: Ritesh,
  },
  {
    name: 'Vivek Rokde',
    role: 'Founder & Frontend Engineer',
    bio: 'Building the user interface and ensuring a great user experience.',
    initials: 'VR',
    photo: Vivek,
  },
]
</script>

<template>
  <section id="about" class="about">
    <div class="head">
      <span class="eyebrow">ABOUT US</span>
      <h2>The people building your product</h2>
      <p class="lede">
        We're a small, hands-on team — no account managers between you and the people
        actually writing the code.
      </p>
    </div>

    <div class="grid">
      <article v-for="member in team" :key="member.name" class="card">
        <img
          v-if="member.photo"
          :src="member.photo"
          :alt="member.name"
          class="avatar-photo"
        />
        <div v-else class="avatar" aria-hidden="true">{{ member.initials }}</div>
        <h3>{{ member.name }}</h3>
        <span class="role">{{ member.role }}</span>
        <p>{{ member.bio }}</p>
      </article>
    </div>
  </section>
</template>

<style scoped>
.about {
  padding: 2rem clamp(1.25rem, 4vw, 3rem) 4rem;
  max-width: 74rem;
  margin: 0 auto;
}

.head {
  max-width: 40rem;
  margin-bottom: 2.2rem;
}

.eyebrow {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--steel);
  margin-bottom: 0.6rem;
}

h2 {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: clamp(1.7rem, 3vw, 2.3rem);
  margin: 0 0 0.6rem;
  letter-spacing: -0.01em;
}

.lede {
  color: var(--text-muted);
  margin: 0;
  line-height: 1.6;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15.5rem, 1fr));
  gap: 1.1rem;
}

.card {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  padding: 1.6rem;
  transition: border-color 0.15s ease, background 0.15s ease;
}

.card:hover {
  border-color: rgba(61, 139, 253, 0.35);
  background: var(--surface-2);
}

.avatar-photo {
  width: 3.4rem;
  height: 3.4rem;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1rem;
  border: 1px solid var(--line);
}

.avatar {
  width: 2.8rem;
  height: 2.8rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--ember), var(--steel));
  color: #0b0c0f;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

h3 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 600;
  margin: 0 0 0.25rem;
}

.role {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.04em;
  color: var(--ember);
  margin-bottom: 0.7rem;
}

p {
  color: var(--text-muted);
  font-size: 0.92rem;
  line-height: 1.55;
  margin: 0;
}
</style>