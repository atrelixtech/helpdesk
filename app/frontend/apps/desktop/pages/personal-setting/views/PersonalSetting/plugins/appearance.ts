// Copyright (C) 2012-2024 Zammad Foundation, https://zammad-foundation.org/

import type { PersonalSettingPlugin } from '../../../components/PersonalSettingSidebar/types.ts'

export default <PersonalSettingPlugin>{
  label: __('Appearance'),
  category: {
    label: __('Profile'),
    order: 1000,
  },
  route: {
    path: 'appearance',
    alias: '',
    name: 'PersonalSettingAppearance',
    component: () => import('../../PersonalSettingAppearance.vue'),
    level: 2,
    meta: {
      title: __('Appearance'),
      requiresAuth: true,
      requiredPermission: 'user_preferences.appearance',
    },
  },
  order: 1000,
  keywords: __('theme,color,style,dark mode,night mode,light mode'),
}
