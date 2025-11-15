import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const folders = ['base', 'shared'];
const componentsDir = path.resolve(__dirname, '../src/components/ui');
const outputJS = path.join(componentsDir, 'index.js');
const outputDTS = path.join(componentsDir, 'index.d.ts');
const aliasRoot = '@/components/ui';

let components = [];

function scanDir(dir, baseDir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            scanDir(fullPath, baseDir);
        } else if (entry.isFile() && entry.name.endsWith('.vue')) {
            const name = entry.name.replace('.vue', '');
            const rel = path.relative(baseDir, fullPath).replace(/\\/g, '/');
            const aliasPath = `${aliasRoot}/${rel}`;
            components.push({ name, aliasPath });
        }
    }
}

folders.forEach(folder => {
    const folderPath = path.join(componentsDir, folder);
    if (fs.existsSync(folderPath)) {
        scanDir(folderPath, componentsDir);
    }
});

let jsContent = '';
components.forEach(c => {
    jsContent += `import ${c.name} from '${c.aliasPath}';\n`;
});
jsContent += `\nexport {\n`;
components.forEach(c => {
    jsContent += `  ${c.name},\n`;
});
jsContent += '};\n';
fs.writeFileSync(outputJS, jsContent, 'utf-8');

let dtsContent = `declare module 'vue' {
  export interface GlobalComponents {
`;
components.forEach(c => {
    dtsContent += `    ${c.name}: typeof import('${c.aliasPath}')['default'];\n`;
});
dtsContent += `  }
}
export {};
`;
fs.writeFileSync(outputDTS, dtsContent, 'utf-8');

console.log('✅ UI index.js and index.d.ts generated!');
