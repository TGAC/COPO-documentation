// record_action_button.js
var visualizeURL = '/myapp/visualize/';
var server_side_select = {}; //holds selected ids for table data - needed in server-side processing

$(document).ready(function () {
    var componentName = $('#nav_component_name').val();

    // 'component_def' is defined in the 'record_action_button.html' file
    var componentMeta = null;
    componentMeta = component_def[componentName]

    do_render_server_side_table(componentMeta);
});

function place_task_buttons(componentMeta) {
  //place custom buttons on table
  var is_custom_buttons_needed = false;

  var customButtons = $('<span/>', {
    style: 'padding-left: 15px;',
    class: 'copo-table-cbuttons',
  });

  if (componentMeta.recordActions.length) {
    componentMeta.recordActions.forEach(function (item) {
      button_str = record_action_button_def[item].template
      var actionBTN = $(button_str);
      /*
      var actionBTN = $('.record-action-templates')
        .find('.' + item)
        .clone();
      */
      actionBTN.removeClass(item);
      actionBTN.attr('data-table', componentMeta.tableID);
      customButtons.append(actionBTN);
    });
    is_custom_buttons_needed = true;
  }



 $('.components_custom_templates').find('.record-action-custom-template').each(function () {
    var actionBTN = $(this).clone();
    actionBTN.removeClass('record-action-custom-template');
    customButtons.append(actionBTN);
    is_custom_buttons_needed = true;
 }) ;

 if (is_custom_buttons_needed) {
  var table = $('#' + componentMeta.tableID).DataTable();
  $(table.buttons().container()).append(customButtons);
  refresh_tool_tips();
  //table action buttons
  do_table_buttons_events();
 }
}

function do_table_buttons_events_server_side(component) {
  //attaches events to table buttons - server-side processing version to function with similar name

  $(document)
    .off('click', '.copo-dt')
    .on('click', '.copo-dt', function (event) {
      event.preventDefault();

      $('.copo-dt').webuiPopover('destroy');

      var elem = $(this);
      var task = elem.attr('data-action').toLowerCase(); //action to be performed e.g., 'Edit', 'Delete'
      var tableID = elem.attr('data-table'); //get target table
      var btntype = elem.attr('data-btntype'); //type of button: single, multi, all
      var title = elem.find('.action-label').html();
      var message = elem.attr('data-error-message');

      if (!title) {
        title = 'Record action';
      }

      if (!message) {
        message = 'No records selected for ' + title + ' action';
      }

      //validate event before passing to handler
      var selectedRows = server_side_select[component].length;

      var triggerEvent = true;

      //do button type validation based on the number of records selected
      if (btntype == 'single' || btntype == 'multi') {
        if (selectedRows == 0) {
          triggerEvent = false;
        } else if (selectedRows > 1 && btntype == 'single') {
          //sort out 'single record buttons'
          triggerEvent = false;
        }
      }

      if (triggerEvent) {
        //trigger button event, else deal with error
        var event = jQuery.Event('addbuttonevents');
        event.tableID = tableID;
        event.task = task;
        event.title = title;
        $('body').trigger(event);
      } else {
        //alert user
        button_event_alert(title, message);
      }
    });
}

function do_render_server_side_table(componentMeta) {
  // Use this function for server-side processing of large tables
  var csrftoken = $.cookie('csrftoken');

  try {
    componentMeta.table_columns = JSON.parse($('#table_columns').val());
  } catch (err) {}

  var tableID = componentMeta.tableID;
  var component = componentMeta.component;

  var columnDefs = [];
  var table = null;

  if ($.fn.dataTable.isDataTable('#' + tableID)) {
    // get table instance
    table = $('#' + tableID).DataTable();
  }

  if (table) {
    //if table instance already exists, refresh
    table.draw();
  }
  else {
    server_side_select[component] = [];

    table = $('#' + tableID).DataTable({
      paging: true,
      processing: true,
      serverSide: true,
      searchDelay: 850,
      columns: componentMeta.table_columns,
      ajax: {
        url: visualizeURL,
        type: 'POST',
        headers: {
          'X-CSRFToken': csrftoken,
        },
        data: {
          task: 'server_side_table_data',
          component: component,
        },
        dataFilter: function (data) {
          var json = jQuery.parseJSON(data);
          json.recordsTotal = json.records_total;
          json.recordsFiltered = json.records_filtered;
          json.data = json.data_set;

          return JSON.stringify(json); // return JSON string
        },
      },
      rowCallback: function (row, data) {
        if ($.inArray(data.DT_RowId, server_side_select[component]) !== -1) {
          $(row).addClass('selected');
        }
      },
      createdRow: function (row, data, index) {
      },
      fnDrawCallback: function () {
      },
      buttons: [
        {
          text: 'Select visible records',
          action: function (e, dt, node, config) {
            //remove custom select info
            $('#' + tableID + '_info')
              .find('.select-item-1')
              .remove();

            dt.rows().select();
            var selectedRows = table.rows('.selected').ids().toArray();

            for (var i = 0; i < selectedRows.length; ++i) {
              var index = $.inArray(
                selectedRows[i],
                server_side_select[component]
              );

              if (index === -1) {
                server_side_select[component].push(selectedRows[i]);
              }
            }

            $('#' + tableID + '_info')
              .find('.select-row-message')
              .html(server_side_select[component].length + ' records selected');
          },
        },
        {
          text: 'Clear selection',
          action: function (e, dt, node, config) {
            dt.rows().deselect();
            server_side_select[component] = [];
            $('#' + tableID + '_info')
              .find('.select-item-1')
              .remove();
          },
        },
      ],
      columnDefs: columnDefs,
      language: {
        select: {
          rows: {
            _: "<span class='select-row-message'>%d records selected</span>",
            0: '',
            1: '%d record selected',
          },
        },
        processing: "<div class='copo-i-loader'></div>",
      },
      dom: 'Bfr<"row"><"row info-rw" i>tlp',
    });

    table
      .buttons()
      .nodes()
      .each(function (value) {
        $(this).removeClass('btn btn-default').addClass('tiny ui button');
      });

    place_task_buttons(componentMeta); //this will place custom buttons on the table for executing tasks on records

    do_table_buttons_events_server_side(component);

     table.on('click', 'tr >td', function () {
      var classList = [
        'annotate-datafile',
        'summary-details-control',
        'detail-hover-message',
      ]; //don't select on columns with these classes
      var foundClass = false;

      var tdList = this.className.split(' ');

      for (var i = 0; i < tdList.length; ++i) {
        if ($.inArray(tdList[i], classList) > -1) {
          foundClass = true;
          break;
        }
      }

      if (foundClass) {
        return false;
      }

      var elem = $(this).closest('tr');

      var id = elem.attr('id');
      var index = $.inArray(id, server_side_select[component]);

      if (index === -1) {
        server_side_select[component].push(id);
      } else {
        server_side_select[component].splice(index, 1);
      }

      elem.toggleClass('selected');

      //selected message
      $('#' + tableID + '_info')
        .find('.select-item-1')
        .remove();
      var message = '';

      if ($('#' + tableID + '_info').find('.select-row-message').length) {
        if (server_side_select[component].length > 0) {
          message = server_side_select[component].length + ' records selected';
          if (server_side_select[component].length == 1) {
            message = server_side_select[component].length + ' record selected';
          }

          $('#' + tableID + '_info')
            .find('.select-row-message')
            .html(message);
        } else {
          $('#' + tableID + '_info')
            .find('.select-row-message')
            .html('');
        }
      } else {
        if (server_side_select[component].length > 0) {
          message = server_side_select[component].length + ' records selected';
          if (server_side_select[component].length == 1) {
            message = server_side_select[component].length + ' record selected';
          }
          $('#' + tableID + '_info').append(
            "<span class='select-item select-item-1'>" + message + '</span>'
          );
        }
      }
    });
  }

  let table_wrapper = $('#' + tableID + '_wrapper');

  table_wrapper.find('.dt-buttons').css({ float: 'right' });

  table_wrapper
    .find('.dataTables_filter')
    .find('label')
    .css({ padding: '10px 0' })
    .find('input')
    .removeClass('input-sm')
    .attr('placeholder', 'Search ' + componentMeta.title)
    .attr('size', 30);

  $('<br><br>').insertAfter(table_wrapper.find('.dt-buttons'));

  //handle event for table details

  //handle event for annotation of datafile

} //end of func
