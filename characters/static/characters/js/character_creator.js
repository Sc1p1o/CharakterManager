const skill_list = [
    'acrob',
    'aprs',
    'blf',
    'clb',
    'crft1',
    'crft2',
    'crft3',
    'dpl',
    'dad',
    'dsg',
    'esc',
    'fly',
    'han',
    'hel',
    'ind',
    'knl_arc',
    'knl_dun',
    'knl_eng',
    'knl_geo',
    'knl_his',
    'knl_loc',
    'knl_nat',
    'knl_nob',
    'knl_pla',
    'knl_rel',
    'lin',
    'prcep',
    'perf1',
    'perf2',
    'prof1',
    'prof2',
    'ride',
    'smot',
    'soh',
    'spell',
    'stl',
    'sur',
    'swim'
]


function calculateMod(attr) {
    const base = parseInt(document.getElementById(`attr_${attr}_base`).value) || 0;
    const race = parseInt(document.getElementById(`attr_${attr}_race`).value) || 0;
    const misc = parseInt(document.getElementById(`attr_${attr}_misc`).value) || 0;

    const total = base + race + misc;
    const mod = Math.floor((total - 10) / 2);

    const resultLabels = document.getElementsByClassName(`result_${attr}`);
    for (const element of resultLabels) {
        element.innerText = mod.toString();
    }

    for (const skill of skill_list){
        console.log("Testing now" + skill);
        calculateSkill(skill);
    }
}

function calculateSkill(skill) {
    const attr = parseInt(document.getElementById(`skill_${skill}_attr`).innerText) || 0;
    const ranks = parseInt(document.getElementById(`skill_${skill}_ranks`).value) || 0;
    const misc = parseInt(document.getElementById(`skill_${skill}_misc`).value) || 0;

    const is_class_skill = document.getElementById(`skill_${skill}_check`).checked;

    let class_skill = 0;

    if(is_class_skill && ranks > 0){
        class_skill = 5;
    }
    const mod = attr + ranks + misc + class_skill;

    const skill_result_element = document.getElementById(`skill_${skill}_result`);

    skill_result_element.innerText = mod.toString();
}