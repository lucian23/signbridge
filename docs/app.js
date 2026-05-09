
const STORAGE_KEY = 'signbridge_data';

function loadData() {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw);
    return getDefaultData();
}
function saveData(data) { localStorage.setItem(STORAGE_KEY, JSON.stringify(data)); }

function getDefaultData() {
    const signs = [
        {id:'a',name:'A',cat:'Litere',sign:'✊',desc:'Pumn inchis, deget mare lateral'},
        {id:'b',name:'B',cat:'Litere',sign:'🖐️',desc:'Palma deschisa cu degete unite'},
        {id:'c',name:'C',cat:'Litere',sign:'👌',desc:'Degetul mare si aratator formeaza C'},
        {id:'d',name:'D',cat:'Litere',sign:'☝️',desc:'Degetul aratator sus, celelalte inchise'},
        {id:'e',name:'E',cat:'Litere',sign:'✊',desc:'Pumn inchis, degete curbate'},
        {id:'f',name:'F',cat:'Litere',sign:'🤞',desc:'Degetele mare si aratator formeaza F'},
        {id:'g',name:'G',cat:'Litere',sign:'🤙',desc:'Degetele mare si aratator formeaza G'},
        {id:'h',name:'H',cat:'Litere',sign:'✌️',desc:'Degetele aratator si mijlociu formeaza H'},
        {id:'i',name:'I',cat:'Litere',sign:'☝️',desc:'Degetul mic ridicat'},
        {id:'j',name:'J',cat:'Litere',sign:'👆',desc:'Degetul aratator face semnul J'},
        {id:'k',name:'K',cat:'Litere',sign:'🤟',desc:'Degetele mare, aratator si mijlociu'},
        {id:'l',name:'L',cat:'Litere',sign:'🤘',desc:'Degetele mare si aratator in L'},
        {id:'m',name:'M',cat:'Litere',sign:'✊',desc:'Pumn cu 3 degete peste degetul mare'},
        {id:'n',name:'N',cat:'Litere',sign:'✌️',desc:'Pumn cu 2 degete peste degetul mare'},
        {id:'o',name:'O',cat:'Litere',sign:'👌',desc:'Degetele mare si aratator formeaza O'},
        {id:'p',name:'P',cat:'Litere',sign:'👇',desc:'Degetul aratator in jos'},
        {id:'r',name:'R',cat:'Litere',sign:'🤞',desc:'Degetele aratator si mijlociu incrucisate'},
        {id:'s',name:'S',cat:'Litere',sign:'✊',desc:'Pumn inchis'},
        {id:'t',name:'T',cat:'Litere',sign:'✊',desc:'Pumn cu degetul mare intre aratator si mijlociu'},
        {id:'u',name:'U',cat:'Litere',sign:'🤟',desc:'Degetele aratator si mijlociu unite ridicate'},
        {id:'v',name:'V',cat:'Litere',sign:'✌️',desc:'Degetele aratator si mijlociu in V'},
        {id:'x',name:'X',cat:'Litere',sign:'🤙',desc:'Degetul aratator curb peste degetul mare'},
        {id:'z',name:'Z',cat:'Litere',sign:'👌',desc:'Degetul aratator traseaza Z in aer'},
        {id:'1',name:'1',cat:'Cifre',sign:'☝️',desc:'Degetul aratator ridicat'},
        {id:'2',name:'2',cat:'Cifre',sign:'✌️',desc:'Degetele aratator si mijlociu ridicate'},
        {id:'3',name:'3',cat:'Cifre',sign:'🤟',desc:'3 degete ridicate'},
        {id:'4',name:'4',cat:'Cifre',sign:'🖐️',desc:'4 degete ridicate'},
        {id:'5',name:'5',cat:'Cifre',sign:'🖐️',desc:'Palma deschisa cu 5 degete'},
        {id:'6',name:'6',cat:'Cifre',sign:'🤙',desc:'Degetul mic, inelar si mijlociu ridicate'},
        {id:'7',name:'7',cat:'Cifre',sign:'✌️',desc:'Degetele mare, aratator si mijlociu ridicate'},
        {id:'8',name:'8',cat:'Cifre',sign:'👌',desc:'Degetul mare si aratator formeaza 8'},
        {id:'9',name:'9',cat:'Cifre',sign:'🤞',desc:'Degetele aratator si mijlociu curbate'},
        {id:'0',name:'0',cat:'Cifre',sign:'👌',desc:'Degetele mare si aratator formeaza O'},
        {id:'buna',name:'Bună',cat:'Salutări',sign:'👋',desc:'Palma deschisa miscare spre exterior'},
        {id:'pa',name:'Pa',cat:'Salutări',sign:'👋',desc:'Palma deschisa miscare stanga-dreapta'},
        {id:'mulțumesc',name:'Mulțumesc',cat:'Salutări',sign:'🤝',desc:'Palma la buza inferioara, miscare in exterior'},
        {id:'te-ro',name:'Te rog',cat:'Salutări',sign:'🙏',desc:'Palmele unite, miscare circulara'},
        {id:'mama',name:'Mamă',cat:'Familie',sign:'🤱',desc:'Degetul aratator atinge obrazul de 2 ori'},
        {id:'tata',name:'Tată',cat:'Familie',sign:'👨',desc:'Degetul aratator atinge fruntea de 2 ori'},
        {id:'frate',name:'Frate',cat:'Familie',sign:'👬',desc:'Degetele aratator de la ambele maini se ating'},
        {id:'sora',name:'Soră',cat:'Familie',sign:'👭',desc:'Degetele mijlocii se ating'},
        {id:'fericit',name:'Fericit',cat:'Emoții',sign:'😊',desc:'Degetul aratator traseaza zambetul'},
        {id:'trist',name:'Trist',cat:'Emoții',sign:'😢',desc:'Degetele aratatoare traseaza lacrima'},
        {id:'suparat',name:'Supărat',cat:'Emoții',sign:'😠',desc:'Pumnul bate pieptul'},
        {id:'obosit',name:'Obosit',cat:'Emoții',sign:'😴',desc:'Palmele se unesc sub obraji'},
        {id:'soare',name:'Soare',cat:'Natura',sign:'☀️',desc:'Degetele se deschid deasupra capului'},
        {id:'ploaie',name:'Ploaie',cat:'Natura',sign:'🌧️',desc:'Degetele coboara in jos ca picaturile'},
        {id:'flori',name:'Flori',cat:'Natura',sign:'🌸',desc:'Degetele se deschid ca o floare'},
        {id:'apa',name:'Apă',cat:'Natura',sign:'💧',desc:'Degetele ating buzele'},
        {id:'caine',name:'Câine',cat:'Cuvinte de bază',sign:'🐕',desc:'Degetul aratator si degetul mare ating nasul'},
        {id:'pisica',name:'Pisică',cat:'Cuvinte de bază',sign:'🐈',desc:'Degetele mimeaza mustatile'},
        {id:'casă',name:'Casă',cat:'Cuvinte de bază',sign:'🏠',desc:'Varfurile degetelor formeaza acoperisul'},
        {id:'masă',name:'Masă',cat:'Cuvinte de bază',sign:'🍽️',desc:'Palmele paralele ca masa'},
        {id:'carte',name:'Carte',cat:'Cuvinte de bază',sign:'📖',desc:'Palmele deschise impreuna'},
        {id:'mâncare',name:'Mâncare',cat:'Cuvinte de bază',sign:'🍽️',desc:'Degetele ating buzele de mai multe ori'},
    ];
    return {signs, learned:[], quizzes:[], badges:[]};
}

let DATA = loadData();

// Navigation
document.querySelectorAll('.nav-link').forEach(link=>{
    link.addEventListener('click',e=>{
        e.preventDefault();
        const page = link.dataset.page;
        showPage(page);
        document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));
        link.classList.add('active');
    });
});

function showPage(page) {
    document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
    const el = document.getElementById(page+'-page');
    if(el) el.classList.add('active');
    if(page==='dashboard') renderDashboard();
    if(page==='dictionary') renderDictionary();
    if(page==='simulator') renderSimulator();
    if(page==='leaderboard') renderLeaderboard();
}

// Dashboard
function renderDashboard() {
    document.getElementById('dash-semi').textContent = DATA.learned.length;
    document.getElementById('dash-quiz').textContent = DATA.quizzes.length;
    const avg = DATA.quizzes.length?Math.round(DATA.quizzes.reduce((a,q)=>a+q.score,0)/DATA.quizzes.length):0;
    document.getElementById('dash-score').textContent = avg+'%';

    const total = DATA.signs.length;
    const pct = Math.round((DATA.learned.length/total)*100);
    document.getElementById('progress-fill').style.width = pct+'%';

    const badges = [];
    if(DATA.learned.length>=5) badges.push('🥉 Începător');
    if(DATA.learned.length>=15) badges.push('🥈 Avansat');
    if(DATA.learned.length>=25) badges.push('🥇 Expert');
    if(avg>=80 && DATA.quizzes.length>=3) badges.push('⭐ Maestru');
    if(DATA.learned.length>=40) badges.push('🏆 Legenda LSR');
    document.getElementById('badges').innerHTML = badges.map(b=>`<span class="badge badge-green">${b}</span>`).join('');
}

// Dictionary
function renderDictionary() {
    const search = document.getElementById('dict-search').value.toLowerCase();
    const filter = document.getElementById('dict-filter').value;
    let items = DATA.signs;
    if(search) items = items.filter(s=>s.name.toLowerCase().includes(search)||s.cat.toLowerCase().includes(search));
    if(filter) items = items.filter(s=>s.cat===filter);
    document.getElementById('dict-grid').innerHTML = items.map(s=>`
        <div class="hand-card" onclick="learnSign('${s.id}')">
            <div class="sign">${s.sign}</div>
            <div class="name">${s.name}</div>
            <div class="cat">${s.cat}</div>
            ${DATA.learned.includes(s.id)?'<div style="color:#10b981;font-size:11px;margin-top:4px">✓ Învățat</div>':''}
        </div>
    `).join('');
}
function learnSign(id) {
    if(!DATA.learned.includes(id)) { DATA.learned.push(id); saveData(DATA); }
    renderDictionary();
}
document.getElementById('dict-search').addEventListener('input',renderDictionary);
document.getElementById('dict-filter').addEventListener('change',renderDictionary);

// Simulator
function renderSimulator() {
    document.getElementById('sim-grid').innerHTML = DATA.signs.map(s=>`
        <div class="hand-card" onclick="showSign('${s.id}')">
            <div class="sign">${s.sign}</div>
            <div class="name">${s.name}</div>
        </div>
    `).join('');
}
function showSign(id) {
    const s = DATA.signs.find(x=>x.id===id);
    document.getElementById('sim-display').innerHTML = `
        <div style="font-size:120px">${s.sign}</div>
        <p style="font-size:24px;font-weight:700;margin-top:12px">${s.name}</p>
        <p style="color:#64748b;margin-top:8px">${s.desc}</p>
        <p style="margin-top:8px"><span class="tag">${s.cat}</span></p>
        ${!DATA.learned.includes(id)?`<button onclick="learnSign('${id}');showSign('${id}')" style="margin-top:16px;padding:10px 20px;background:#3b82f6;color:white;border:none;border-radius:8px;cursor:pointer">Marchează ca învățat</button>`:'<p style="color:#10b981;margin-top:12px">✓ Semn învățat</p>'}
    `;
}

// Quiz
let currentQuiz = null;
document.getElementById('start-quiz').addEventListener('click',()=>{
    const level = parseInt(document.getElementById('quiz-level').value);
    const pool = level===1?DATA.signs.filter(s=>s.cat==='Litere'):
                 level===2?DATA.signs.filter(s=>['Salutări','Familie','Emoții'].includes(s.cat)):
                 DATA.signs.filter(s=>['Natura','Cuvinte de bază'].includes(s.cat)||s.cat==='Emoții');
    const questions = [];
    const used = new Set();
    while(questions.length<10 && used.size<pool.length) {
        const s = pool[Math.floor(Math.random()*pool.length)];
        if(!used.has(s.id)) {
            used.add(s.id);
            const wrong = pool.filter(x=>x.id!==s.id).sort(()=>Math.random()-0.5).slice(0,3);
            const options = [...wrong,s].sort(()=>Math.random()-0.5);
            questions.push({sign:s,options,answer:s.id});
        }
    }
    currentQuiz = {level,questions,index:0,score:0};
    showQuestion();
});

function showQuestion() {
    const q = currentQuiz.questions[currentQuiz.index];
    const container = document.getElementById('quiz-container');
    container.innerHTML = `
        <div class="quiz-box">
            <p style="color:#64748b">Întrebarea ${currentQuiz.index+1} din ${currentQuiz.questions.length} | Nivel ${currentQuiz.level}</p>
            <div class="sign">${q.sign.sign}</div>
            <p style="color:#64748b;margin-bottom:16px">Ce semn reprezintă?</p>
            <div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center">
                ${q.options.map(o=>`<button class="quiz-btn" onclick="answerQuiz('${o.id}')">${o.name}</button>`).join('')}
            </div>
        </div>
    `;
}

function answerQuiz(id) {
    const q = currentQuiz.questions[currentQuiz.index];
    const correct = id===q.answer;
    if(correct) currentQuiz.score++;
    currentQuiz.index++;
    if(currentQuiz.index>=currentQuiz.questions.length) {
        const pct = Math.round((currentQuiz.score/currentQuiz.questions.length)*100);
        DATA.quizzes.push({level:currentQuiz.level,score:pct,date:new Date().toISOString()});
        saveData(DATA);
        let msg = pct>=90?'🌟 Excelent!':'pct>=70?'✅ Bun!':'⚠️ Mai exersează';
        document.getElementById('quiz-container').innerHTML = `
            <div class="quiz-box">
                <h3>${msg}</h3>
                <p style="font-size:48px;font-weight:700;color:#3b82f6;margin:16px 0">${pct}%</p>
                <p>${currentQuiz.score} / ${currentQuiz.questions.length} corecte</p>
                <button onclick="currentQuiz=null;document.getElementById('quiz-container').innerHTML='';" style="margin-top:16px;padding:10px 20px;background:#3b82f6;color:white;border:none;border-radius:8px;cursor:pointer">Închide</button>
            </div>
        `;
        renderDashboard();
        return;
    }
    showQuestion();
}

// Leaderboard
function renderLeaderboard() {
    const players = [
        {name:'Ana M.',tests:12,avg:92},
        {name:'Mihai P.',tests:8,avg:85},
        {name:'Elena D.',tests:15,avg:78},
        {name:'George R.',tests:5,avg:72},
        {name:'Maria S.',tests:20,avg:95},
    ];
    const myTests = DATA.quizzes.length;
    const myAvg = myTests?Math.round(DATA.quizzes.reduce((a,q)=>a+q.score,0)/myTests):0;
    if(myTests>0) players.push({name:'Tu',tests:myTests,avg:myAvg,you:true});
    players.sort((a,b)=>b.avg-a.avg);
    document.getElementById('leaderboard-body').innerHTML = players.map((p,i)=>`
        <tr class="${p.you?'rank-1':''}">
            <td><strong>${i+1}</strong></td>
            <td>${p.name}</td>
            <td>${p.tests}</td>
            <td>${p.avg}%</td>
            <td>${p.avg>=90?'⭐ Expert':p.avg>=70?'✅ Avansat':'📝 Începător'}</td>
        </tr>
    `).join('');
}

renderDashboard();
