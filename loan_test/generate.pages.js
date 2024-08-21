const fs = require('fs');
const path = require('path');

const template = fs.readFileSync('업체 상세 페이지/company-template.html', 'utf8');

for (let i = 1; i <= 50; i++) {
    const content = template.replace(/{{id}}/g, i);
    const filePath = path.join(__dirname, '업체 상세 페이지', `company${i}.html`);
    fs.writeFileSync(filePath, content, 'utf8');
}

console.log('Pages generated successfully!');
