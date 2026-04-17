1. 添加call_device_tool、get_note_tool_schema工具，并添加到channel.js中
2. channel.js中删除create_note、search_notes、modify_note工具

3. name: "call_device_tool",
description: "端工具调用。必须先调用`get_xxx_tool_schema`获取了具体的工具schema，才能使用本工具执行对应端工具。",
parameters: {
    type: "object",
    properties: {
        toolName: {
            type: "string",
            description: "要调用的具体端工具名称，即`get_xxx_tool_schema`返回的工具的name",
        },
        arguments: {
            type: "object",
            description: "工具所需的具体参数JSON键值对",
        },
    },
    required: ["toolName", "arguments"],
}

【工具返回】
1. 如果匹配到对应的工具，则执行对应工具的execute方法并返回结果
2. 如果没有匹配到工具名，则返回"端工具{toolName}不存在。请确保toolName为`get_xxx_tool_schema`返回的工具的name。"
3. 如果匹配到工具名但参数错误，则返回"端工具参数错误：{具体错误信息}。请确保arguments符合`get_xxx_tool_schema`返回的工具schema。"

4. name: "get_note_tool_schema",
description: "获取可在用户设备上创建、搜索、追加备忘录的相关端工具列表。",
parameters: {
    type: "object",
    properties: { },
}

【工具返回】
以下为工具列表。请仔细阅读，使用`call_device_tool`进行调用：
{"name":"create_note","description":"在用户设备上创建备忘录。需要提供备忘录标题和内容。
  注意:
  a. 操作超时时间为60秒,请勿重复调用此工具
  b. 如果遇到各类调用失败场景,最多只能重试一次，不可以重复调用多次。
  c. 调用工具前需认真检查调用参数是否满足工具要求

  回复约束：如果工具返回没有授权或者其他报错，只需要完整描述没有授权或者其他报错内容即可，不需要主动给用户提供解决方案，例如告诉用户如何授权，如何解决报错等都是不需要的，请严格遵守。
  ","parameters":{"properties":{"title":{"type":"string","description":"备忘录标题，必填"},"content":{"type":"string","description":"备忘录内容，必填"}},"required":["title","content"],"type":"object"}}
{"name":"search_notes","description":"搜索用户设备上的备忘录内容。根据关键词在备忘录的标题、内容和附件名称中进行检索。注意:操作超时时间为60秒,请勿重复调用此工具,如果超时或失败,最多重试一次。回复约束：如果工具返回没有授权或者其他报错，只需要完整描述没有授权或者其他报错内容即可，不需要主动给用户提供解决方案，例如告诉用户如何授权，如何解决报错等都是不需要的，请严格遵守。","parameters":{"properties":{"query":{"type":"string","description":"搜索关键词，用于在备忘录中检索相关内容"}},"required":["query"],"type":"object"}}
{"name":"modify_note","description":"在指定备忘录中追加新内容。使用前必须先调用 search_notes 工具获取备忘录的 entityId。参数说明：entityId 是备忘录的唯一标识符（从 search_notes 工具获取），text 是要追加的文本内容。注意:操作超时时间为60秒,请勿重复调用此工具,如果超时或失败,最多重试一次。回复约束：如果工具返回没有授权或者其他报错，只需要完整描述没有授权或者其他报错内容即可，不需要主动给用户提供解决方案，例如告诉用户如何授权，如何解决报错等都是不需要的，请严格遵守。","parameters":{"properties":{"entityId":{"type":"string","description":"备忘录的唯一标识符，必须先通过 search_notes 工具获取"},"text":{"type":"string","description":"要追加到备忘录的文本内容"}},"required":["entityId","text"],"type":"object"}}

{"type":"message","id":"be137b64","parentId":"aef7f1ef","timestamp":"2026-04-17T02:39:42.258Z","message":{"role":"user","content":[{"type":"text","text":"Conversation info (untrusted metadata):\n```json\n{\n  \"message_id\": \"7ad7c419-40b5-4ab6-ae48-f40791d53c63&42&87fa&0\",\n  \"sender_id\": \"106c68843fde421e8a0ee185a674b916\",\n  \"sender\": \"106c68843fde421e8a0ee185a674b916\",\n  \"timestamp\": \"Fri 2026-04-17 10:39 GMT+8\"\n}\n```\n\nSender (untrusted metadata):\n```json\n{\n  \"label\": \"106c68843fde421e8a0ee185a674b916\",\n  \"id\": \"106c68843fde421e8a0ee185a674b916\",\n  \"name\": \"106c68843fde421e8a0ee185a674b916\"\n}\n```\n\nhttps://feeds-drcn.cloud.huawei.com.cn/landingpage/media?docid=105113613932262218853032&to_app=hwbrowser&dy_scenario=push&tn=3a8d67e662d9be80d6e63e0d343121886e0b337e47d4c97f7a74b670bf7cbe60&ctype=video_live&cpid=666&r=CN&pageType=2&share_to=link 收藏这个"}],"timestamp":1776393582219}}
{"type":"message","id":"72fca9ba","parentId":"be137b64","timestamp":"2026-04-17T02:39:48.682Z","message":{"role":"assistant","content":[{"type":"toolCall","id":"call_6156398fb4dc476a899e949d1366f819","name":"call_device_tool","arguments":{"toolName":"add_collection","arguments":{"dataType":"HYPER_LINK","content":"https://feeds-drcn.cloud.huawei.com.cn/landingpage/media?docid=105113613932262218853032&to_app=hwbrowser&dy_scenario=push&tn=3a8d67e662d9be80d6e63e0d343121886e0b337e47d4c97f7a74b670bf7cbe60&ctype=video_live&cpid=666&r=CN&pageType=2&share_to=link"}}}],"api":"openai-completions","provider":"xiaoyiprovider","model":"LLM_GLM5.1","usage":{"input":44608,"output":145,"cacheRead":0,"cacheWrite":0,"totalTokens":44753,"cost":{"input":0.000044608000000000004,"output":2.9000000000000003e-7,"cacheRead":0,"cacheWrite":0,"total":0.000044898}},"stopReason":"stop","timestamp":1776393582258,"responseId":"7ad7c419-40b5-4ab6-ae48-f40791d53c63&42&87fa&0"}}
{"type":"message","id":"86e52c58","parentId":"72fca9ba","timestamp":"2026-04-17T02:39:48.968Z","message":{"role":"toolResult","toolCallId":"call_6156398fb4dc476a899e949d1366f819","toolName":"call_device_tool","content":[{"type":"text","text":"{\"errMsg\":\"intent invalid error\",\"retErrCode\":\"-304\"}"}],"isError":false,"timestamp":1776393588965}}
{"type":"message","id":"03449709","parentId":"86e52c58","timestamp":"2026-04-17T02:39:51.845Z","message":{"role":"assistant","content":[{"type":"text","text":"收藏链接时出现错误：intent invalid error（错误码：-304）\n\n小艺收藏功能目前可能存在限制或需要特定条件才能使用。建议您稍后再试，或者通过手机端的小艺收藏功能手动添加。"}],"api":"openai-completions","provider":"xiaoyiprovider","model":"LLM_GLM5.1","usage":{"input":44771,"output":49,"cacheRead":0,"cacheWrite":0,"totalTokens":44820,"cost":{"input":0.000044771,"output":9.8e-8,"cacheRead":0,"cacheWrite":0,"total":0.000044869}},"stopReason":"stop","timestamp":1776393588971,"responseId":"7ad7c419-40b5-4ab6-ae48-f40791d53c63&42&87fa&0"}}
{"type":"custom","customType":"openclaw.cache-ttl","data":{"timestamp":1776393591893,"provider":"xiaoyiprovider","modelId":"LLM_GLM5.1"},"id":"5343e1d7","parentId":"03449709","timestamp":"2026-04-17T02:39:51.893Z"}
