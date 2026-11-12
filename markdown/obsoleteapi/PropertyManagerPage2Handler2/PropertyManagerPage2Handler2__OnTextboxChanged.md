---
title: "PropertyManagerPage2Handler2::OnTextboxChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnTextboxChanged.htm"
---

# PropertyManagerPage2Handler2::OnTextboxChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler3::OnTextboxChanged](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnTextboxChanged.htm).

Description

This method is called when the end-user changes the string in a text box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler2.OnTextboxChanged ( Id, Text )

| Input: | (long) Id | ID of text box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnTextboxChanged ( Id, Text )

| Input: | (long) Id | ID of text box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
