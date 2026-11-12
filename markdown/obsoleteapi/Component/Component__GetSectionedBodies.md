---
title: "Component::GetSectionedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetSectionedBodies.htm"
---

# Component::GetSectionedBodies

This method is obsolete and has been superseded by [Component2::GetSectionedBodies](sldworksAPI.chm::/Component2/Component2__GetSectionedBodies.htm).

Description

This method gets the sectioned bodies seen in the specified view and returns them as a SafeArray of Dispatch pointers to each individual Body object.

Syntax (OLE Automation)

retval = Component.GetSectionedBodies ( viewIn)

| Input: | (LPDISPATCH) viewIn | Dispatch pointer to the model view object displaying the sectioned view |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of Dispatch pointers to the sectioned bodies in the specified view |

Syntax (COM)

status = Component->GetSectionedBodies ( viewIn, &retval )

| Input: | (LPDISPATCH) viewIn | Dispatch pointer to the model view object displaying the sectioned view |
| --- | --- | --- |
| Output: | (VARIANT) retval | VARIANT of type SafeArray of Dispatch pointers to the sectioned bodies in the specified view |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To determine if the desired model view is currently displaying a sectioned view, use ModelView::GetDisplayState.

If you need the full body representation, use Component::GetBody or PartDoc::Body, which ignore the sectioning operation.

For COM implementations, refer to Component::EnumSectionedBodies.

If a component is suppressed or lightweight, this method might return NULL because the component is loaded into memory. For more information on lightweight components, refer to Working With Lightweight Components.
