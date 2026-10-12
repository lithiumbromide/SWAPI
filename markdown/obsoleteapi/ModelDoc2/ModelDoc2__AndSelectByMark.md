---
title: "ModelDoc2::AndSelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AndSelectByMark.htm"
---

# ModelDoc2::AndSelectByMark

This method is obsolete and has been superseded by [ModelDocExtension::SelectByID](../ModelDocExtension/ModelDocExtension__SelectByID.htm).

Description

This method adds an object to the selections or removes it if it is already selected. The selection is added with a mark as required by certain API functions that use multiple selections, such as ModelDoc2::InsertMfDraft, ModelDoc2::InsertSplitLineSil, and ModelDoc2::InsertSplitLineProject.

Syntax (OLE Automation)

retval = ModelDoc2.AndSelectByMark ( selID, selParams, x, y, z, mark)

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Input: | (long) mark | Number you wish to use as a mark |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->AndSelectByMark ( selID, selParams, x, y, z, mark, &retval )

| Input: | (BSTR) selID | ID of object |
| --- | --- | --- |
| Input: | (BSTR) selParams | Type name of object |
| Input: | (double) x | X selection location |
| Input: | (double) y | Z selection location |
| Input: | (double) z | Z selection location |
| Input: | (long) mark | Number you wish to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method instead of using the individual selection methods on the following objects:

- Annotation
- Component2
- Feature
- SketchHatch
- SketchPoint
- SketchSegment

The previously listed objects' selection methods do not work well when a PropertyManager page is open or a command is running. This method, ModelDoc2::AndSelectByMark, handles selection correctly whether or not a command is running.

If you specify a mark, SolidWorks puts the selection into the selection list box that has that mark, regardless of whether it is active or not. If you do not specify a mark, SolidWorks puts the selection into the active selection list box. Keep in mind that the selection still has to pass the entity filtering criteria for that selection list box before SolidWorks adds it completely.

If you want SolidWorks to mark your entity, pass 0 as the mark argument.
