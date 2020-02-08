# Rate-limit APIs

Your goal is to implement a simple web app which will serve HTTP requests and support rate limiting on them.

## Specs

### 1. Hi, me

Your application should expose a route with template `/greet/{name}` (where name is a route parameter), and it should respond to `GET` requests with status `200 OK` and body `Hi, {name}!`:

```bash
  curl http://localhost/greet/me
  Hi, me!
```

It's expected that this endpoint is rate limited. Rate limiting should be done by originating IP address, and limit should be set at `n` requests per `minute` (time window). For sake of simplicity, you can hardcode the requirement to `10` requests per minute.

### 2. Limiting

Following headers should be present on every `200 OK` response:

- `X-RateLimit-Limit` Number of allowed requests.
- `X-RateLimit-Remaining` Number of requests left for current minute (time window).

When done with `curl`, successful request should look like something like this:

```bash
~ curl http://localhost/greet/me -v
***
< HTTP/1.1 200 OK
< Content-Type: text/plain; charset=utf-8
< X-RateLimit-Limit: 10
< X-RateLimit-Remaining: 9
<

Hi, me!
```

### 3. Too Many Requests

When request limit is reached, your application should respond with [429 Too Many Requests][2d4db513]

```bash
~ curl http://localhost/greet/me -v
***
< HTTP/1.1 429 Too Many Requests
< Content-Type: text/plain; charset=utf-8
<
Rate limit exceeded.
```


## Delivery

You should deliver source code for your solution (on GitHub, if possible). Also, please provide Docker setup for your project so it could be run easily. 

## Notes

- If you're stuck, or need additional info - let us know.
- You can implement your solution in any language you see fit.
- You **may** not use existing framework provided rate-limiting solutions.

[2d4db513]: https://httpstatuses.com/429 "429 Too Many Requests"
