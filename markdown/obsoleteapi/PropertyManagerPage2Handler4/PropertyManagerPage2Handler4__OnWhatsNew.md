---
title: "PropertyManagerPage2Handler4::OnWhatsNew"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnWhatsNew.htm"
---

# PropertyManagerPage2Handler4::OnWhatsNew

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnWhatsNew.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnWhatsNew.htm)

Description

This method is called when a user clicks the What's New button on this PropertyManager page. Your add-in must implement this method.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnWhatsNew ()

Syntax (COM)

status = PropertyManagerPage2Handler4->OnWhatsNew ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

When a user clicks the What's New button on this PropertyManager page, the appropriate What's New Help topic is displayed. Use SldWorks::ShowHelp to display the What's New Help topic.
