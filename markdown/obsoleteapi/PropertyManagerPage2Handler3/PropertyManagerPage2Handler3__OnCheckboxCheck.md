---
title: "PropertyManagerPage2Handler3::OnCheckboxCheck"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnCheckboxCheck.htm"
---

# PropertyManagerPage2Handler3::OnCheckboxCheck

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnCheckboxCheck](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnCheckboxCheck.htm).

Description

This method is called when a user selects this check box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler3.OnCheckboxCheck ( Id, Checked )

| Input: | (long) Id | ID of this check box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the check box is selected, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnCheckboxCheck ( Id, Checked )

| Input: | (long) Id | ID of this check box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the check box is selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
