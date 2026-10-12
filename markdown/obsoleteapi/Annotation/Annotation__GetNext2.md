---
title: "Annotation::GetNext2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetNext2.htm"
---

# Annotation::GetNext2

This method is obsolete and has been superseded by [Annotation::GetNext3](sldworksAPI.chm::/Annotation/Annotation__GetNext3.htm).

#### Description

This method gets the next annotation.

#### Syntax (OLE Automation)

retval = Annotation.GetNext2 ()

| Return: | (LPDISPATCH) retval | Dispatch object of the next annotation |
| --- | --- | --- |

#### Syntax (COM)

status = Annotation->IGetNext2 ( &retval )

| Output: | (LPANNOTATION) retval | Pointer to the next annotation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method retrieves all display dimensions, including suppressed, hidden, and dangling dimensions, if the sheet format is visible. See Sheet::SheetFormatVisible.

SolidWorks suppresses or hides a dimension when you specifically select a dimension and hide it, or when you select a feature and hide all dimensions. If you need to filter out these dimensions, use Annotation::Visible to check that status.

SolidWorks returns the annotation even if it is on a layer that is not displayed.

If annotations or any specific type of annotations are not displayed, use ModelDoc2::GetUserPreferenceToggle to discover those situations.
