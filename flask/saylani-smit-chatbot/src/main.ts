import { GoogleGenAI } from "@google/genai";

const SAYLANI_GREEN = "#00a651";
const SYSTEM_INSTRUCTION = `You are a helpful and professional AI assistant for Saylani Mass IT Training (SMIT), a flagship program of Saylani Welfare International Trust. 

Your goals:
1. Provide accurate information about SMIT courses (Web & Mobile Web Development, Artificial Intelligence, Graphic Design, Video Editing, Mobile App Development, CCNA, etc.).
2. Explain the admission process (usually involves an online test and interview).
3. List campus locations (Main Branch at Bahadurabad, Karachi; branches in Lahore, Faisalabad, Hyderabad, etc.).
4. Share Saylani's mission: "Serving humanity regardless of religion, cast, or creed."
5. Be encouraging to students, as SMIT provides free, high-quality IT education to the youth of Pakistan.
6. If you don't know a specific detail (like a specific date for a future batch), suggest they visit the official website (saylaniwelfare.com) or their nearest campus.

Tone: Professional, polite, helpful, and patriotic.`;

// DOM Elements
const messagesList = document.getElementById('messages-list')!;
const chatForm = document.getElementById('chat-form') as HTMLFormElement;
const chatInput = document.getElementById('chat-input') as HTMLInputElement;
const sendBtn = document.getElementById('send-btn') as HTMLButtonElement;
const clearBtn = document.getElementById('clear-chat')!;
const quickBtns = document.querySelectorAll('.quick-btn');
const welcomeTime = document.querySelector('.welcome-time')!;

// Set initial time
welcomeTime.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

// Gemini Setup
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY! });
const chat = ai.chats.create({
  model: "gemini-3-flash-preview",
  config: {
    systemInstruction: SYSTEM_INSTRUCTION,
  },
});

function createMessageElement(role: 'user' | 'model', text: string) {
  const div = document.createElement('div');
  div.className = `flex ${role === 'user' ? 'justify-end' : 'justify-start'} animate-fade-in`;
  
  const inner = document.createElement('div');
  inner.className = `flex gap-3 max-w-[85%] ${role === 'user' ? 'flex-row-reverse' : 'flex-row'}`;
  
  const icon = document.createElement('div');
  icon.className = `w-8 h-8 rounded-full flex-shrink-0 flex items-center justify-center shadow-sm ${role === 'user' ? 'bg-gray-800 text-white' : 'text-white'}`;
  if (role === 'model') icon.style.backgroundColor = SAYLANI_GREEN;
  
  icon.innerHTML = role === 'user' 
    ? '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
    : '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>';

  const content = document.createElement('div');
  content.className = `rounded-2xl px-4 py-3 shadow-sm ${role === 'user' ? 'bg-gray-800 text-white rounded-tr-none' : 'bg-white text-gray-800 border border-gray-100 rounded-tl-none'}`;
  
  const textDiv = document.createElement('div');
  textDiv.className = 'chat-text text-sm leading-relaxed';
  // Simple markdown-to-html replacement for vanilla
  textDiv.innerHTML = text
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>')
    .replace(/- (.*?)(?=\n|$)/g, '<li>$1</li>')
    .replace(/(<li>.*?<\/li>)+/g, '<ul>$&</ul>');
    
  const timeDiv = document.createElement('div');
  timeDiv.className = `text-[10px] mt-2 opacity-50 ${role === 'user' ? 'text-right' : 'text-left'}`;
  timeDiv.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  content.appendChild(textDiv);
  content.appendChild(timeDiv);
  inner.appendChild(icon);
  inner.appendChild(content);
  div.appendChild(inner);
  
  return div;
}

async function handleSend(text: string) {
  if (!text.trim()) return;

  // Add user message
  messagesList.appendChild(createMessageElement('user', text));
  chatInput.value = '';
  window.scrollTo(0, document.body.scrollHeight);

  // Add loading indicator
  const loadingDiv = document.createElement('div');
  loadingDiv.className = 'flex justify-start text-gray-400 ml-11 text-xs italic animate-pulse';
  loadingDiv.id = 'loading-indicator';
  loadingDiv.textContent = 'Saylani Assistant is typing...';
  messagesList.appendChild(loadingDiv);

  try {
    const response = await chat.sendMessage({ message: text });
    const modelText = response.text;
    
    // Remove loading
    document.getElementById('loading-indicator')?.remove();
    
    // Add model message
    messagesList.appendChild(createMessageElement('model', modelText));
    
    // Hide quick questions after first interaction
    document.getElementById('quick-questions')?.classList.add('hidden');
  } catch (error) {
    console.error(error);
    document.getElementById('loading-indicator')?.remove();
    messagesList.appendChild(createMessageElement('model', "I'm sorry, I encountered an error. Please try again."));
  }

  window.scrollTo(0, document.body.scrollHeight);
}

chatForm.addEventListener('submit', (e) => {
  e.preventDefault();
  handleSend(chatInput.value);
});

quickBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const query = btn.getAttribute('data-query')!;
    handleSend(query);
  });
});

clearBtn.addEventListener('click', () => {
  messagesList.innerHTML = `
    <div class="flex justify-start">
      <div class="flex gap-3 max-w-[85%] flex-row">
        <div class="w-8 h-8 rounded-full flex-shrink-0 flex items-center justify-center shadow-sm bg-saylani-green text-white">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>
        </div>
        <div class="rounded-2xl px-4 py-3 shadow-sm bg-white text-gray-800 border border-gray-100 rounded-tl-none">
          <div class="chat-text text-sm leading-relaxed">
            Assalam-o-Alaikum! Welcome to Saylani SMIT Assistant. How can I help you today with your IT journey?
          </div>
          <div class="text-[10px] mt-2 opacity-50 text-left">${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
        </div>
      </div>
    </div>
  `;
  document.getElementById('quick-questions')?.classList.remove('hidden');
});
