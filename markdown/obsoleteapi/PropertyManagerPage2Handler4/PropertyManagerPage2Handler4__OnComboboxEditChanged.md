---
title: "PropertyManagerPage2Handler4::OnComboboxEditChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnComboboxEditChanged.htm"
---

# PropertyManagerPage2Handler4::OnComboboxEditChanged

This method is obsolete and has been superseded by P[ropertyManagerPage2Handler5::OnComboboxEditChanged.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnComboboxEditChanged.htm)

Description

This method is called when a user changes the text string in the text box of a combo box.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnComboboxEditChanged ( Id, Text )

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnComboboxEditChanged ( Id, Text )

| Input: | (long) Id | ID of combo box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is only called if the combo box was set up as an editable text box. If the combo box is set up to as a static text box, then this method is not called.

If the user can edit the text in the text box, then use this method with PropertyManagerPage2Handler4::OnComboxSelectionChanged to find out what is in the text box of the combo box.

When this method is called, the control may not yet be updated with the current selection, so the PropertyManagerPageCombobox::CurrentSelection property is not reliable. The text passed into this method is the up-to-date text.
