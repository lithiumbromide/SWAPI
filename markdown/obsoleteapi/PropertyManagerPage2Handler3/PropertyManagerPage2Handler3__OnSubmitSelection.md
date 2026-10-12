---
title: "PropertyManagerPage2Handler3::OnSubmitSelection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnSubmitSelection.htm"
---

# PropertyManagerPage2Handler3::OnSubmitSelection

This method is obsolete and has been superseded by [PropertyManagerPage2Handler4::OnSubmitSelection](../PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSubmitSelection.htm).

Description

This method is called when a selection is made. It allows the add-in to accept or reject the selection.

NOTE: If writing a VBA macro, then you must set this method to TRUE for the user to select something (see the example). If this method is not set to TRUE, then the user cannot select anything. This method is set to FALSE by default.

Syntax (OLE Automation)

retval = PropertyManagerPage2Handler3.OnSubmitSelection ( Id, Selection, SelType)

| Input: | (long) Id | ID of the active selection box, where this selection is being made |
| --- | --- | --- |
| Input: | (LPDISPATCH) Selection | Dispatch pointer to the object being selected |
| Input: | (long) SelType | Entity type of the selection as defined in swSelectType_e |
| Output: | (VARIANT_BOOL) retval | TRUE if the selection is accepted, FALSE if the selection is rejected |

Syntax (COM)

status = PropertyManagerPage2Handler3->OnSubmitSelection ( Id, Selection, SelType, &retval)

| Input: | (long) Id | ID of the active selection box, where this selection is being made |
| --- | --- | --- |
| Input: | (LPDISPATCH) Selection | Dispatch pointer to the object being selected |
| Input: | (long) SelType | Entity type of the selection as defined in swSelectType_e |
| Output: | (VARIANT_BOOL) retval | TRUE if the selection is accepted, FALSE if the selection is rejected |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is called by SolidWorks when an add-in has a PropertyManager page displayed and a selection is made that passes the selection filter criteria set up for a selection list box. The add-in can then:

1. Take the Dispatch pointer and the selection type.
2. QueryInterface the Dispatch pointer to get the specific interface.
3. Use APIs of that interface to determine if the selection should be allowed or not.

The add-in should not Release() the Dispatch pointer. SolidWorks will Release() the Dispatch pointer upon return from this method.

The method is called during the process of SolidWorks selection. It is neither a pre-notification nor post-notification. The add-in should not be taking any action that might affect the model or the selection list. The add-in should only be querying information and then returning TRUE/VARIANT_TRUE or FALSE/VARIANT_FALSE.
