---
title: "PropertyManagerPage2Handler4::OnSelectionboxListChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSelectionboxListChanged.htm"
---

# PropertyManagerPage2Handler4::OnSelectionboxListChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnSelectionboxListChanged.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnSelectionboxListChanged.htm)

Description

This method is called when a user changes the selection list in a selection box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnSelectionboxListChanged ( Id, Count )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection box |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnSelectionboxListChanged ( Id, Count )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection box |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is called when your application uses a selection method, such as ModelDocExtension::SelectByID2, just as if the selection was made interactively.

The method is called during the process of SolidWorks selection. It is neither a pre-notification or post-notification. The add-in should not be taking any action that may affect the model or the selection list. The add-in should only be querying information, presumably about the state of selections to set up its own information correctly.

Regardless of how many items the user selects, this method is called only once per interactive box selection. In other words, if the user selects six faces using a box selection, this method is called only once.
