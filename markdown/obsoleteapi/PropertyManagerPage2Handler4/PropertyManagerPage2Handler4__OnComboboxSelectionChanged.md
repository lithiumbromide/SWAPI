---
title: "PropertyManagerPage2Handler4::OnComboboxSelectionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnComboboxSelectionChanged.htm"
---

# PropertyManagerPage2Handler4::OnComboboxSelectionChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnComboboxSelectionChanged.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnComboboxSelectionChanged.htm)

Description

This method is called when a user changes the selected item in a combo box on this PropertyManager.

Syntax (OLE Autom

void = PropertyManagerPage2Handler4.OnComboboxSelectionChanged ( Id, Item )

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnComboboxSelectionChanged ( Id, Item )

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the user can edit the text in the text box, then use this method with PropertyManagerPagew2Handler4::OnComboxEditChanged to find out what is in the text box of the combo box.

When this method is called, the control may not yet be updated with the current selection, so the PropertyManagerPageCombobox::CurrentSelection property is not reliable. To get the current text, use the value of Item that is passed into the method as the argument to PropertyManagerPageCombobox::ItemText.

If the user has edited the text in the text box and then clicks the arrow to show or hide the list box of the combo box, and the text in the text box matches the first characters in any of the items in the list, then that item is automatically selected in the list and this method is called, indicating that the selected item has changed.
