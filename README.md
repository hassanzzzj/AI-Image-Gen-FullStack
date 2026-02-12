<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Image Generator - Project Documentation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #0f172a; color: #e2e8f0; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }
        code { background-color: #1e293b; color: #38bdf8; padding: 2px 6px; border-radius: 4px; font-family: 'Courier New', Courier, monospace; }
        pre { background-color: #000; padding: 15px; border-radius: 8px; overflow-x: auto; border: 1px solid #334155; }
    </style>
</head>
<body class="p-4 md:p-10">

    <div class="max-w-4xl mx-auto">
        <header class="text-center mb-12">
            <h1 class="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-600 mb-4">
                🎨 AI Image Generator
            </h1>
            <p class="text-xl text-slate-400">A Professional Streamlit & Dockerized Image Synthesis Tool</p>
            <div class="flex justify-center gap-4 mt-6">
                <span class="bg-blue-600/20 text-blue-400 px-3 py-1 rounded-full text-sm border border-blue-500/30">Python 3.9+</span>
                <span class="bg-green-600/20 text-green-400 px-3 py-1 rounded-full text-sm border border-green-500/30">Docker Ready</span>
                <span class="bg-purple-600/20 text-purple-400 px-3 py-1 rounded-full text-sm border border-purple-500/30">Free API</span>
            </div>
        </header>

        <section class="glass p-8 rounded-2xl mb-8">
            <h2 class="text-2xl font-bold mb-4 flex items-center gap-2">
                <i class="fas fa-rocket text-blue-500"></i> Project Overview
            </h2>
            <p class="text-slate-300 leading-relaxed">
                This project is a high-performance web application designed to generate high-quality AI images from textual descriptions. By integrating <strong>Streamlit</strong> for the frontend and <strong>Pollinations AI</strong> for backend inference, it provides a seamless, zero-cost solution for creators and developers.
            </p>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
                <i class="fas fa-layer-group text-purple-500"></i> Tech Stack
            </h2>
            <div class="overflow-hidden rounded-xl border border-slate-700">
                <table class="w-full text-left">
                    <thead class="bg-slate-800 text-slate-200">
                        <tr>
                            <th class="p-4">Technology</th>
                            <th class="p-4">Purpose</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-700 bg-slate-900/50">
                        <tr>
                            <td class="p-4 font-semibold text-blue-400">Streamlit</td>
                            <td class="p-4">Interactive UI & Reactive State Management</td>
                        </tr>
                        <tr>
                            <td class="p-4 font-semibold text-blue-400">Docker</td>
                            <td class="p-4">Containerization & Environment Consistency</td>
                        </tr>
                        <tr>
                            <td class="p-4 font-semibold text-blue-400">Pollinations AI</td>
                            <td class="p-4">Stable Diffusion based Image Generation</td>
                        </tr>
                        <tr>
                            <td class="p-4 font-semibold text-blue-400">Requests</td>
                            <td class="p-4">API Communication & Image Fetching</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <section class="glass p-8 rounded-2xl mb-8">
            <h2 class="text-2xl font-bold mb-4 flex items-center gap-2">
                <i class="fas fa-folder-open text-yellow-500"></i> Project Structure
            </h2>
            <pre><code>.
├── app.py              # Main Application Logic
├── requirements.txt    # Python Dependencies
├── Dockerfile          # Container Build Recipe
├── docker-compose.yml  # Orchestration File
└── .gitignore          # Version Control Filters</code></pre>
        </section>

        <section class="mb-8">
            <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
                <i class="fas fa-terminal text-green-500"></i> Setup & Installation
            </h2>
            
            <div class="space-y-6">
                <div>
                    <h3 class="text-lg font-semibold text-slate-200 mb-2">Method 1: Local Python Environment</h3>
                    <pre><code>pip install -r requirements.txt
streamlit run app.py</code></pre>
                </div>

                <div>
                    <h3 class="text-lg font-semibold text-slate-200 mb-2">Method 2: Docker (Best for Production)</h3>
                    <pre><code>docker-compose up --build</code></pre>
                    <p class="mt-2 text-sm text-slate-400 italic">Navigate to http://localhost:8501 in your browser.</p>
                </div>
            </div>
        </section>

        <section class="grid md:grid-cols-2 gap-6 mb-12">
            <div class="p-6 border border-slate-700 rounded-xl hover:border-blue-500 transition-colors">
                <i class="fas fa-bolt text-2xl text-blue-500 mb-3"></i>
                <h4 class="text-lg font-bold mb-2">Instant Generation</h4>
                <p class="text-sm text-slate-400">No waiting in queues. Get your AI art in seconds.</p>
            </div>
            <div class="p-6 border border-slate-700 rounded-xl hover:border-green-500 transition-colors">
                <i class="fas fa-dollar-sign text-2xl text-green-500 mb-3"></i>
                <h4 class="text-lg font-bold mb-2">100% Free</h4>
                <p class="text-sm text-slate-400">Unlimited generations without any subscription or tokens.</p>
            </div>
        </section>

        <footer class="text-center border-t border-slate-800 pt-8 mt-12">
            <p class="text-slate-500">Developed with ❤️ and Streamlit</p>
            <p class="text-xs text-slate-600 mt-2 uppercase tracking-widest">© 2026 Professional AI Portfolio</p>
        </footer>
    </div>

</body>
</html>