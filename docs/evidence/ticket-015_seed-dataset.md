# Ticket 015 - Seed Dataset

## Command
```bash
head -n 4 docs/forensics/seed-data.csv
wc -l docs/forensics/seed-data.csv
awk -F, '{print NR, NF}' docs/forensics/seed-data.csv | tail -n 5
```

## Output 
```text | Note: terminal wraps long lines; schema validated with awk (NF=8).
date_utc,block_number,tx_hash,from_address,to_address,value_or_token,label,source
2022-04-17T12:24:16Z,14602790,0xcd314668aaa9bbfebaf1a0bd2b6553d01dd58899c508d4729fa7311dc5d33
ad7,0x1c5dCdd006EA78a7E4783f9e6021C32935a10fb4,0x79224bc0bf70ec34f0ef56ed8251619499a59def,0 ETH,exploit_tx,https://etherscan.io/tx/0xcd314668aaa9bbfebaf1a0bd2b6553d01dd58899c508d4729fa7311dc5d33ad7                                                                                  2022-04-17T14:56:04Z,14603456,0x3bc6c39d2579517f37c9ee20ac3345c99447a5464e060114a5ad3b19a57b7
b7c,0x1c5dCdd006EA78a7E4783f9e6021C32935a10fb4,0xd90e2f925DA726b50C4Ed8D0Fb90Ad053324F31b,100 ETH,deposit_tornado_cash,https://etherscan.io/tx/0x3bc6c39d2579517f37c9ee20ac3345c99447a5464e060114a5ad3b19a57b7b7c                                                                      2022-04-17T14:55:51Z,14603455,0xe8b60dc187cf44e28516774865d8c9bcef88a8b36079ec14f125402b7f000
a3a,0x1c5dCdd006EA78a7E4783f9e6021C32935a10fb4,0xd90e2f925DA726b50C4Ed8D0Fb90Ad053324F31b,100 ETH,deposit_tornado_02,https://etherscan.io/tx/0xe8b60dc187cf44e28516774865d8c9bcef88a8b36079ec14f125402b7f000a3a                                                                        16 docs/forensics/seed-data.csv
12 8
13 8
14 8
15 8
16 8
```
