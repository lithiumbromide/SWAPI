---
title: "PropertyManagerPage2Handler::OnTextboxChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnTextboxChanged.htm"
---

# PropertyManagerPage2Handler::OnTextboxChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler2::OnTextboxChanged](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnTextboxChanged.htm).

Description

This method is called when the end-user changes the string in a text box in this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnTextboxChanged ( Id, Text )

| Input: | (long) Id | Textbox ID |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |

Syntax (COM)

status = PropertyManagerPage2Handler->OnTextboxChanged ( Id, Text )

| Input: | (long) Id | Textbox ID |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
