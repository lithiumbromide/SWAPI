---
title: "ModelDoc2::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SelectByMark.htm"
---

# ModelDoc2::SelectByMark

This method is obsolete and has been superseded by [ModelDocExtension::SelectByID](../ModelDocExtension/ModelDocExtension__SelectByID.htm).

Description

This method and ModelDoc2::AndSelectByMark behave exactly the same as the ModelDoc2::SelectById and ModelDoc2::AndSelectById, with the exception that this method also marks the selected entity with the integer mark provided as the last argument. This mark is used by certain API functions that require multiple selections.

Syntax (OLE Automation)

retval = ModelDoc2.SelectByMark ( selID, selParams, x, y, z, mark)

| Input: | (BSTR) selID | ID of object; this case-sensitive string is intended for objects that are automatically named by SolidWorks during entity creation, such as dimensions, drawing views, and so on; if you do not know the object ID or if it is an item that is not automatically named by SolidWorks, you can pass an empty string |
| --- | --- | --- |
| Input: | (BSTR) selParams | Uppercase type name of object (for example, "EDGE") as defined by swSelectType_e; if you do not know the object type, you can pass in an empty string |
| Input: | (double) x | X,Y,Z selection location; values are in meters; in certain situations you can simply pass in ( 0,0,0 ); see ModelDoc2::SelectByID for details |
| Input: | (double) y | See x argument |
| Input: | (double) z | See x argument |
| Input: | (long) mark | Number you want to use as a mark; this number is used by certain API functions that require ordered entity selection |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->SelectByMark ( selID, selParams, x, y, z, mark, &retval )

| Input: | (BSTR) selID | ID of object; this case-sensitive string is intended for objects that are automatically named by SolidWorks during entity creation, such as: dimensions, drawing views, and so on; if you do not know the object ID or if it is an item that is not automatically named by SolidWorks, you can pass an empty string |
| --- | --- | --- |
| Input: | (BSTR) selParams | Uppercase type name of object (for example, "EDGE") as defined by swSelectType_e; if you do not know the object type, you can pass in an empty string |
| Input: | (double) x | X,Y,Z selection location; values are in meters; in certain situations you can simply pass in ( 0,0,0 ); see ModelDoc2::SelectByID for details |
| Input: | (double) y | See x argument |
| Input: | (double) z | See x argument |
| Input: | (long) mark | Number you want to use as a mark; this number is used by certain API functions that require ordered entity selection |
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

The previously listed object's selection methods do not work well when a PropertyManager page is open or a command is running. This method, ModelDoc2::SelectByMark, handles selection correctly whether or not a command is running.

If you specify a mark, SolidWorks puts the selection into the selection list box that has that mark, regardless of whether it is active or not. If you do not specify a mark, SolidWorks puts the selection into the active selection list box. The selection still has to pass the entity filtering criteria for that selection list box before SolidWorks adds it completely.

If you want SolidWorks to mark your entity, pass 0 as the mark argument.
