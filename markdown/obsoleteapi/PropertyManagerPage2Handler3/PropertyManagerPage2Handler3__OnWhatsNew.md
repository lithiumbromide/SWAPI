---
title: "PropertyManagerPage2Handler3::OnWhatsNew"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnWhatsNew.htm"
---

# PropertyManagerPage2Handler3::OnWhatsNew

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnWhatsNew](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnWhatsNew.htm).

Description

This method is called when a user clicks the What's New button on this PropertyManager page. Your add-in must implement this method.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnWhatsNew ()

Syntax (COM)

status = PropertyManagerPage2Handler3->OnWhatsNew ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

When a user clicks the What's New button on this PropertyManager page, the appropriate What's New Help topic is displayed. Use SldWorks::ShowHelp to display the What's New Help topic.
