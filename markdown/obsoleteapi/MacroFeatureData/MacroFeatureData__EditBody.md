---
title: "MacroFeatureData::EditBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MacroFeatureData/MacroFeatureData__EditBody.htm"
---

# MacroFeatureData::EditBody

This property is obsolete and has been superseded by [MacroFeatureData::EditBodies](sldworksAPI.chm::/MacroFeatureData/MacroFeatureData__EditBodies.htm), [MacroFeatureData::IGetEditBodies](sldworksAPI.chm::/MacroFeatureData/MacroFeatureData__IGetEditBodies.htm), and [MacroFeatureData::ISetEditBodies](sldworksAPI.chm::/MacroFeatureData/MacroFeatureData__ISetEditBodies.htm).

Description

This property gets or sets the body to be modified by this feature.

Syntax (OLE Automation)

editBody = MacroFeatureData.EditBody (VB Get property)

MacroFeatureData.EditBody = editBody (VB Set property)

editBody = MacroFeatureData.GetEditBody ( ) (C++ Get property)

MacroFeatureData.SetEditBody ( editBody ) (C++ Set property)

| Property: | (LPBODY2) editBody | Pointer to the body to edit |
| --- | --- | --- |

Syntax (COM)

status = MacroFeatureData->get_EditBody ( *editBody )

status = MacroFeatureData->put_EditBody ( editBody )

| Property: | (LPBODY2) editBody | Pointer to the body to edit |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Accessing Selections that Define Features for details on using this property.
