$(document).ready(function () {
    var componentName = $('#nav_component_name').val();
    var pageIcons = $('.copo-page-icons'); // Profile component icons

    // 'component_def' is defined in the 'title_button.html' file
    var componentMeta = null;
    componentMeta = component_def[componentName]

    // 'get_component_meta' reference
    var component = componentMeta;

    // Ignored obsolete code about creating page title and adding
    // it to the page 'buttonsSpan'

    //Profile component buttons
    if (profile_type != undefined)  {
        var pcomponentHTML = $('.pcomponents-icons-templates')
          .clone()
          .removeClass('pcomponents-icons-templates');

        var pcomponentAnchor = pcomponentHTML
          .find('.pcomponents-anchor')
          .clone()
          .removeClass('pcomponents-anchor');

        pcomponentHTML.find('.pcomponents-anchor').remove();

        pageIcons.append(pcomponentHTML);

        //'get_profile_components' is defined in the 'component.html' file
        var components = get_profile_components(profile_type);

        for (var i = 0; i < components.length; ++i) {
            var comp = components[i];

            if (comp.component == component.component) {
              continue;
            }

            var newAnchor = pcomponentAnchor.clone();
            pcomponentHTML.append(newAnchor);

            newAnchor.attr('title', 'Navigate to ' + comp.title);
            newAnchor.attr('href',  comp.url.replace('999', profile_id));
            newAnchor.find('i').addClass(comp.color).addClass(comp.semanticIcon);

        }
   }
});