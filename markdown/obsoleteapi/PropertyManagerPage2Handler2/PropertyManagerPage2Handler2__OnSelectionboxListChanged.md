---
title: "PropertyManagerPage2Handler2::OnSelectionboxListChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnSelectionboxListChanged.htm"
---

# PropertyManagerPage2Handler2::OnSelectionboxListChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler3::OnSelectionboxListChanged](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnSelectionboxListChanged.htm).

Description

This method is called when the end-user changes the selection list in a selection box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler2.OnSelectionboxListChanged ( Id, Count )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection box |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnSelectionboxListChanged ( Id, Count )

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection box |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is called when your application uses a selection method, such as ModelDocExtension::SelectByID2, just as if the selection was made interactively.

Regardless of how many items the end-user selects, this method is called only once per interactive box selection. In other words, if the end-user selects six faces using a box selection, this method is called only once.
