---
title: "PropertyManagerPage2Handler4::OnPopupMenuItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnPopupMenuItem.htm"
---

# PropertyManagerPage2Handler4::OnPopupMenuItem

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnPopupMenuItem.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnPopupMenuItem.htm)

Description

When the user selects a pop-up menu item, this method determines which item was selected. The add-in should then perform the appropriate action.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnPopupMenuItem ( Id)

| Input: | (long) Id | Unique user-defined ID for a pop-up menu item (see PropertyManagerPage2::AddPopupMenuItem) |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnPopupMenuItem ( Id)

| Input: | (long) Id | Unique user-defined ID for a pop-up menu item (see PropertyManagerPage2::AddPopupMenuItem) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
