---
title: "PropertyManagerPage2Handler3::OnGroupCheck"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnGroupCheck.htm"
---

# PropertyManagerPage2Handler3::OnGroupCheck

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnGroupCheck](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnGroupCheck.htm).

Description

This method is called when a user selects the check box in the title of a group box on a PropertyManager page.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnGroupCheck ( Id, Checked )

| Input: | (long) Id | Resource ID of the check box in title of the group box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the check box in the title of the group box is selected, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnGroupCheck ( Id, Checked )

| Input: | (long) Id | Resource ID of the check box in the title of the group box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the check box in the title of the group box is selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
