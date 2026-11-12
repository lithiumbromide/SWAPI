---
title: "ModelDoc2::AndSelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AndSelectByID.htm"
---

# ModelDoc2::AndSelectByID

This method is obsolete and has been superseded by [ModelDocExtension::SelectByID](../ModelDocExtension/ModelDocExtension__SelectByID.htm).

Description

This methods adds an object to the list of selected items or removes it if it is already selected. For a full description of selection and the arguments, see ModelDoc2::SelectByID.

Syntax (OLE Automation)

retval = ModelDoc2.AndSelectByID ( selID, selParams, x, y, z)

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Y selection location |
| Input: | (double) z | Z selection location |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE if not |

Syntax (COM)

status = ModelDoc2->AndSelectByID ( selID, selParams, x, y, z, &retval )

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object (uppercase) |
| Input: | (double) x | X selection location |
| Input: | (double) y | Y selection location |
| Input: | (double) z | Z selection location |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method instead of using the individual selection methods on the following objects:

- Annotation
- Component2
- Feature
- SketchHatch
- SketchPoint
- SketchSegment

The previously listed objects' selection methods do not work well when a PropertyManager page is open or a command is running. This method, ModelDoc2::AndSelectByID, handles selection correctly whether or not a command is running.
