---
title: "PropertyManagerPage2Handler4::OnCheckboxCheck"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnCheckboxCheck.htm"
---

# PropertyManagerPage2Handler4::OnCheckboxCheck

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnCheckboxCheck](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnCheckboxCheck.htm).

Description

This method is called when a user selects this check box on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnCheckboxCheck ( Id, Checked )

| Input: | (long) Id | ID of this check box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the check box is selected, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnCheckboxCheck ( Id, Checked )

| Input: | (long) Id | ID of this check box |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Checked | TRUE if the check box is selected, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
