# 4 steps to excute this project :whale::
- :smile:首先准备好neo4j的安装，启动如下：
输入 ``neo4j.bat console``
<image src="images/01_neo4j.png">
启动后界面如下：
<image src="images/02_neo4j_browse.png">

- :smile:启动前端
输入 ``cd frontend``
``yarn``
``yarn run dev``
<image src="images/03_frontend.png">
使用浏览器访问 `` http://localhost:5173/``
界面如下：
<image src="images/05_final_browse1.png">

- :smile:启动后端
输入 ``cd backend``
配置环境，安装依赖 ``pip install -r requirements.txt``
激活环境，启动项目 ``python score.py``
<image src="images/04_backend.png">

- :smile:进入浏览器界面，进行后端的连接
<image src="images/05_final_browse1.png">
输入neo4j的登陆密码
<image src="images/06_final_browse2.png">
启动成功，界面如下
<image src="images/07_final_browse3.png">

- Some Tips:
```bash
接来就是导入文件，利用大模型生成知识图谱，并结合右边机器人进行问答。
大模型支持 ollama 本地部署和调用其他大模型API，记得在 backend 文件夹下.env文件填入你的api。
如果要在列表中添加新的大模型，请在 frontend 文件下.env文件也进行相应的添加。
```