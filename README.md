<!DOCTYPE html>
<html>
<body>

<div align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-orange?style=for-the-badge" />
  <br />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />

  <h1 align="center" style="font-size: 3rem; color: #38bdf8;">🚀 AI Image Studio Pro</h1>
  <p align="center" style="font-size: 1.2rem;">
    <i>Transforming text into art using <b>Microservices Architecture</b> and <b>Generative AI</b>.</i>
  </p>
</div>

<hr style="border: 2px solid #334155;" />

<h2>📖 Project Introduction</h2>
<p>
  This project is a high-performance <b>Full-Stack Generative AI Application</b> developed as a core deliverable for the <b>Week 4 DevOps & Containerization Task</b>. 
  It utilizes a decoupled architecture where the frontend and backend operate in isolated environments, communicating through a virtualized bridge network.
</p>



<h2>🛠️ Core Features</h2>
<ul>
  <li><b>Real-time Image Synthesis:</b> Connects to Hugging Face's <code>FLUX.1-schnell</code> model for ultra-fast generation.</li>
  <li><b>Container Orchestration:</b> Fully managed via Docker Compose for easy scaling.</li>
  <li><b>Asynchronous Processing:</b> Backend handles heavy AI requests without blocking the event loop.</li>
  <li><b>Dark Mode UI:</b> A modern, sleek React interface optimized for developer experience.</li>
  <li><b>Robust Error Handling:</b> Advanced retry logic for API timeouts and 404 router redirects.</li>
</ul>

<h2>🏗️ System Architecture & DevOps Flow</h2>
<p>
  The application follows the <b>Modern DevOps Lifecycle</b>. By using Docker, we eliminate the "works on my machine" problem, providing a consistent environment across Development, Staging, and Production.
</p>



<table width="100%">
  <tr style="background-color: #1e293b; color: white;">
    <th width="30%">Layer</th>
    <th width="70%">Technology & Practice Used</th>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td>React.js (Functional Components, Hooks, Axios)</td>
  </tr>
  <tr>
    <td><b>Backend API</b></td>
    <td>FastAPI (Uvicorn ASGI, Pydantic Schema, CORS Middleware)</td>
  </tr>
  <tr>
    <td><b>Containerization</b></td>
    <td>Docker (Multistage builds, .dockerignore optimization)</td>
  </tr>
  <tr>
    <td><b>Orchestration</b></td>
    <td>Docker Compose (Services, Networks, Volumes)</td>
  </tr>
  <tr>
    <td><b>Environment</b></td>
    <td>Abstraction via <code>.env</code> files for API Security</td>
  </tr>
</table>

<h2>🚀 Installation & Setup Guide</h2>

<h3>1. Clone the Repository</h3>
<pre style="background: #0f172a; color: #38bdf8; padding: 15px; border-radius: 8px;">
git clone https://github.com/hassanzzzj/AI-Image-Gen-FullStack.git
cd AI-Image-Gen-FullStack
</pre>

<h3>2. Configure API Keys</h3>
<p>Navigate to the <code>backend/</code> folder and create a <code>.env</code> file:</p>
<pre style="background: #0f172a; color: #38bdf8; padding: 15px; border-radius: 8px;">
HUGGING_FACE_TOKEN=your_token_starts_with_hf_
</pre>

<h3>3. Launch with Docker Compose</h3>
<p>Build and start all services with a single command:</p>
<pre style="background: #0f172a; color: #38bdf8; padding: 15px; border-radius: 8px;">
docker-compose up --build
</pre>
<p>Once the logs show <i>"Application startup complete"</i>, visit <b>http://localhost:3000</b>.</p>

<h2>🔍 Troubleshooting & Debugging</h2>
<ul>
  <li><b>Error 404 (Hugging Face):</b> Check the <code>API_URL</code> in <code>main.py</code>. We use the latest <code>router.huggingface.co</code> endpoint.</li>
  <li><b>Container Connectivity:</b> Ensure no other service is using ports 3000 or 8000.</li>
  <li><b>Docker Cache Issues:</b> Run <code>docker system prune -f</code> to clear old build caches.</li>
</ul>

<hr style="border: 1px solid #334155;" />

<div align="center">
  <h3>👨‍💻 Developer Notes</h3>
  <p>
    This project demonstrates the successful implementation of <b>CI/CD ready containerization</b>. 
    By decoupling the frontend from the backend, we achieve <b>High Availability</b> and <b>Fault Tolerance</b>.
  </p>
  <p><b>Created by Hassan </b></p>
</div>

</body>
</html>