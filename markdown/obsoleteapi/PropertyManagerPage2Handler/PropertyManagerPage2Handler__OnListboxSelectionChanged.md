---
title: "PropertyManagerPage2Handler::OnListboxSelectionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnListboxSelectionChanged.htm"
---

# PropertyManagerPage2Handler::OnListboxSelectionChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnListboxSelectionChanged](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnListboxSelectionChanged.htm).

Description

This method is called when the end-user changes the selected item in a list box in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnListboxSelectionChanged ( Id, Item )

| Input: | (long) Id | List box ID |
| --- | --- | --- |
| Input: | (long) Item | Item ID |

Syntax (COM)

status = PropertyManagerPage2Handler->OnListboxSelectionChanged ( Id, Item )

| Input: | (long) Id | List box ID |
| --- | --- | --- |
| Input: | (long) Item | Item ID |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
