# done
1. 日期+时间，格式修改Y-m-d H:i，默认当前日期时间
2. 周期改为数字+单位，单位为列表
3. 编辑与新增都在行内编辑
4，表格中的元素居中显示
5. 数据按添加顺序倒序显示，最新添加数据在最前面
6. input框中的数据居中
7. 距离事件天数自动算(事件发生事件+周期-当天)，不需要用户输入和数据库获取，编辑和新增功能已实现
8. 修复距离事件天数字段列表页面显示问题
9. 项目统一默认东八区时区，修复前后端计算方法得到的距离事件天数不一样问题
10. 距离事件天数的计算公式修改为：当前日期-事件日期，与周期和具体时间无关。周期事件后续会更新事件时间，并且不记录首次事件时间。与具体时间无关更方便知道事件发生日期，做好准备。正值表示未来事件，负值表示过去事件。
11. 按照monitor服务进行修改字段和ui样式，表列名还未改。

# todo 
- 增加筛选条件
- 增加录入记录系统,如扫码开门,扫码挪车
- 距离事件天数自动计算，不需要用户输入和数据库获取，已发生为负数，未发生为正数，当天为0
- 类型字段改为从历史数据获取列表，也支持自定义编辑
- 支持多选框
- 多选记录分享功能，并添加标题，支持原数据分享和指定报表分享
- 周期事件更新事件时间



功能
- 记录操作
    - 新增单条记录
    - 编辑单条记录
    - 所有事件列表
- 记录分类
    - 一次性事件(过去/未来)
        - 事件类型
        - 事件信息
        - 事件发生时间
        - 距离事件天数(负数表示过去事件，正数表示未来事件)
    - 周期事件
        - 事件类型
        - 事件信息
        - 事件发生时间(未来事件)
        - 距离事件天数(一定是正数)
        - 周期
    - 与时间无关的事件(可以归类为一次性事件)
        - 事件类型
        - 事件信息
        - 创建记录时间
        - 已记录天数
- 分享记录

记录可以是固定程序、笔记、资源、提醒、交互响应。。。