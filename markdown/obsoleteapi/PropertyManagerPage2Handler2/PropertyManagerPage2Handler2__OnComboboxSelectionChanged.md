---
title: "PropertyManagerPage2Handler2::OnComboboxSelectionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnComboboxSelectionChanged.htm"
---

# PropertyManagerPage2Handler2::OnComboboxSelectionChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler3::OnComboboxSelectionChanged](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnComboboxSelectionChanged.htm).

Description

This method is called when the end-user changes the selected item in a combo box on this PropertyManager.

Syntax (OLE Autom

void = PropertyManagerPage2Handler2.OnComboboxSelectionChanged ( Id, Item )

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnComboboxSelectionChanged ( Id, Item )

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use this method with the PropertyManagerPagew2Handler2::OnComboxEditChanged method to find out what is in the text box of the combo box, if the user can edit the text in the text box.

When this method is called, the control may not yet be updated with the current selection, so the PropertyManagerPageCombobox::CurrentSelection property is not reliable. To get the current text, use the Item number that is passed into the method as the argument to the PropertyManagerPageCombobox::ItemText method.

If the end-user has edited the text in the text box and then presses the arrow to show or hide the list box in the combo box, and the text in the text box matches the first characters in any of the items in the list, then that item is automatically selected in the list and this method is called, indicating that the selected item has changed.
