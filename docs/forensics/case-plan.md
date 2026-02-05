## Case Plan

Goal: The purpose of this work paper is to evidence the audit plan. We used the Beanstalk Exploit as a study-case.

## Case
Beanstalk Governance Attack (Apr 17-24, 2022) 
<br> Chain: Ethereum <br> attacker EOA: 0x1c5dcdd006ea78a7e4783f9e6021c32935a10fb4 <br> seed tx: 0xcd314668aaa9bbfebaf1a0bd2b6553d01dd58899c508d4729fa7311dc5d33ad7

## Audit Questions
Goal: The purpose of this work paper is to evidence the audit questions, metrics, and the evidence of the case analysed.

| Audit Questions | Measure | Evidence |
| --- | --- | --- |
| Who were the top 10 receivers? | Total wei (ETH) value received per address within 48h / 7d. | List of the top 10 destination addresses.|
| Which exit sinks were used? | Total value sent to labeled sinks (mixer/bridges/CEX) within 48h / 7d | - List of identified sink addresses (e.g. labeled mixer / labeled CEX / labeled bridge) linked to the exploit. <br> - Label source:  post-mortem reference. |
| How fast did the funds move? | % of total outflow moved within 1h, 6h, 48h | Table + chart from notebook |

## Minimum Dataset
- seed tx receipt/logs
- outbound tx list (48h, 7d)
- top 10 receivers table

## Sources
- Primary (on-chain): JSON-RPC/Etherscan
- Secundary (post-mortem): report/blog

## Evidence Plan
- Script's terminal output
- Notebook output

