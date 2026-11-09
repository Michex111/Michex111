<div align="center">

<img src="assets/hero.svg" width="100%" alt="Chukwuebuka Madu — backend and systems engineer. I build the machinery behind the interface. Animated diagram of the Transform request path from agents and a React app through FastAPI, PostgreSQL and Redis Streams to workers and S3 storage." />

<br/>

<a href="https://github.com/Michex111"><img src="assets/links/github.svg" height="34" alt="GitHub: @Michex111" /></a>&nbsp;
<a href="https://transform-to.com"><img src="assets/links/transform.svg" height="34" alt="Transform live site: transform-to.com" /></a>&nbsp;
<a href="https://pypi.org/project/guardian-type-enforcer/"><img src="assets/links/pypi.svg" height="34" alt="Guardian on PyPI" /></a>&nbsp;
<img src="assets/links/location.svg" height="34" alt="Based in Charlottetown, Prince Edward Island" />

<br/>

**I like the parts of a system nobody notices until they break:**<br/>
queues, retries, auth boundaries, and the layer between a Python API and the machine underneath it.

</div>

<br/>

<img src="assets/sections/about.svg" alt="01 — About" />

I'm a software engineer based in Charlottetown, PEI. Most of my work is backend: services that take a request, hand the slow part to a worker, and report back honestly about what happened. I care most about the edges. What happens when a worker dies halfway through a job? What does a forged token look like compared with an expired one? What should the app do if production config is unsafe?

A few habits show up in everything I build:

- **I write the plan before the code.** Larger features start as a design doc and an audit of what already exists, and they say plainly what is not finished yet.
- **I keep the domain separate from the frameworks.** Business rules live in plain Python. Databases, queues, payment providers and LLMs connect through ports and adapters, so I can swap them out and test them with fakes.
- **I go down a layer when it's worth it.** When runtime type checking in pure Python cost too much, I wrote the hot path as a CPython C-extension.
- **I build software that AI agents can use.** That means real interfaces with real authorization (OAuth, scoped tools, the same service layer the REST API uses), not a chatbot bolted onto the side.

> **Right now:** building *cloud workspaces* for Transform, which are persistent Python environments that agents can drive through MCP. The rule behind them: the runtime is disposable, the workspace is not.

<br/>

<img src="assets/sections/stack.svg" alt="02 — Toolbox" />

<table>
  <tr>
    <td><b>Languages</b><br/><sub>Python · TypeScript · C · Java</sub></td>
    <td>
      <img src="assets/icons/python.svg" width="44" alt="Python" title="Python" />
      <img src="assets/icons/typescript.svg" width="44" alt="TypeScript" title="TypeScript" />
      <img src="assets/icons/c.svg" width="44" alt="C" title="C (CPython C-API)" />
      <img src="assets/icons/java.svg" width="44" alt="Java" title="Java" />
    </td>
  </tr>
  <tr>
    <td><b>Backend &amp; APIs</b><br/><sub>async services, auth, payments</sub></td>
    <td>
      <img src="assets/icons/fastapi.svg" width="44" alt="FastAPI" title="FastAPI" />
      <img src="assets/icons/pydantic.svg" width="44" alt="Pydantic" title="Pydantic" />
      <img src="assets/icons/sqlalchemy.svg" width="44" alt="SQLAlchemy" title="SQLAlchemy 2.0 (async)" />
      <img src="assets/icons/flask.svg" width="44" alt="Flask" title="Flask" />
      <img src="assets/icons/jwt.svg" width="44" alt="JSON Web Tokens" title="JWT auth" />
      <img src="assets/icons/stripe.svg" width="44" alt="Stripe" title="Stripe" />
    </td>
  </tr>
  <tr>
    <td><b>Data &amp; messaging</b><br/><sub>storage, streams, caching</sub></td>
    <td>
      <img src="assets/icons/postgresql.svg" width="44" alt="PostgreSQL" title="PostgreSQL" />
      <img src="assets/icons/redis.svg" width="44" alt="Redis" title="Redis (Streams, caching, rate limits)" />
      <img src="assets/icons/sqlite.svg" width="44" alt="SQLite" title="SQLite" />
      <img src="assets/icons/minio.svg" width="44" alt="MinIO" title="MinIO (S3-compatible, local)" />
      <img src="assets/icons/backblaze.svg" width="44" alt="Backblaze B2" title="Backblaze B2 (S3-compatible, production)" />
    </td>
  </tr>
  <tr>
    <td><b>AI &amp; agents</b><br/><sub>MCP servers, LLM APIs</sub></td>
    <td>
      <img src="assets/icons/mcp.svg" width="44" alt="Model Context Protocol" title="Model Context Protocol" />
      <img src="assets/icons/llm.svg" width="44" alt="LLM APIs" title="LLM APIs via OpenAI-compatible SDK (OpenAI, Groq)" />
    </td>
  </tr>
  <tr>
    <td><b>Frontend</b><br/><sub>typed SPAs</sub></td>
    <td>
      <img src="assets/icons/react.svg" width="44" alt="React" title="React" />
      <img src="assets/icons/vite.svg" width="44" alt="Vite" title="Vite" />
      <img src="assets/icons/tailwindcss.svg" width="44" alt="Tailwind CSS" title="Tailwind CSS" />
    </td>
  </tr>
  <tr>
    <td><b>Infra &amp; tooling</b><br/><sub>ship, test, observe</sub></td>
    <td>
      <img src="assets/icons/docker.svg" width="44" alt="Docker" title="Docker" />
      <img src="assets/icons/githubactions.svg" width="44" alt="GitHub Actions" title="GitHub Actions" />
      <img src="assets/icons/nginx.svg" width="44" alt="NGINX" title="NGINX" />
      <img src="assets/icons/render.svg" width="44" alt="Render" title="Render" />
      <img src="assets/icons/vercel.svg" width="44" alt="Vercel" title="Vercel" />
      <img src="assets/icons/prometheus.svg" width="44" alt="Prometheus" title="Prometheus metrics" />
      <img src="assets/icons/uv.svg" width="44" alt="uv" title="uv" />
      <img src="assets/icons/pytest.svg" width="44" alt="pytest" title="pytest" />
      <img src="assets/icons/vitest.svg" width="44" alt="Vitest" title="Vitest" />
    </td>
  </tr>
</table>

<br/>

<img src="assets/sections/projects.svg" alt="03 — Featured work" />

<a href="https://github.com/Michex111/transform"><img src="assets/projects/transform.svg" width="100%" alt="Transform — distributed file conversion with async workers, server-sent events and an MCP server. Built with FastAPI, PostgreSQL, Redis Streams, React and TypeScript, Docker." /></a>

A full file-conversion platform covering documents, images, audio, video, ebooks, fonts and archives. The API never does the heavy work. It validates the job, queues it, and streams progress back while separate workers do the conversion.

- **Layered with Domain-Driven Design:** `domain → application → infrastructure → presentation`, with 18 application ports. Queues, storage, payments, email, LLMs and container runtimes are all swappable adapters.
- **Reliable job processing:** Redis Streams consumer groups, retry with backoff, `XAUTOCLAIM` to recover messages stuck with a dead consumer, and a dead-letter stream for replaying failed jobs. Live progress reaches the browser over SSE.
- **Security built in from the start:** opt-in encryption at rest (chunked AES-256-GCM with per-user keys derived via HKDF), single-use verification tokens stored only as SHA-256 hashes, responses that don't reveal whether an account exists, and an app that refuses to boot with unsafe production config.
- **Usable by AI agents:** a remote MCP server with OAuth 2.1 + PKCE and dynamic client registration. It calls the *same* application services as the REST API, so no authorization rule is written twice.
- **Tested and gated:** 2,100+ pytest test functions, Vitest on the frontend, `pyrefly` type checking in CI, and deploys that only run after CI passes.

<sub>**Stack:** Python · FastAPI · SQLAlchemy 2 (async) · Alembic · PostgreSQL · Redis Streams · S3 (MinIO / Backblaze B2) · Stripe · React 18 · TypeScript · Vite · Tailwind · Docker · Prometheus</sub><br/>
**[Source →](https://github.com/Michex111/transform)** &nbsp;·&nbsp; **[Live →](https://transform-to.com)**

<br/>

<a href="https://github.com/Michex111/guardian-type-enforcer"><img src="assets/projects/guardian.svg" width="100%" alt="Guardian — runtime type enforcement and access control for Python, written as a CPython C-extension. Built with C, the CPython C-API, Python 3.11+, cibuildwheel and pytest." /></a>

Runtime type checking usually costs a lot because it runs in Python. Guardian moves the checks into C. Type hints are compiled once into an internal form, and every later assignment or call is checked natively.

- **Hooks into CPython's attribute protocol:** a custom `tp_setattro` on the `Shield` base type checks the type of every attribute assignment, with no proxy objects or `__dict__` wrapping.
- **Access control by walking stack frames:** private `_attributes` are protected by walking the caller's frames in C. Frame locals are read through the mapping protocol, so it also works with PEP 667's `FrameLocalsProxy` on Python 3.13+.
- **Feels like normal Python:** `@guard`, `@deepguard`, and a drop-in `dataclass` with `@validator` hooks and `dataclass_transform`, so IDEs and type checkers understand it.
- **Released properly:** tag-triggered CI runs the tests, then builds wheels with `cibuildwheel` for Linux, macOS (x86_64 + arm64) and Windows, including free-threaded CPython 3.14, and publishes them to PyPI. Includes a benchmark harness comparing it with Pydantic v2 and Beartype.

<sub>**Stack:** C · CPython C-API · Python · pytest · cibuildwheel · GitHub Actions</sub><br/>
**[Source →](https://github.com/Michex111/guardian-type-enforcer)** &nbsp;·&nbsp; **[PyPI →](https://pypi.org/project/guardian-type-enforcer/)** &nbsp;·&nbsp; `pip install guardian-type-enforcer`

<br/>

<a href="https://github.com/Michex111/terms-ai"><img src="assets/projects/terms-ai.svg" width="100%" alt="Terms Guardian — flags risky Terms-of-Service clauses with a schema-bound LLM. Built with FastAPI, Pydantic, Groq, slowapi and Vercel." /></a>

The analysis backend for a browser extension that highlights predatory clauses in Terms of Service and explains them in plain English. The interesting problem is making an LLM *behave like an API*.

- **Structured output:** the model is limited to a fixed set of clause types and risk indicators, with fixed scoring rules, and every response is validated against a Pydantic model.
- **Cheap and predictable:** documents are whitespace-normalised and hashed with SHA-256, so the same policy is never sent to the LLM twice within the cache window.
- **Fails safely:** if the model fails, the API still returns a schema-valid fallback, so the extension never breaks. Requests are rate-limited per IP and locked to the extension's origin.

<sub>**Stack:** Python · FastAPI · Pydantic · OpenAI-compatible SDK → Groq · slowapi · Vercel serverless</sub><br/>
**[Source →](https://github.com/Michex111/terms-ai)**

<br/>

<a href="https://github.com/Michex111/Pro-URL-shortner"><img src="assets/projects/url-shortener.svg" width="100%" alt="Pro URL Shortener — async FastAPI service with Base62 IDs and a Redis cache-aside layer. Built with FastAPI, async SQLAlchemy, PostgreSQL and Redis." /></a>

A small project with deliberate choices. Each short code is the Base62 encoding of the row's primary key, so codes can never collide and there are no random retries. Redirects go through a Redis cache-aside layer with a TTL, and submitting the same URL twice returns the existing code. It uses an async stack from the route down to the database session.

<sub>**Stack:** Python · FastAPI · async SQLAlchemy · PostgreSQL · Redis · Pydantic</sub><br/>
**[Source →](https://github.com/Michex111/Pro-URL-shortner)**

<br/>

<img src="assets/sections/activity.svg" alt="04 — Activity" />

<img src="assets/generated/stats.svg" width="100%" alt="GitHub activity card: original public repositories, commits in the last 12 months, stars, and language breakdown by bytes of code." />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/generated/snake-light.svg" />
  <img src="assets/generated/snake-dark.svg" width="100%" alt="Animated snake eating the squares of my GitHub contribution graph." />
</picture>

<br/>

<img src="assets/sections/connect.svg" alt="05 — Connect" />

<div align="center">

If you're working on backend infrastructure, developer tooling or agent-facing software, I'd like to hear about it.<br/>
Open an issue on any of my repos, or find me here:

<a href="https://github.com/Michex111"><img src="assets/links/github.svg" height="34" alt="GitHub: @Michex111" /></a>&nbsp;
<a href="https://pypi.org/project/guardian-type-enforcer/"><img src="assets/links/pypi.svg" height="34" alt="Guardian on PyPI" /></a>

<br/>

<sub>Every visual on this page is a self-hosted SVG in <a href="assets"><code>assets/</code></a>. The activity card and snake are regenerated daily by <a href=".github/workflows/profile-assets.yml">a GitHub Actions workflow</a>.</sub>

</div>
