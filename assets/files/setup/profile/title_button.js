// myapp/static/myapp/js/title_button.js
$(document).ready(function () {
    var componentName = $('#nav_component_name').val();

    // 'component_def' is defined in the 'title_button.html' file
    var componentMeta = null;
    componentMeta = component_def[componentName]

    // 'get_component_meta' reference
    var component = componentMeta;

    // Ignored obsolete code about creating page title and adding
    // it to the page 'buttonsSpan'

    // Create buttons
    var buttonsSpan = $('<span/>', {style: 'white-space:nowrap;'});

    if (component.buttons) {
        component.buttons.forEach(function (item) {
            button_str = title_button_def[item.split('|')[0]].template
            additional_attr = title_button_def[item.split('|')[0]].additional_attr
            button = $(button_str);

            if (additional_attr != undefined) {
                attrs = additional_attr.split(',');
                for (var i = 0; i < attrs.length; ++i) {
                    if (attrs[i].indexOf(':') > -1) {
                        key = attrs[i].split(':')[0];
                        value = attrs[i].split(':')[1];
                        if (value.indexOf('#') > -1 || value.indexOf('.') > -1) {
                            button.attr(key, $(value).val());
                        } else {
                            button.attr(key, value);
                        }
                    }
                }
            }
            buttonsSpan
                .append(button)
                .append("<span style='display: inline;'>&nbsp;</span>");
        });
    }
});