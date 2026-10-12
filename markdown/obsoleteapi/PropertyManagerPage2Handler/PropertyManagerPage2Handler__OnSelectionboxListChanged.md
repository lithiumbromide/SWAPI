---
title: "PropertyManagerPage2Handler::OnSelectionboxListChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnSelectionboxListChanged.htm"
---

# PropertyManagerPage2Handler::OnSelectionboxListChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnSelectionboxChanged](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnSelectionboxListChanged.htm).

Description

This method is called when the end-user changes the selection list in a selection list box in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnSelectionboxListChanged ( Id, Count )

| Input: | (long) Id | Selection box ID |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection list box |

Syntax (COM)

status = PropertyManagerPage2Handler->OnSelectionboxListChanged ( Id, Count )

| Input: | (long) Id | Selection box ID |
| --- | --- | --- |
| Input: | (long) Count | Number of items in this selection list box |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is called when your application uses a selection method, such as ModelDocExtension::SelectByID, just as if the selection was made interactively.

An interactive box selection causes this handler to be called once, regardless of how many items the user selected. In other words, if your box selection causes six faces to be selected, you will get only one call to this handler.
