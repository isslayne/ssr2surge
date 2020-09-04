# ssr2surge
## forked from https://github.com/WhoJave/ExternalConfig

#### 使用说明

- 项目中使用的python3路径为 `/usr/local/bin/python3`，请自行安装

- 生成配置的路径为`~/Documents/Surge/config`

- 请将ss-local文件复制到`~/Documents/Surge/config`目录下

- 请将v2rayCore相关文件复制到`~/Documents/Surge/config/v2raycore`

- `~/Documents/Surge/config/external.txt`Surge中可用的SSR External配置文件，如配置参考所示

- `~/Documents/Surge/config/v2rayExternal.txt`Surge中可用的V2RAY External配置文件，如配置参考所示

- 关于`ss-local（此处指的是SSR）`[ShadowsocksX-NG-R8](https://github.com/qinyuhang/ShadowsocksX-NG-R/releases)安装后在`~/Library/Application Support/ShadowsocksX-NG/ss-local-2.5.6.9.static`这个路径下可找到

- 参考:https://community.nssurge.com/d/3-external-proxy-provider 启动后可在`/tmp`路径看到log

- `v2ray`同理 这里 https://github.com/v2ray/v2ray-core/releases 下载使用

- Python脚本使用

  ```shell
  #进入项目中脚本文件夹
  cd ExternalConfig/ExternalConfig/script
  #执行如下脚本在指定目录生成配置
  python3 RSS.py -s `此外为你的SSR订阅地址` -p 端口号
  python3 v2json.py -s `此外为你的V2RAY订阅地址` -p 端口号
  #示例：
  script git:(master) ✗ python3 RSS.py -s https://www.xxxxxx.com -p 19522 
  script git:(master) ✗ python3 v2json.py -s https://www.xxxxxx.com -p 19829
  ```

#### 配置参考:

>- 示例：
>
>```json
>SSR东京2上海 = external, exec = "/Users/你的用户名/Documents/Surge/config/ss-local", local-port = 19522, args = "-c", args = "/Users/你的用户名/Documents/Surge/config/SSRJson/SSR东京2上海.json", addresses = "服务器IP"
>香港5v2ray = external, exec = "/Users/你的用户名/Documents/Surge/config/v2ray-core/v2ray", local-port = 19829, args = "--config=/Users/你的用户名/Documents/Surge/config/vmessJson/香港5v2ray.json", addresses = "服务器IP"
>```
>
>注意：上文配置中 `local-port`要与下文json配置中的`local-port`保持一致
>
>- SSR东京2上海.json
>
>```json
>{
>"local_address" : "127.0.0.1",
>"local_port" : 19522,
>"server" : "服务器地址",
>"server_port" : 8888,
>"method" : "aes-256-cfb",
>"protocol" : "auth_chain_a",
>"protocol_param" : "",
>"timeout" : 60,
>"obfs" : "tls1.2_ticket_auth",
>"obfs_param" : "cloudflare.com",
>"password" : "你的密码"
>}
>```
