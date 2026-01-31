document.addEventListener('DOMContentLoaded', () => {

    // --- Analytics Charts ---
    if (document.getElementById('sourceChart')) {
        const ctxSource = document.getElementById('sourceChart').getContext('2d');
        new Chart(ctxSource, {
            type: 'bar',
            data: {
                labels: ['Solar', 'Acoustic', 'Piezo', 'Thermo'],
                datasets: [{
                    label: 'Energy Harvested (mAh/hr)',
                    data: [120, 45, 80, 60],
                    backgroundColor: ['#ffeb3b', '#00e5ff', '#ff0055', '#ff9800']
                }]
            },
            options: { scales: { y: { beginAtZero: true } }, plugins: { legend: { display: false } } }
        });

        const ctxPie = document.getElementById('pieChart').getContext('2d');
        new Chart(ctxPie, {
            type: 'doughnut',
            data: {
                labels: ['Solar', 'Acoustic', 'Piezo', 'Thermo'],
                datasets: [{
                    data: [40, 15, 25, 20],
                    backgroundColor: ['#ffeb3b', '#00e5ff', '#ff0055', '#ff9800'],
                    borderWidth: 0
                }]
            }
        });

        const ctxLine = document.getElementById('lineChart').getContext('2d');
        new Chart(ctxLine, {
            type: 'line',
            data: {
                labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
                datasets: [{
                    label: 'Battery Level (%)',
                    data: [85, 80, 75, 90, 88, 95], // Shows charging events
                    borderColor: '#00f2fe',
                    tension: 0.4
                }]
            }
        });
    }

    // --- Battery Simulation ---

    if (document.getElementById('battery-level')) {
        let level = 50;
        const levelBar = document.getElementById('battery-level');
        const text = document.getElementById('percentage-text');
        const statusText = document.getElementById('status-text');
        const chargingToggle = document.getElementById('charging-toggle');

        // Function to update status text
        const updateStatus = () => {
            if (chargingToggle && chargingToggle.checked) {
                statusText.innerText = "Charging - Multiple Sources Active";
                statusText.style.color = "#00f2fe";
            } else {
                statusText.innerText = "Not Charging - Sources Disconnected";
                statusText.style.color = "#ff5555";
            }
        };

        // Initial check
        if (chargingToggle) {
            updateStatus();
            chargingToggle.addEventListener('change', updateStatus);
        }

        setInterval(() => {
            if (chargingToggle && chargingToggle.checked && level < 100) {
                level += 1;
                levelBar.style.width = level + '%';
                text.innerText = level + '%';

                // Color change based on level
                if (level > 80) levelBar.style.background = 'linear-gradient(90deg, #00f2fe, #4facfe)';
                else if (level < 20) levelBar.style.background = '#ff0055';
            }
        }, 2000); // Simulate charging every 2s
    }

});

// --- Chatbot Logic ---
function sendMessage() {
    const input = document.getElementById('user-input');
    const history = document.getElementById('chat-history');
    const msg = input.value.trim();

    if (msg) {
        // User Message
        const userDiv = document.createElement('div');
        userDiv.className = 'message user';
        userDiv.innerHTML = `<div class="bubble">${msg}</div>`;
        history.appendChild(userDiv);
        input.value = '';
        history.scrollTop = history.scrollHeight;

        // Bot Response Simulation
        setTimeout(() => {
            const botDiv = document.createElement('div');
            botDiv.className = 'message bot';
            botDiv.style.cssText = 'margin-bottom: 15px; display: flex; align-items: flex-start;';

            let response = "I'm not sure about that specific detail. You can ask me about: Solar, Acoustic, Piezo, Thermal energy, or <strong>Charging Problems</strong>.";
            const m = msg.toLowerCase();

            // Core Technology
            if (m.includes('solar') || m.includes('sun') || m.includes('light')) {
                response = "Our <strong>Flexible Solar Panels</strong> use printed perovskite cells. They charge efficiently in both outdoor sunlight and indoor artificial lighting.";
            }
            else if (m.includes('sound') || m.includes('acoustic') || m.includes('voice') || m.includes('noise')) {
                response = "The <strong>Acoustic Harvester</strong> uses nanofiber membranes to convert sound waves (like your voice or music) into electrical energy. It works best in noisy environments!";
            }
            else if (m.includes('piezo') || m.includes('kinetic') || m.includes('move') || m.includes('walk') || m.includes('shake')) {
                response = "<strong>Piezoelectric Modules</strong> harvest energy from movement. Simply walking with your phone or tapping the screen generates power.";
            }
            else if (m.includes('thermal') || m.includes('heat') || m.includes('thermo') || m.includes('warm')) {
                response = "The <strong>Thermoelectric Generator</strong> uses the heat difference between your phone and the air. It actually helps cool down your phone while charging it!";
            }

            // Commercial/Usage
            else if (m.includes('price') || m.includes('cost') || m.includes('buy') || m.includes('how much')) {
                response = "The standard ENERGYNEST case is <strong>$89</strong>. The Heavy Duty version is $99. You can place a pre-order on the Order page.";
            }
            else if (m.includes('compatible') || m.includes('phone') || m.includes('support') || m.includes('iphone') || m.includes('samsung')) {
                response = "We currently support: iPhone 13/14/15 series, Samsung Galaxy S23/S24 series, and Google Pixel 7/8. Select your model in the order form.";
            }
            else if (m.includes('safe') || m.includes('damage') || m.includes('battery') || m.includes('health')) {
                response = "Yes, it is 100% safe! Our <strong>Smart Power IC</strong> regulates voltage and prevents overcharging, actually extending your phone's battery health by providing stable trickle charging.";
            }
            else if (m.includes('charging') || m.includes('fast') || m.includes('speed') || m.includes('time')) {
                response = "This is a trickle-charging solution designed to keep your battery maintained throughout the day. It extends battery life by 30-50% rather than fast-charging from 0 to 100%.";
            }
            // Troubleshooting / Problems
            else if (m.includes('slow') || m.includes('stopped') || m.includes('issue') || m.includes('problem') || m.includes('not working')) {
                response = "<strong>Charging Issues?</strong> Check these factors:<br>1. <strong>Light:</strong> Solar needs direct light.<br>2. <strong>Noise:</strong> Acoustic needs sound/voice.<br>3. <strong>Toggle:</strong> Ensure the switch in the Battery tab is ON.<br><em>Note: This is a hybrid maintenance charger, not a fast charger.</em>";
            }
            else if (m.includes('hello') || m.includes('hi') || m.includes('hey')) {
                response = "Hello! I am ENERGYBOT. Ask me about Solar, Acoustic, or <strong>Charging Problems</strong>!";
            }

            botDiv.innerHTML = `
                <div style="background: var(--primary-color); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; color: #000;"><i class="fas fa-robot"></i></div>
                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 0 15px 15px 15px; max-width: 70%; line-height: 1.5;">${response}</div>
            `;
            history.appendChild(botDiv);
            history.scrollTop = history.scrollHeight;
        }, 800);
    }
}
