<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Code Studio</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg viewBox='-10 -10 120 120' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cdefs%3E%3ClinearGradient id='fGrad' x1='0%25' y1='0%25' x2='100%25' y2='100%25'%3E%3Cstop offset='0%25' style='stop-color:%2360a5fa' /%3E%3Cstop offset='100%25' style='stop-color:%23a855f7' /%3E%3C/linearGradient%3E%3C/defs%3E%3Ccircle cx='50' cy='50' r='48' stroke='url(%23fGrad)' stroke-width='10' /%3E%3Cpath d='M30 35L12 50L30 65M70 35L88 50L70 65' stroke='url(%23fGrad)' stroke-width='12' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M58 25L42 75' stroke='url(%23fGrad)' stroke-width='12' stroke-linecap='round'/%3E%3C/svg%3E">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/theme/dracula.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/addon/dialog/dialog.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    
    <style>
        /* =========================================
           1. VARIABLES (O'ZGARUVCHILAR)
        ========================================= */
        :root {
            --bg-main: #030712;
            --bg-glass: rgba(17, 24, 39, 0.7);
            --bg-glass-light: rgba(255, 255, 255, 0.05);
            --border-glass: rgba(255, 255, 255, 0.1);
            
            --color-primary: #3b82f6;
            --color-primary-hover: #2563eb;
            --color-primary-glow: rgba(59, 130, 246, 0.4);
            --color-danger: #ef4444;
            --color-danger-bg: rgba(239, 68, 68, 0.1);
            
            --color-ai: #a855f7; /* AI uchun maxsus rang */
            
            --text-main: #f3f4f6;
            --text-dim: #9ca3af;
            
            --blur: blur(20px);
            --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            
            --z-base: 10;
            --z-dialog: 100;
            --z-header: 1000;
            --z-ai: 1500; /* AI yordamchisi ustunligi */
            --z-nav: 2000;
            --z-modal: 10000;
            --z-splash: 100000;
        }

        /* =========================================
           2. BASE & RESET
        ========================================= */
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        
        html, body { 
            height: 100%; overflow: hidden; 
            font-family: 'Inter', sans-serif; 
            background: var(--bg-main); color: var(--text-main); 
        }

        body::before {
            content: ''; position: fixed; inset: 0;
            background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, var(--bg-main) 100%);
            z-index: -2;
        }

        /* Maxsus Scrollbar */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.2); border-radius: 4px; }
        ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--color-primary); }

        :focus:not(:focus-visible) { outline: none; }
        :focus-visible { outline: 2px solid var(--color-primary); outline-offset: 2px; }

        svg { width: 1.25rem; height: 1.25rem; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

        /* =========================================
           3. UI COMPONENTS
        ========================================= */
        .text-gradient {
            background: linear-gradient(90deg, #60a5fa, #a855f7);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }

        .btn {
            display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
            padding: 0.5rem 1rem; border-radius: 0.5rem; border: 1px solid var(--border-glass);
            background: var(--bg-glass-light); color: var(--text-main);
            font-size: 0.75rem; font-weight: 600; cursor: pointer;
            transition: all var(--transition);
        }
        .btn:hover { background: rgba(255, 255, 255, 0.1); transform: translateY(-1px); }
        .btn:active { transform: scale(0.95); }
        .btn--icon { padding: 0.5rem; }
        
        .btn--primary { background: var(--color-primary); border: none; box-shadow: 0 4px 15px var(--color-primary-glow); }
        .btn--primary:hover { background: var(--color-primary-hover); box-shadow: 0 6px 20px var(--color-primary-glow); }
        
        .btn--danger { color: var(--color-danger); border-color: var(--color-danger-bg); }
        .btn--danger:hover { background: var(--color-danger-bg); }

        .btn--full { width: 100%; margin-block-start: 1rem; }

        .input-field {
            width: 100%; padding: 0.75rem 1rem; margin-block: 0.5rem;
            background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-main); border-radius: 0.5rem; outline: none; transition: all var(--transition);
        }
        .input-field:focus { border-color: var(--color-primary); background: rgba(0, 0, 0, 0.5); box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2); }
        select.input-field option { background: #111827; color: var(--text-main); }

        .panel {
            background: var(--bg-glass); backdrop-filter: var(--blur);
            border: 1px solid var(--border-glass); border-radius: 1rem;
            display: flex; flex-direction: column; overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }

        .panel__header {
            padding: 0.75rem 1rem; background: rgba(0,0,0,0.2);
            font-size: 0.65rem; font-weight: 800; letter-spacing: 1px;
            color: var(--text-dim); text-transform: uppercase;
            display: flex; align-items: center; justify-content: space-between;
            border-bottom: 1px solid var(--border-glass);
        }

        /* =========================================
           4. LAYOUT & SCREENS
        ========================================= */
        #splash-screen {
            z-index: var(--z-splash); background: var(--bg-main); 
            display: flex; flex-direction: column; align-items: center; justify-content: center;
        }
        .splash-logo-main { width: clamp(120px, 20vw, 250px); height: auto; filter: drop-shadow(0 0 20px var(--color-primary-glow)); }
        @keyframes pulse { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.05); opacity: 0.8; } }
        .animate-pulse { animation: pulse 2s infinite ease-in-out; }
        
        .overlay {
            position: fixed; inset: 0; display: flex; justify-content: center; align-items: center;
            z-index: var(--z-modal); 
            background: rgba(0, 0, 0, 0.4); 
            backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px);
            transition: opacity 0.4s ease, visibility 0.4s ease;
        }
        .overlay.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
        
        .modal-box { 
            background: rgba(255, 255, 255, 0.05); 
            backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
            padding: 2.5rem; border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.1); 
            box-shadow: 0 10px 30px rgba(0,0,0,0.5); width: 90%; max-width: 380px; text-align: center; 
        }
        
        .spinner { animation: spin 1s linear infinite; display: none; width: 1rem; height: 1rem; }
        @keyframes spin { 100% { transform: rotate(360deg); } }

        .header {
            height: 60px; background: rgba(17, 24, 39, 0.6); backdrop-filter: var(--blur);
            border-bottom: 1px solid var(--border-glass); padding: 0 1.25rem;
            display: flex; justify-content: space-between; align-items: center; z-index: var(--z-header); position: relative;
        }
        .header__logo { display: flex; align-items: center; gap: 0.75rem; font-size: 1.2rem; font-weight: 800; }
        .header__logo-container { display: flex; align-items: center; justify-content: center; cursor: pointer; transition: transform var(--transition); }
        .header__logo-container:hover { transform: rotate(10deg) scale(1.1); }
        .header__logo-container svg { width: 35px; height: 35px; }
        .header__actions { display: flex; gap: 0.5rem; }

        .workspace { position: relative; height: calc(100% - 120px); display: block; padding: 0; }
        .workspace__panel { position: absolute; inset: 0; width: 100%; height: 100%; border-radius: 0; border: none; opacity: 0; pointer-events: none; transition: opacity var(--transition); }
        .workspace__panel.active-view { opacity: 1; pointer-events: auto; z-index: var(--z-base); display: flex; }
        iframe { flex: 1; border: none; background: #fff; border-radius: 0 0 1rem 1rem; width: 100%; height: 100%; }
        
        .resizer { display: none; }

        .mobile-nav {
            position: fixed; bottom: 0; inset-inline: 0; height: 60px;
            background: rgba(17, 24, 39, 0.8); backdrop-filter: var(--blur); border-top: 1px solid var(--border-glass);
            display: flex; justify-content: space-around; align-items: center; z-index: var(--z-nav);
        }
        .nav-item { display: flex; flex-direction: column; align-items: center; gap: 0.25rem; color: var(--text-dim); cursor: pointer; transition: color var(--transition); }
        .nav-item.active { color: var(--color-primary); }
        .nav-item span { font-size: 0.6rem; font-weight: bold; text-transform: uppercase; }

        .tab-system { display: flex; background: rgba(0,0,0,0.4); margin: 0.75rem; border-radius: 0.5rem; padding: 0.25rem; }
        .tab-btn { flex: 1; padding: 0.5rem; border: none; background: transparent; color: var(--text-dim); cursor: pointer; font-size: 0.65rem; font-weight: 700; border-radius: 0.4rem; transition: all var(--transition); }
        .tab-btn.active { background: var(--color-primary); color: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }
        
        .list-container { flex: 1; overflow-y: auto; padding: 0.75rem; display: flex; flex-direction: column; gap: 0.6rem; }
        .card { 
            padding: 1rem; background: rgba(255,255,255,0.03); border-radius: 0.75rem; 
            border: 1px solid rgba(255,255,255,0.05); cursor: pointer; 
            display: flex; justify-content: space-between; align-items: center; 
            transition: all var(--transition); 
        }
        .card:hover { border-color: var(--color-primary); background: rgba(255,255,255,0.08); transform: translateY(-2px); }
        .card__info { display: flex; flex-direction: column; gap: 0.2rem;}
        .card__title { color: var(--color-primary); font-size: 0.9rem; font-weight: 600; }
        
        .delete-btn { background: none; border: none; cursor: pointer; padding: 0.4rem; opacity: 0.6; transition: var(--transition); color: var(--color-danger); border-radius: 50%; }
        .delete-btn:hover { opacity: 1; background: var(--color-danger-bg); transform: scale(1.1); }

        .CodeMirror { height: 100% !important; flex: 1; font-size: 15px; background: transparent !important; }
        .CodeMirror-dialog { background: rgba(17, 24, 39, 0.95) !important; color: #fff !important; padding: 0.75rem !important; border-radius: 0.75rem !important; border: 1px solid var(--color-primary); box-shadow: 0 10px 30px rgba(0,0,0,0.5); position: absolute; top: 10px; right: 10px; z-index: var(--z-dialog); }
        .CodeMirror-dialog input { background: rgba(0,0,0,0.5); border: 1px solid var(--border-glass); color: #fff; padding: 0.4rem 0.8rem; border-radius: 0.4rem; outline: none; margin-inline: 0.5rem; }
        .CodeMirror-dialog button { background: var(--border-glass); border: none; color: #fff; padding: 0.4rem 0.8rem; border-radius: 0.4rem; cursor: pointer; font-size: 0.75rem; transition: 0.2s;}
        .CodeMirror-dialog button:hover { background: var(--color-primary); }

        .desktop-only { display: none; }
        
        @media (min-width: 900px) {
            .desktop-only { display: inline-flex !important; }
            .mobile-nav { display: none; }
            
            .workspace { height: calc(100% - 60px); display: flex; padding: 0.75rem; gap: 0; }
            
            .workspace__panel { position: relative; border-radius: 1rem; border: 1px solid var(--border-glass); opacity: 1; pointer-events: auto; transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s; }
            
            #view-files { width: 0; opacity: 0; pointer-events: none; border: none; margin-right: 0; }
            #view-files.open { width: 300px; opacity: 1; pointer-events: auto; border: 1px solid var(--border-glass); margin-right: 0.75rem; flex-shrink: 0; }
            #view-files > div { min-width: 300px; }
            #editor-container { width: 50%; flex: none; }
            #preview-container { flex: 1; min-width: 0; }
            
            .resizer { display: flex; width: 16px; cursor: col-resize; justify-content: center; align-items: center; z-index: var(--z-base); user-select: none; }
            .resizer::after { content: ''; width: 4px; height: 40px; border-radius: 2px; background: rgba(255, 255, 255, 0.15); transition: background var(--transition), height 0.3s; }
            .resizer:hover::after, .resizer.active::after { background: var(--color-primary); height: 60px; box-shadow: 0 0 10px var(--color-primary-glow); }
            body.resizing { user-select: none; cursor: col-resize; }
        }

        /* =========================================
           ✨ YASHRIN AI DRAWER (O'NG TOMONDAN)
        ========================================= */
        #ai-drawer {
            position: fixed; top: 60px; right: -500px; /* Yashirin */
            width: 450px; height: calc(100% - 60px);
            background: rgba(15, 23, 42, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border-left: 1px solid var(--color-ai);
            z-index: var(--z-ai); 
            transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex; flex-direction: column;
            box-shadow: -10px 0 40px rgba(0,0,0,0.6);
        }
        #ai-drawer.open { right: 0; }
        
        .ai-header { 
            padding: 15px 20px; background: rgba(0,0,0,0.4); 
            border-bottom: 1px solid var(--border-glass); 
            display: flex; justify-content: space-between; align-items: center;
        }
        .ai-title { font-weight: 800; color: #e9d5ff; display: flex; align-items: center; gap: 10px; font-size: 1rem;}
        .close-ai { background: none; border: none; color: var(--text-dim); cursor: pointer; transition: 0.3s;}
        .close-ai:hover { color: #fff; transform: scale(1.1);}

        #ai-chat-box { 
            flex: 1; overflow-y: auto; padding: 20px; 
            display: flex; flex-direction: column; gap: 15px; font-size: 0.95rem; 
        }
        .chat-bubble { 
            max-width: 85%; padding: 14px 18px; border-radius: 12px; 
            line-height: 1.6; white-space: pre-wrap; font-family: 'Inter', sans-serif;
        }
        .bubble-user { align-self: flex-end; background: var(--color-primary); color: white; border-bottom-right-radius: 4px;}
        .bubble-ai { align-self: flex-start; background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.3); color: #f3f4f6; border-bottom-left-radius: 4px;}
        
        /* GEMINI TYPING EFFECT KURSORI */
        .typing-cursor::after { 
            content: '▋'; animation: blink 1s step-start infinite; 
            color: var(--color-ai); margin-left: 4px; 
        }
        @keyframes blink { 50% { opacity: 0; } }

        .ai-input-area { 
            padding: 20px; border-top: 1px solid var(--border-glass); 
            background: rgba(0,0,0,0.5); display: flex; flex-direction: column; gap: 12px;
        }
        .ai-input-wrapper { display: flex; gap: 10px; }
        .ai-input-wrapper input { 
            flex: 1; padding: 14px; border-radius: 8px; border: 1px solid var(--border-glass); 
            background: rgba(255,255,255,0.05); color: white; outline: none; font-size: 0.95rem;
        }
        .ai-input-wrapper button { 
            padding: 0 20px; background: linear-gradient(90deg, #60a5fa, #a855f7); 
            color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; 
        }
        .btn-full-analyze { 
            width: 100%; padding: 12px; background: rgba(168, 85, 247, 0.2); 
            border: 1px solid var(--color-ai); color: #e9d5ff; border-radius: 8px; 
            cursor: pointer; font-weight: 600; transition: 0.3s;
        }
        .btn-full-analyze:hover { background: var(--color-ai); color: white; box-shadow: 0 0 15px rgba(168, 85, 247, 0.4);}

        @media (max-width: 900px) {
            #ai-drawer { width: 100%; right: -100%; }
        }
    </style>
</head>
<body>

<div id="splash-screen" class="overlay">
    <svg class="animate-pulse splash-logo-main" viewBox="-10 -10 120 120" fill="none">
        <defs>
            <linearGradient id="codeGradSplash" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#60a5fa" /><stop offset="100%" style="stop-color:#a855f7" />
            </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="48" stroke="url(#codeGradSplash)" stroke-width="10" />
        <path d="M35 35L20 50L35 65" stroke="url(#codeGradSplash)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M65 35L80 50L65 65" stroke="url(#codeGradSplash)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M55 30L45 70" stroke="url(#codeGradSplash)" stroke-width="7" stroke-linecap="round"/>
    </svg>
    <div class="text-gradient" style="font-size:2.2rem; font-weight:800; letter-spacing:3px; margin-top:1.5rem;">CODE STUDIO</div>
    <div style="margin-top:0.5rem; color:var(--text-dim); font-size:0.8rem; letter-spacing: 1px;">Ishchi muhit tayyorlanmoqda...</div>
</div>

<div id="login-screen" class="overlay hidden" style="background: url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=2072') center/cover; z-index:9999;">
    <div style="position: absolute; inset: 0; background: rgba(0,0,0,0.65); z-index: -1;"></div>
    <div class="modal-box">
        <h2 class="text-gradient" style="font-weight:800; margin-bottom:1.5rem; letter-spacing:1px; text-shadow:0 2px 10px rgba(0,0,0,0.8);">TIZIMGA KIRISH</h2>
        
        <input type="email" id="email" class="input-field" placeholder="Elektron manzil">
        <input type="password" id="password" class="input-field" placeholder="Parol (min. 6 belgi)">
        
        <button class="btn btn--primary btn--full" onclick="authAction('login')" style="padding: 0.8rem;">
            <svg class="spinner" id="login-spinner" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke="rgba(255,255,255,0.3)"></circle><path d="M12 2a10 10 0 0 1 10 10" stroke="#fff"></path></svg>
            <span id="login-text">KIRISH</span>
        </button>
        <button class="btn" style="background:none; border:none; margin-top:1rem; font-size:0.8rem; color:var(--text-dim);" onclick="authAction('signup')">Ro'yxatdan o'tish</button>
    </div>
</div>

<header class="header">
    <div class="header__logo">
        <button class="btn btn--icon desktop-only" onclick="toggleSidebar()" title="Menyu" style="border: none; background: transparent;">
            <svg viewBox="0 0 24 24"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
        <div class="header__logo-container" title="Code Studio Home">
            <svg viewBox="-10 -10 120 120" fill="none">
                <circle cx="50" cy="50" r="46" stroke="url(#codeGradSplash)" stroke-width="6" />
                <path d="M35 35L20 50L35 65" stroke="url(#codeGradSplash)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M65 35L80 50L65 65" stroke="url(#codeGradSplash)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M55 30L45 70" stroke="url(#codeGradSplash)" stroke-width="7" stroke-linecap="round"/>
            </svg>
        </div>
        <span class="text-gradient desktop-only">CODE STUDIO</span>
    </div>
    
    <div class="header__actions">
        <button class="btn btn--icon" onclick="toggleAI()" style="border-color: var(--color-ai); color: var(--color-ai); background: rgba(168, 85, 247, 0.1);">
            <svg viewBox="0 0 24 24"><path d="M12 2a2 2 0 0 1 1.73 1h.27a2 2 0 0 1 2 2v2h2a2 2 0 0 1 2 2v2h.27a2 2 0 0 1 1.73 1 2 2 0 0 1-1.73 3h-.27v2a2 2 0 0 1-2 2h-2v2a2 2 0 0 1-2 2h-.27a2 2 0 0 1-1.73-1 2 2 0 0 1-1.73 1h-.27a2 2 0 0 1-2-2v-2h-2a2 2 0 0 1-2-2v-2h-.27a2 2 0 0 1-1.73-3 2 2 0 0 1 1.73-1h.27v-2a2 2 0 0 1 2-2h2V5a2 2 0 0 1 2-2h.27A2 2 0 0 1 12 2z"></path></svg>
            <span class="desktop-only" style="font-weight: 800; margin-left: 5px;">AI YORDAMCHI</span>
        </button>
        <button class="btn btn--icon desktop-only" onclick="toggleLayout()" title="Oynani yashirish/ko'rsatish"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg></button>
        <button class="btn btn--icon" onclick="editor.execCommand('find')" title="Qidirish"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></button>
        <button class="btn btn--icon" onclick="triggerUndo()" title="Orqaga"><svg viewBox="0 0 24 24"><path d="M3 7v6h6"></path><path d="M3 13a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 13"></path></svg></button>
        <button class="btn btn--icon" onclick="triggerRedo()" title="Oldinga"><svg viewBox="0 0 24 24"><path d="M21 7v6h-6"></path><path d="M21 13a9 9 0 1 1-9-9 9.75 9.75 0 0 1 6.74 2.74L21 13"></path></svg></button>
        <button class="btn btn--icon btn--primary" onclick="toggleModal(true)" title="Saqlash"><svg viewBox="0 0 24 24"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg></button>
        <button class="btn btn--icon btn--danger" onclick="logout()" title="Chiqish"><svg viewBox="0 0 24 24"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg></button>
    </div>
</header>

<div class="workspace" id="workspace">
    <aside class="panel workspace__panel" id="view-files">
        <div class="panel__header">LOYIHALAR <svg viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg></div>
        <div style="padding: 0.75rem 0.75rem 0;"><input type="text" class="input-field" style="margin:0;" id="repo-search" placeholder="Loyihalarni izlash..." oninput="filterRepos()"></div>
        <div class="tab-system">
            <button class="tab-btn active" id="tab-my" onclick="setTab('my')">MENIKILAR</button>
            <button class="tab-btn" id="tab-pub" onclick="setTab('pub')">OMMAVIY</button>
        </div>
        <div id="repo-list" class="list-container"></div>
    </aside>
    <div class="panel workspace__panel active-view" id="editor-container">
        <div class="panel__header">EDITOR <svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg></div>
        <textarea id="editor"></textarea>
    </div>
    <div class="resizer" id="resizer"></div>
    <div class="panel workspace__panel" id="preview-container">
        <div class="panel__header">NATIJA <svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></div>
        <iframe id="preview"></iframe>
    </div>
</div>

<div id="ai-drawer">
    <div class="ai-header">
        <div class="ai-title">
            <svg viewBox="0 0 24 24"><path d="M12 2l3 6.5L22 9.5l-5 5 1.5 7L12 18l-6.5 3.5L7 14.5l-5-5 7-1L12 2z"></path></svg>
            Code Studio AI
        </div>
        <button class="close-ai" onclick="toggleAI()">
            <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
    </div>
    
    <div id="ai-chat-box">
        <div class="chat-bubble bubble-ai">Salom Muhammadrasul! Men sizning doimiy yordamchingizman. Kodingizni tekshirish uchun pastdagi tugmani bosing yoki o'zingizni qiziqtirgan savolni bering. (Faqat dasturlashga oid).</div>
    </div>
    
    <div class="ai-input-area">
        <button class="btn-full-analyze" onclick="requestFullAnalysis()">✨ Hozirgi kodni to'liq tahlil qilish</button>
        <div class="ai-input-wrapper">
            <input type="text" id="ai-input" placeholder="Savol yozing..." onkeypress="handleAIEnter(event)">
            <button onclick="sendToAI()">></button>
        </div>
    </div>
</div>

<div class="mobile-nav">
    <div class="nav-item" onclick="switchView('view-files', this)"><svg viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg><span>Fayllar</span></div>
    <div class="nav-item active" onclick="switchView('editor-container', this)"><svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg><span>Kod</span></div>
    <div class="nav-item" onclick="switchView('preview-container', this)"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg><span>Natija</span></div>
</div>

<div id="save-modal" class="overlay hidden">
    <div class="modal-box">
        <h3 style="margin-top:0; color:#fff; margin-bottom: 1.5rem;">Kodni Saqlash</h3>
        <input type="text" id="repo-name" class="input-field" placeholder="Loyiha nomini kiriting">
        
        <select id="repo-visibility" class="input-field">
            <option value="public">🌍 Ommaviy (Barchaga ko'rinadi)</option>
            <option value="private">🔒 Shaxsiy (Faqat o'zingizga)</option>
        </select>
        <button class="btn btn--primary btn--full" onclick="saveRepo()" style="padding: 0.8rem;">SAQLASH</button>
        <button class="btn btn--full" onclick="toggleModal(false)" style="padding: 0.8rem; background: transparent;">BEKOR QILISH</button>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/mode/xml/xml.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/mode/javascript/javascript.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/mode/css/css.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/mode/htmlmixed/htmlmixed.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/addon/dialog/dialog.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/addon/search/searchcursor.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.15/addon/search/search.min.js"></script>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
    import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
    import { getFirestore, collection, addDoc, query, where, onSnapshot, Timestamp, deleteDoc, doc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
    import { getDatabase, ref, set, onValue } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";

    const firebaseConfig = {
        apiKey: "AIzaSyD24nPrQ38jQarBMTSco5-JDVcKTvcofjs",
        authDomain: "education-15cd7.firebaseapp.com",
        projectId: "education-15cd7",
        storageBucket: "education-15cd7.firebasestorage.app",
        messagingSenderId: "527861318421",
        appId: "1:527861318421:web:18969dd6728be524d3df1c",
        databaseURL: "https://education-15cd7-default-rtdb.firebaseio.com/"
    };

    const app = initializeApp(firebaseConfig);
    const auth = getAuth(app);
    const db = getFirestore(app);
    const rtdb = getDatabase(app);

    let user = null;
    let allRepos = [];

    window.editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
        mode: "htmlmixed", 
        theme: "dracula", 
        lineNumbers: true, 
        autoCloseTags: true, 
        lineWrapping: true
    });

    const savedCode = localStorage.getItem('codestudio_saved_code');
    if (savedCode) {
        editor.setValue(savedCode);
    }

    window.triggerUndo = () => editor.undo();
    window.triggerRedo = () => editor.redo();

    const resizer = document.getElementById('resizer');
    const editorContainer = document.getElementById('editor-container');
    const iframe = document.getElementById('preview');
    const aside = document.getElementById('view-files');
    const workspace = document.getElementById('workspace');

    let isResizing = false;

    resizer.addEventListener('mousedown', (e) => {
        isResizing = true; 
        document.body.classList.add('resizing'); 
        resizer.classList.add('active');
        iframe.style.pointerEvents = 'none'; 
        e.preventDefault();
    });

    document.addEventListener('mousemove', (e) => {
        if (!isResizing) return;
        const rect = workspace.getBoundingClientRect();
        let asideWidth = aside.classList.contains('open') ? aside.offsetWidth + 12 : 0; 
        let newWidth = e.clientX - rect.left - asideWidth - 12; 
        
        if (newWidth < 200) newWidth = 200; 
        let maxWidth = rect.width - asideWidth - 24 - 200; 
        if (newWidth > maxWidth) newWidth = maxWidth;
        
        editorContainer.style.width = `${newWidth}px`;
        editor.refresh(); 
    });

    document.addEventListener('mouseup', () => {
        if (isResizing) { 
            isResizing = false; 
            document.body.classList.remove('resizing'); 
            resizer.classList.remove('active'); 
            iframe.style.pointerEvents = 'auto'; 
        }
    });

    window.toggleLayout = () => {
        if (window.innerWidth < 900) return;
        if (editorContainer.style.display === 'none') {
            editorContainer.style.display = 'flex'; 
            editorContainer.style.width = '50%'; 
            resizer.style.display = 'flex';
        } else {
            editorContainer.style.display = 'none'; 
            resizer.style.display = 'none';
        }
        setTimeout(() => editor.refresh(), 50);
    };

    window.toggleSidebar = () => { 
        aside.classList.toggle('open'); 
        setTimeout(() => editor.refresh(), 400); 
    };

    window.switchView = (viewId, el) => {
        document.querySelectorAll('.workspace__panel').forEach(v => v.classList.remove('active-view'));
        document.getElementById(viewId).classList.add('active-view');
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        el.classList.add('active');
        if(viewId === 'editor-container') setTimeout(() => editor.refresh(), 50);
    };

    window.filterRepos = () => {
        const term = document.getElementById('repo-search').value.toLowerCase();
        const filtered = allRepos.filter(r => r.name.toLowerCase().includes(term));
        renderList(filtered);
    };

    function renderList(items) {
        const list = document.getElementById('repo-list');
        list.innerHTML = "";
        const isAdmin = user && user.email === 'admin@admin.com';
        
        items.forEach(item => {
            const card = document.createElement('div');
            card.className = "card";
            
            const info = document.createElement('div');
            info.className = "card__info";
            info.innerHTML = `
                <span class="card__title">${item.name}</span>
                <small style="color:${item.isPublic ? '#4ade80' : '#f87171'}">
                    ${item.isPublic ? '🌍 Ommaviy' : '🔒 Shaxsiy'}
                </small>
            `;
            card.appendChild(info);

            if (item.uid === user.uid || isAdmin) {
                const delBtn = document.createElement('button');
                delBtn.className = 'delete-btn';
                delBtn.innerHTML = `<svg viewBox="0 0 24 24"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>`;
                delBtn.onclick = async (e) => {
                    e.stopPropagation();
                    if(confirm(`"${item.name}" loyihasini butunlay o'chirib tashlaysizmi?`)) {
                        await deleteDoc(doc(db, "repos", item.id));
                    }
                };
                card.appendChild(delBtn);
            }

            card.onclick = () => {
                editor.setValue(item.code);
                updatePreview();
                
                if (window.innerWidth >= 900) {
                    if (!item.isPublic) {
                        editorContainer.style.display = 'none'; resizer.style.display = 'none';
                    } else {
                        editorContainer.style.display = 'flex'; editorContainer.style.width = '50%'; resizer.style.display = 'flex';
                    }
                    setTimeout(() => editor.refresh(), 50);
                } else {
                    if (!item.isPublic) switchView('preview-container', document.querySelectorAll('.nav-item')[2]);
                    else switchView('editor-container', document.querySelectorAll('.nav-item')[1]);
                }
            };
            list.appendChild(card);
        });
    }

    const toggleLoading = (isLoading) => {
        document.getElementById('login-spinner').style.display = isLoading ? 'block' : 'none';
        document.getElementById('login-text').style.display = isLoading ? 'none' : 'block';
    }

    window.authAction = async (type) => {
        const e = document.getElementById('email').value;
        const p = document.getElementById('password').value;
        if(!e || !p) return alert("Email va parolni kiriting!");
        
        toggleLoading(true);
        try {
            if(type === 'signup') await createUserWithEmailAndPassword(auth, e, p);
            else await signInWithEmailAndPassword(auth, e, p);
        } catch(err) { alert("Xato: " + err.message); } 
        finally { toggleLoading(false); }
    };

    window.addEventListener('load', () => { 
        setTimeout(() => { document.getElementById('splash-screen').classList.add('hidden'); updatePreview(); }, 1500); 
    });

    onAuthStateChanged(auth, u => {
        if(u) {
            user = u; 
            document.getElementById('login-screen').classList.add('hidden'); 
            setTab('my');
        } else {
            user = null; 
            document.getElementById('login-screen').classList.remove('hidden');
        }
    });

    window.setTab = (t) => {
        document.getElementById('tab-my').className = t === 'my' ? 'tab-btn active' : 'tab-btn';
        document.getElementById('tab-pub').className = t === 'pub' ? 'tab-btn active' : 'tab-btn';
        const q = t === 'my' ? query(collection(db, "repos"), where("uid", "==", user.uid)) : query(collection(db, "repos"), where("isPublic", "==", true));
        onSnapshot(q, (snaps) => {
            allRepos = [];
            snaps.forEach(d => allRepos.push({ id: d.id, ...d.data() }));
            filterRepos();
        });
    };

    editor.on('change', () => {
        updatePreview();
        const currentCode = editor.getValue();
        localStorage.setItem('codestudio_saved_code', currentCode);
        if(user) set(ref(rtdb, `drafts/${user.uid}`), { code: currentCode, t: Date.now() });
    });

    function updatePreview() {
        const p = document.getElementById('preview').contentDocument;
        p.open(); 
        p.write('<style>body{color:#000; font-family:sans-serif; margin:0; padding:10px;}</style>' + editor.getValue()); 
        p.close();
    }

    window.toggleModal = (v) => {
        const modal = document.getElementById('save-modal');
        if(v) modal.classList.remove('hidden'); else modal.classList.add('hidden');
    }
    
    window.saveRepo = async () => {
        const name = document.getElementById('repo-name').value;
        const isPublic = document.getElementById('repo-visibility').value === 'public'; 
        
        if(!name) return alert("Iltimos loyiha nomini kiriting!");
        
        await addDoc(collection(db, "repos"), { 
            uid: user.uid, name: name, code: editor.getValue(), isPublic: isPublic, time: Timestamp.now() 
        });
        
        toggleModal(false);
        document.getElementById('repo-name').value = '';
    };
    
    window.logout = () => signOut(auth);

    // =========================================
    // ✨ YANGI QO'SHILGAN AI LOGIKASI
    // =========================================
    const aiDrawer = document.getElementById('ai-drawer');
    const chatBox = document.getElementById('ai-chat-box');
    const aiInput = document.getElementById('ai-input');

    window.toggleAI = () => {
        aiDrawer.classList.toggle('open');
    };

    window.handleAIEnter = (e) => { 
        if(e.key === 'Enter') sendToAI(); 
    };

    window.sendToAI = async () => {
        const text = aiInput.value.trim();
        if(!text) return;
        
        appendMessage(text, 'user');
        aiInput.value = '';
        
        const prompt = `Foydalanuvchi so'rovi: "${text}"\n\nFoydalanuvchining hozirgi kodi (agar u kod haqida so'rasa shunga qara, bo'lmasa mavzuni ohista kodga bur):\n\`\`\`html\n${editor.getValue()}\n\`\`\``;
        await fetchAndTypeAI(prompt);
    };

    window.requestFullAnalysis = async () => {
        const code = editor.getValue().trim();
        appendMessage("Mening yozgan kodimni batafsil va uzoq qilib tahlil qilib bering.", 'user');
        
        const prompt = `Foydalanuvchining kodi ushbu:\n\`\`\`html\n${code}\n\`\`\`\nIltimos, ushbu kodni to'liq, ipidan-ignasigacha batafsil tahlil qil. Xatolarni ayt va qanday yaxshilash mumkinligini darslikdek tushuntir.`;
        await fetchAndTypeAI(prompt);
    };

    function appendMessage(text, sender) {
        const div = document.createElement('div');
        div.className = `chat-bubble bubble-${sender}`;
        div.innerText = text;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
        return div;
    }

    async function fetchAndTypeAI(promptText) {
        // "O'ylamoqda..." belgisi
        const aiBubble = appendMessage("", 'ai');
        aiBubble.classList.add('typing-cursor'); 
        
        try {
            const response = await fetch('http://127.0.0.1:5000/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ code: promptText })
            });
            const data = await response.json();
            const fullText = data.analysis || "Xatolik: AI dan javob kelmadi.";
            
            // Animatsiya orqali yozish (Gemini Effect)
            await typeWriterEffect(aiBubble, fullText, 15);
            
        } catch (err) {
            aiBubble.classList.remove('typing-cursor');
            aiBubble.innerText = "⚠️ Xatolik yuz berdi. Iltimos, terminalda 'python3 ai.py' ishlayotganiga ishonch hosil qiling.";
        }
    }

    function typeWriterEffect(element, text, speed) {
        return new Promise(resolve => {
            let i = 0;
            element.innerHTML = ''; 
            
            function type() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    chatBox.scrollTop = chatBox.scrollHeight;
                    setTimeout(type, speed);
                } else {
                    element.classList.remove('typing-cursor'); 
                    resolve();
                }
            }
            type();
        });
  // Sizning Render havolangiz
const BACKEND_URL = "https://ai-backend-odjb.onrender.com";

async function askAI() {
    const inputField = document.getElementById('ai-input');
    const chatBox = document.getElementById('ai-chat-box');
    const prompt = inputField.value;

    if (!prompt) return;

    // 1. Foydalanuvchi xabarini ekranga chiqarish
    chatBox.innerHTML += `<div style="background: #3b82f6; color: white; padding: 8px 12px; border-radius: 12px 12px 0 12px; align-self: flex-end; max-width: 80%; margin-bottom: 10px;">${prompt}</div>`;
    inputField.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    // 2. Yuklanish holati (Loading indicator)
    const loadingId = 'loading-' + Date.now();
    chatBox.innerHTML += `<div id="${loadingId}" style="color: #64748b; font-size: 11px; margin-bottom: 10px;">AI o'ylamoqda...</div>`;

    try {
        // 3. Render backendga so'rov yuborish
        const response = await fetch(`${BACKEND_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: prompt }),
        });

        const data = await response.json();

        // 4. AI javobini chiqarish
        document.getElementById(loadingId).remove(); // Loadingni o'chirish
        chatBox.innerHTML += `<div style="background: #1e293b; color: #cbd5e1; padding: 10px 15px; border-radius: 12px 12px 12px 0; align-self: flex-start; max-width: 85%; border: 1px solid rgba(255,255,255,0.05); margin-bottom: 10px;">${data.reply}</div>`;
        
    } catch (error) {
        document.getElementById(loadingId).innerText = "❌ Xatolik: Backend ulanmadi yoki 'CORS' xatosi.";
        console.error("Xatolik:", error);
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}  }
</script>
</body>
</html>
