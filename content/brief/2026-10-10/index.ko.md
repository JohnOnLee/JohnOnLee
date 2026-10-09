---
title: "Cloudflare, Deno 팀 인수 — Deno 런타임 종료 수순"
date: 2026-10-10
summary: "10월 9일 Cloudflare와 Deno가 각각 발표했습니다. Deno 팀 전체가 Cloudflare로 합류하고, 노드.js를 만든 Ryan Dahl과 공동 창업자 Bert Belder가 Deno가 8월에 공개한…"
---

## Cloudflare가 Deno 팀 전체를 받아들이고, Deno 런타임과 Deploy는 정리 수순에 들어갔습니다

10월 9일 Cloudflare와 Deno가 각각 발표했습니다. Deno 팀 전체가 Cloudflare로 합류하고, 노드.js를 만든 Ryan Dahl과 공동 창업자 Bert Belder가 Deno가 8월에 공개한 celld를 Cloudflare의 오픈소스 런타임 workerd에 합치는 작업을 맡습니다. 두 회사가 내건 목표는 Workers 프로그래밍 모델을 Cloudflare 네트워크가 아니라 자기 인프라에서 돌리는 일을 정식 지원 경로로 만드는 것입니다. 인수 금액은 공개되지 않았습니다. [Deno](https://deno.com/blog/cloudflare) [Cloudflare](https://blog.cloudflare.com/deno-joins-cloudflare/) [The New Stack](https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl/)

일정은 발표문에 숫자로 적혀 있습니다. Deno 런타임은 1년 동안 매달 버그 수정과 보안 패치를 받고, 그 뒤에는 Deno 팀의 개발이 끝납니다. 코드는 오픈소스로 남고 이어서 개발할 사람은 환영한다는 조건입니다. 호스팅 서비스인 Deno Deploy는 6개월 더 운영한 뒤 종료되고, 유료 고객에게는 Cloudflare Workers로 옮기는 이전 지원이 제공됩니다. 패키지 레지스트리 JSR은 계속 운영되며 인프라는 Cloudflare로 이동합니다. Cloudflare는 workerd를 공개한 뒤 셀프 호스팅 생태계가 따라와 주기를 기대했지만 그렇게 되지 않았고, 직접 굴리는 Durable Objects는 단일 인스턴스까지만 지원했다고 밝혔습니다.

## 지금 확인할 것은 마이그레이션 일정이고, 남는 질문은 그 다음입니다

Deno Deploy에 서비스를 올려 둔 팀이라면 남은 시간은 6개월입니다. 런타임만 쓰고 서버는 직접 굴리는 팀이라면 1년 뒤부터 새 기능이 붙지 않는 런타임을 안고 가게 됩니다. 오늘 당장 깨지는 것은 없지만, 다음 분기에 Deno 위에 새 서비스를 얹을 계획이었다면 그 전에 방향을 정하는 편이 낫습니다.

이번 발표로 나가는 길의 주인이 바뀌었습니다. workerd는 Cloudflare가 프로덕션에서 쓰는 런타임을 그대로 공개한 코드이고, Workers 위에 쌓은 앱을 다른 인프라로 옮길 때 쓰는 통로였습니다. 그 통로를 대신 만들어 주던 celld를 만든 팀이 Cloudflare로 들어갔고, 앞으로 셀프 호스팅용 Durable Objects는 Cloudflare가 직접 만듭니다. 에이전트 제품을 만드는 쪽에는 이 모델이 잘 맞습니다. Durable Object 하나가 자기 SQLite를 가진 작은 서버처럼 동작하고 WebSocket 연결을 들고 있으니, 사용자별 상태와 실시간 연결이 필요한 에이전트 하네스를 같은 방식으로 나눠 담을 수 있습니다. celld는 오브젝트 스토리지 하나만 외부 의존성으로 두는 단일 바이너리입니다.

지금 바로 프로덕션에 얹을 수 있는 물건은 아닙니다. workerd와 celld를 합친 결과물은 아직 없고, 두 회사가 밝힌 것은 앞으로 몇 달간의 추가 발표뿐입니다. Deno Deploy가 닫히는 날과 런타임 지원이 끝나는 날 모두 연도만 정해졌습니다. 셀프 호스팅을 계획하고 있었다면 지금은 celld와 workerd를 직접 띄워 보는 단계이고, 새 프로젝트의 기본 런타임을 Deno로 잡는 결정은 미루는 편이 안전합니다.

## 오늘의 다른 소식 (한 줄)

- **Anthropic, Claude Managed Agents에 동적 워크플로 베타 공개**: 에이전트가 워크플로 프로그램을 직접 써서 최대 1,000개 하위 에이전트를 여러 단계로 돌리고 결과를 합칩니다. 11만 6천 줄 코드베이스에 심은 버그 70개를 단일 에이전트는 14~27개 찾았고 워크플로는 66개를 찾았다고 회사가 밝혔습니다. [Claude Platform 릴리스 노트](https://platform.claude.com/docs/en/release-notes/overview)
- **Oxide Computer, 4억 4,500만 달러 Series D**: Eclipse가 주도했고 AMD Ventures 등이 참여했습니다. 온프레미스 클라우드 장비를 파는 회사로, 2026년 봄 영업이익 기준으로 법인세를 냈다고 밝혔습니다. [Oxide](https://oxide.computer/blog/our-445m-series-d)
- **OpenAI, 해고된 안전 연구원 3명 관련 입장 발표**: 회사는 신뢰 위반이라며 발언 때문이 아니라고 했고, 해고된 연구원들은 위축 효과를 경고했습니다. [CNBC](https://www.cnbc.com/2026/10/09/openai-fired-researchers-ai-concerns.html)
- **OpenAI 연환산 매출 500억 달러, 연말 700억 달러 전망**: 9월 말 기준 약 500억 달러이고, 블룸버그 보도에 따르면 연말 700억 달러 이상을 투자자에게 제시했습니다. [TNW](https://thenextweb.com/news/openai-revenue-70bn-year-end-50bn-september)
- **Arena, 2억 달러 Series B와 Alignment Index 공개**: 기업가치는 31억 달러이고 Lightspeed와 Khosla가 공동 주도했습니다. 에이전트가 지시를 따르고 완료를 정확히 보고하는지 평가하는 지표를 함께 내놨습니다. [Tech Startups](https://techstartups.com/2026/10/09/startup-funding-news-today-october-9-2026-arena-bloomx-ocean-scanntech-more/)