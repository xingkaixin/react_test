# Reason and Action 模式

1. Client -> Question:
   **What is the result of dividing mckaywrigley’s GitHub followers by 2?**

2. ChatGPT -> Answer

   **Thought**: `我需要使用GithubUserInfoTool来获取mckaywrigley的粉丝数，然后将其除以2。`

   **Action**: `使用GithubUserInfoTool。`

   **Action Input**: `mckaywrigley`

 3. Tool ->  Observation -> ChatGPT

    **Observation**: 

    ```json
    {
    "login": "mckaywrigley",
    "id": 29221284,
    "node_id": "MDQ6VXNlcjI5MjIxMjg0",
    "avatar_url": "https://avatars.githubusercontent.com/u/29221284?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/mckaywrigley",
    "html_url": "https://github.com/mckaywrigley",
    "followers_url": "https://api.github.com/users/mckaywrigley/followers",
    "following_url": "https://api.github.com/users/mckaywrigley/following{/other_user}",
    "gists_url": "https://api.github.com/users/mckaywrigley/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/mckaywrigley/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/mckaywrigley/subscriptions",
    "organizations_url": "https://api.github.com/users/mckaywrigley/orgs",
    "repos_url": "https://api.github.com/users/mckaywrigley/repos",
    "events_url": "https://api.github.com/users/mckaywrigley/events{/privacy}",
    "received_events_url": "https://api.github.com/users/mckaywrigley/received_events",
    "type": "User",
    "site_admin": false,
    "name": "Mckay Wrigley",
    "company": null,
    "blog": "mckaywrigley.com",
    "location": null,
    "email": null,
    "hireable": null,
    "bio": "Building AI devtools (Codewand AI), open source AI chat (Chatbot UI), & other experiments.",
    "twitter_username": "mckaywrigley",
    "public_repos": 11,
    "public_gists": 0,
    "followers": 1939,
    "following": 2,
    "created_at": "2017-06-06T05:16:41Z",
    "updated_at": "2023-04-11T03:05:42Z"
    }
    ```

4. ChatGPT -> Answer:

   **Thought**: `现在我知道了mckaywrigley的粉丝数，我需要将其除以2。`

   **Action**: `使用CalculatorTool。`

   **Action Input**: `1939 / 2`

5. Tool -> Observation -> ChatGPT
   **Observation**: `969.5`

6. ChatGPT -> Answer

   **Thought**: `我已经计算出了mckaywrigley的GitHub粉丝数除以2的结果。`

   Final Answer: `969.5`

