{
      "type": "cliDefinition",
      "name": "ohom Uninstall sub1 sub2", // 拼接好的cli子工具
      "version": "1.0.0", // 暂时预留
      "description": "ohos-bm bundle management CLI tool", // 子工具描述 
      "executeSide": "Device/Cloud", // 新增
      "requirePermissions": [], // 预留
      "inputSchema": { // 子工具输入
        "type": "object",
        "properties": {
          "help": { "type": "boolean", "default": false },
          "xxxx": { "type": "string"}
        }
      },
      "outputSchema": { // 子工具输出
        "type": "object",
        "properties": {
          "type": { "type": "string" },
          "status": { "type": "string" },
          "data": { "type": "object", "properties": {} }
        }
      }
    },
