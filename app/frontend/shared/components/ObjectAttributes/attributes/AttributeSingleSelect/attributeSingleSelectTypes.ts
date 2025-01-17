// Copyright (C) 2012-2024 Zammad Foundation, https://zammad-foundation.org/

import type { ObjectAttribute } from '#shared/entities/object-attributes/types/store.ts'

export interface ObjectAttributeSingleSelect extends ObjectAttribute {
  dataType: 'select' | 'tree_select'
  dataOption: {
    historical_options: Record<string, string>
    linktemplate: string
    maxlength: number
    null: boolean
    nulloption: boolean
    relation: string
    permission?: string[]
    multiple: boolean
    filter?: number[] // ids
    only_shown_if_selectable?: boolean
    relation_condition?: { access?: 'full'; roles?: 'Agent' }
    // array for tree_select
    // irrelevant for displaying
    options: Record<string, string> | Record<string, string>[]
  }
}
