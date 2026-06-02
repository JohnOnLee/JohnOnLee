---
title: "코딩 에이전트 커스터마이징 — 설문"
date: 2026-06-03
hideMeta: true
---

<div style="text-align: center; margin: 3rem 0;">

## 🛠️ 코딩 에이전트, 얼마나 깊게 쓰고 계신가요?

<p style="font-size: 1.2rem; color: var(--secondary); margin: 1.5rem 0;">
7문항 · 2분 소요 · 익명 · 제출 후 실시간 결과 확인
</p>

<p style="margin: 2rem 0;">
<span id="countdown" style="font-size: 2rem; font-weight: 700; color: var(--primary);">3</span>
</p>

<p style="color: var(--secondary);">
설문 폼으로 이동 중입니다...
</p>

<p style="margin-top: 2rem;">
<a href="https://forms.gle/22hwLNNzk5BQZ2QP6" style="font-size: 1rem; padding: 0.6rem 1.5rem; background: var(--primary); color: var(--theme); border-radius: 6px; text-decoration: none;">
→ 설문으로 바로 가기
</a>
</p>

<p style="margin-top: 1.5rem; font-size: 0.85rem; color: var(--secondary);">
이동되지 않으면 <a href="https://forms.gle/22hwLNNzk5BQZ2QP6">여기를 클릭</a>하세요.
</p>

</div>

<script>
(function() {
  var count = 3;
  var el = document.getElementById('countdown');
  var timer = setInterval(function() {
    count--;
    if (count <= 0) {
      clearInterval(timer);
      window.location.href = 'https://forms.gle/22hwLNNzk5BQZ2QP6';
    } else {
      el.textContent = count;
    }
  }, 1000);
})();
</script>
