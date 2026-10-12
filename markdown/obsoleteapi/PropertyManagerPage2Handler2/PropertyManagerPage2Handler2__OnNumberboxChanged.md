---
title: "PropertyManagerPage2Handler2::OnNumberboxChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnNumberboxChanged.htm"
---

# PropertyManagerPage2Handler2::OnNumberboxChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler3::OnNumberboxChanged](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnNumberboxChanged.htm).

Description

This method when the end-user changes the value in a number box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler2.OnNumberboxChanged ( Id, Value )

| Input: | (long) Id | ID of number box |
| --- | --- | --- |
| Input: | (double) Value | Value |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnNumberboxChanged ( Id, Value )

| Input: | (long) Id | ID of number box |
| --- | --- | --- |
| Input: | (double) Value | Value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
