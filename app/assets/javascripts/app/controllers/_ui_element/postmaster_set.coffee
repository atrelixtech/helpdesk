# coffeelint: disable=camel_case_classes
class App.UiElement.postmaster_set extends App.UiElement.ApplicationAction
  @defaults: (attribute) ->
    defaults = ['x-zammad-ticket-state_id']

    groups =
      ticket:
        name: __('Ticket creation')
        model: 'Ticket'
      'ticket-followup':
        name: __('Ticket update')
        model: 'Ticket'
      article:
        name: 'Article'
      expert:
        name: 'Expert'

    elements = {}
    for groupKey, groupMeta of groups
      if groupMeta.model
        for row in App[groupMeta.model].configure_attributes

          # ignore passwords and relations
          if row.type isnt 'password' && row.name.substr(row.name.length-4,4) isnt '_ids'

            # ignore readonly attributes
            if !row.readonly
              config = _.clone(row)

              switch config.tag
                when 'date'
                  config.operator = ['static', 'relative']
                when 'datetime'
                  config.operator = ['static', 'relative']
                when 'tag'
                  config.operator = ['add', 'remove']
                when 'autocompletion_ajax_external_data_source'
                  config.objectName = groupMeta.model
                  config.attributeName = config.name

              elements["x-zammad-#{groupKey}-#{config.name}"] = config

    elements['x-zammad-article-internal']  = _.clone(App.TicketArticle.attributesGet()['internal'])
    elements['x-zammad-article-internal'].null = false

    elements['x-zammad-article-type_id']   = _.clone(App.TicketArticle.attributesGet()['type_id'])
    elements['x-zammad-article-sender_id'] = _.clone(App.TicketArticle.attributesGet()['sender_id'])
    elements['x-zammad-ignore'] = { name: 'x-zammad-ignore', display: __('Ignore Message'), tag: 'boolean', type: 'boolean', null: false }

    [defaults, groups, elements]

  @elementKeyGroup: (elementKey) ->
    return 'expert' if elementKey is 'x-zammad-ignore'
    return 'ticket-followup' if elementKey.startsWith('x-zammad-ticket-followup')
    elementKey.replace('x-zammad-', '').split(/-/)[0]
