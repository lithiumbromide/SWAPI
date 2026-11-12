---
title: "Component::Visible"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__Visible.htm"
---

# Component::Visible

This property is obsolete and has been superseded by [Component2::Visible](sldworksAPI.chm::/Component2/Component2__Visible.htm).

Description

This property gets the visibility state of this component.

Syntax (OLE Automation)

Visible = Component.Visible (VB Get property)

Visible = Component.GetVisible ( ) (C++ Get property)

| Property: | (long) Visible | Visibility state of this component instance as defined in swComponentVisibilityState_e |
| --- | --- | --- |

Syntax (COM)

status = Component->get_Visible( &Visible )

| Property: | (long) Visible | Visibility state of this component instance as defined in swComponentVisibilityState_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The functionality of this property is also available with the following ModelDoc methods:

- ModelDoc2::HideComponent2
- ModelDoc2::ShowComponent2
