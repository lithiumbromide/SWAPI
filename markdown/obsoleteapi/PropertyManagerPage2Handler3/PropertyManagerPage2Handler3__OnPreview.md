---
title: "PropertyManagerPage2Handler3::OnPreview"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnPreview.htm"
---

# PropertyManagerPage2Handler3::OnPreview

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnPreview](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnPreview.htm).

Description

This method is called when a user clicks the Preview button on a PropertyManager page.

Syntax (OLE Automation)

retval = PropertyManagerPage2Handler3.OnPreview ()

| Output: | (VARIANT_BOOL) retval | TRUE if the operations specified by your add-in executes, FALSE if not (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnPreview ( &retval)

| Output: | (VARIANT_BOOL) retval | TRUE if the operations specified by your add-in executes, FALSE if not (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To show a Preview button on a PropertyManager page, include swPropertyManagerOptions_PreviewButton in the Options argument of SldWorks::CreatePropertyManagerPage.

You can do whatever you want in response to the Preview button being clicked. Your add-in is responsible for preview handling, including keeping track of the state of the Preview button. Your add-in controls what happens when the Preview button is clicked; SolidWorks takes not action when the Preview button is clicked.
