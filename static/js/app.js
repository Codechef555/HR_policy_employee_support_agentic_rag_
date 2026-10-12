const chat = document.getElementById('chat');
const form = document.getElementById('chatForm');
const question = document.getElementById('question');
const trace = document.getElementById('trace');
const sourceUsed = document.getElementById('sourceUsed');

function escapeHtml(s=''){return s.replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));}
function formatText(s=''){return escapeHtml(s).replace(/\n/g,'<br>');}

function addMessage(role, text, source='', citations=[]){
    const wrap=document.createElement('div'); wrap.className=`message ${role}`;
    const citeHtml=citations.length?`<div class="citations"><strong>Sources</strong><br>${citations.map(c=>c.url?`<a href="${escapeHtml(c.url)}" target="_blank" rel="noopener">${escapeHtml(c.title)}</a>`:escapeHtml(c.title)).join('<br>')}</div>`:'';
    wrap.innerHTML=`<div class="avatar">AI</div><div class="bubble">${formatText(text)}${source?`<div class="answer-source">Source: ${escapeHtml(source)}</div>`:''}${citeHtml}</div>`;

    chat.appendChild(wrap); chat.scrollTop=chat.scrollHeight;
}

function renderTrace(items=[]){}