---
title: "Component::EnumSectionedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__EnumSectionedBodies.htm"
---

# Component::EnumSectionedBodies

This method is obsolete and has been superseded by [Component2::EnumSectionedBodies](sldworksAPI.chm::/Component2/Component2__EnumSectionedBodies.htm).

Description

This method gets the sectioned bodies seen in the specified view and returns them in an enumerated list. To determine if the desired model view is currently displaying a sectioned view, see ModelView::GetDisplayState.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Component->EnumSectionedBodies ( viewIn, &retval )

| Input: | (LPMODELVIEW) viewIn | Pointer to the model view object displaying the sectioned view |
| --- | --- | --- |
| Output: | (LPENUMBODIES) retval | Pointer to the enumerated list of bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you need the full body representation, use Component::GetBody or [PartDoc::Body](../PartDoc/PartDoc__Body.htm), which ignores the sectioning operation.

For Dispatch implementations, use [Component::GetSectionedBodies](Component__GetSectionedBodies.htm).

If a component is suppressed or lightweight, this method might return NULL because the component was not loaded into memory by SolidWorks. For more information on lightweight components, see Working With Lightweight Components.
