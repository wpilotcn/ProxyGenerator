# H͜͡E͜͡L͜͡L͜͡O͜͡ W͜͡O͜͡R͜͡L͜͡D͜͡ E͜͡X͜͡T͜͡R͜͡A͜͡C͜͡T͜͡ P͜͡R͜͡O͜͡X͜͡Y͜͡ N͜͡O͜͡D͜͡E͜͡

𓆝 𓆟 𓆞 𓆟 𓆝 𓆟 𓆞 𓆟 𓆝𓆝 𓆟𓆝 𓆟 𓆟 𓆞 𓆟  
**Author:** wpilot  
**Date:** 2024-10-26  
**Version:** 1.2  
𓆝 𓆟 𓆞 𓆟 𓆝 𓆟 𓆞 𓆟 𓆝 𓆟𓆝 𓆟𓆝 𓆟 𓆞 𓆟  
# Key Changes Made to the Code

## Restructured Routes
- Restructured the routes into groups of URLs, where each group contains the same config with different sources.

## Added Failover Logic
- Added a `try_get_config` function that implements the failover logic:
  - Tries each URL in sequence.
  - Returns the first successful response.
  - Returns `None` if all URLs fail.

## Simplified Output Format
- Removed Chinese characters.
- Changed "线路一" etc. to simple "Route" labels.
- Kept the structure clean and minimal.

## Improved Error Handling
- Improved error handling to handle complete group failures.
- Added UTF-8 encoding specification when writing the file.

## Summary
The code will now try each backup URL in sequence if the primary URL fails, and will only output English text in the results file.
⠀⠀  
免责声明:
本项目为个人学习测试使用，禁止其他用途，非必要不 fork，可以给个小星星 (star)。

任何单位或个人认为通过本产品提供的软件可能涉嫌侵犯其合法权益，应该及时向作者书面反馈，并提供身份证明、权属证明及详细侵权情况证明，作者在收到上述法律文件后，将会尽快移除被控侵权软件。

如若侵犯了您的权益，请及时通过邮箱（wpilotcn@Gmail.com）联系作者，作者会第一时间关闭仓库。
