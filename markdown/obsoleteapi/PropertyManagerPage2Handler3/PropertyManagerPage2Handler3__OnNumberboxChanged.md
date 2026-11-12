---
title: "PropertyManagerPage2Handler3::OnNumberboxChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnNumberboxChanged.htm"
---

# PropertyManagerPage2Handler3::OnNumberboxChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnNumberboxChanged](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnNumberboxChanged.htm).

Description

This method is called when a user changes the value in a number box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnNumberboxChanged ( Id, Value )

| Input: | (long) Id | ID of number box |
| --- | --- | --- |
| Input: | (double) Value | Value |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnNumberboxChanged ( Id, Value )

| Input: | (long) Id | ID of number box |
| --- | --- | --- |
| Input: | (double) Value | Value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
