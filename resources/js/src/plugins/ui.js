const components = import.meta.glob(
    '@/components/ui/{base,shared}/**/*.vue',
    { eager: true }
);


//For IDE

let IDEComponents = {};
const ideModules = import.meta.glob('@/components/ui/index.js', { eager: true });
if (ideModules && ideModules['@/components/ui/index.js']) {
    IDEComponents = ideModules['@/components/ui/index.js'];
}



export default {
    install(app) {
        Object.entries(components).forEach(([modPath, mod]) => {
            const comp = mod.default;
            if (!comp) return;

            const compName = comp.name || modPath.split('/').pop().replace('.vue', '');
            app.component(compName, comp);
        });


        //For IDE
        if (IDEComponents && Object.keys(IDEComponents).length) {
            Object.values(IDEComponents).forEach(comp => {
                if (!comp.name) return;
                app.component(comp.name, comp);
            });
            console.log('generated IDE')
        }
    }
};
