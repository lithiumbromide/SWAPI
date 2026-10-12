---
title: "PropertyManagerPage2Handler4::OnTextboxChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnTextboxChanged.htm"
---

# PropertyManagerPage2Handler4::OnTextboxChanged

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnTextboxChanged](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnTextboxChanged.htm).

Description

This method is called when a user changes the string in a text box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnTextboxChanged ( Id, Text )

| Input: | (long) Id | ID of text box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnTextboxChanged ( Id, Text )

| Input: | (long) Id | ID of text box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
