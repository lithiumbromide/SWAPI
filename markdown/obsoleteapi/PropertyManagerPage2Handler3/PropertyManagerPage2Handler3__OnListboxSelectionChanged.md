---
title: "PropertyManagerPage2Handler3::OnListboxSelectionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnListboxSelectionChanged.htm"
---

# PropertyManagerPage2Handler3::OnListboxSelectionChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnListboxSelectionChanged](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnListboxSelectionChanged.htm).

Description

This method is called when a user changes the selected item in a list box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnListboxSelectionChanged ( Id, Item )

| Input: | (long) Id | ID of the list box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnListboxSelectionChanged ( Id, Item )

| Input: | (long) Id | ID of the list box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
