---
title: "View::Name"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__Name.htm"
---

# View::Name

This property is obsolete and has been superseded by [View::GetName2](sldworksAPI.chm::/View/View__GetName2.htm) and [View::SetName2](sldworksAPI.chm::/View/View__SetName2.htm).

Description

This property gets the name of this drawing view.

Syntax (OLE Automation)

name = View.Name (VB Get property)

name = View.GetName ( ) (C++ Get property)

| Property: | (BSTR) name | Name of this drawing view |
| --- | --- | --- |

Syntax (COM)

status = View->get_Name ( )

| Property: | (BSTR) name | Name of this drawing view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This value should match the view name that appears in the FeatureManager design tree of your drawing document.
