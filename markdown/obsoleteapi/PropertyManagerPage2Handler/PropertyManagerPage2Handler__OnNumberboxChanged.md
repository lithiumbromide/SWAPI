---
title: "PropertyManagerPage2Handler::OnNumberboxChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnNumberboxChanged.htm"
---

# PropertyManagerPage2Handler::OnNumberboxChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnNumberboxChanged](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnNumberboxChanged.htm).

Description

This method is called when the end-user changes the value in a number box in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnNumberboxChanged ( Id, Value )

| Input: | (long) Id | Numberbox ID |
| --- | --- | --- |
| Input: | (double) Value | Item ID |

Syntax (COM)

status = PropertyManagerPage2Handler->OnNumberboxChanged ( Id, Value )

| Input: | (long) Id | Numberbox ID |
| --- | --- | --- |
| Input: | (double) Value | Item ID |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
