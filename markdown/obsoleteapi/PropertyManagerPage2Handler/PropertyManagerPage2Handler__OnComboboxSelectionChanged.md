---
title: "PropertyManagerPage2Handler::OnComboboxSelectionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnComboboxSelectionChanged.htm"
---

# PropertyManagerPage2Handler::OnComboboxSelectionChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnComboboxSelectionChanged](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnComboboxSelectionChanged.htm).

Description

This method is called when the end-user changes the selected item in a combo box in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnComboboxSelectionChanged ( Id, Item )

| Input: | (long) Id | Combobox ID |
| --- | --- | --- |
| Input: | (long) Item | Item ID |

Syntax (COM)

status = PropertyManagerPage2Handler->OnComboboxSelectionChanged ( Id, Item )

| Input: | (long) Id | Combobox ID |
| --- | --- | --- |
| Input: | (long) Item | Item ID |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
