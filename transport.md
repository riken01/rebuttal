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
