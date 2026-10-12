---
title: "ModelDoc::SelectByMark"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectByMark.htm"
---

# ModelDoc::SelectByMark

This method is obsolete and has been superseded by [ModelDoc2::SelectByMark](../ModelDoc2/ModelDoc2__SelectByMark.htm).

Description

This method and ModelDoc::AndSelectByMark behave exactly the same as ModelDoc::SelectById and ModelDoc::AndSelectById, except that the former methods mark the selected entity with the integer mark provided as the last argument. This mark is used by API functions that require multiple selections.

Syntax (OLE Automation)

retval = ModelDoc.SelectByMark ( selID, selParams, x, y, z, mark)

| Input: | (BSTR) selID | ID of object; this case-sensitive string is intended for objects that are automatically named by SolidWorks during entity creation, such as dimensions and drawing views; if you do not know the object ID or if it is an item that is not automatically named by SolidWorks, you can pass an empty string |
| --- | --- | --- |
| Input: | (BSTR) selParams | Uppercase type name of object (for exmample, "EDGE"); see swSelectType_e for valid names; if you do not know the object type, you can pass in an empty string |
| Input: | (double) x | X selection location; values are in meters; in certain situations you can simply pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (double) y | Y selection location; values are in meters; in certain situations you can simply pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (double) z | Z selection location; values are in meters; in certain situations you can simply pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (long) mark | Number to use as a mark |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SelectByMark ( selID, selParams, x, y, z, mark, &retval )

| Input: | (BSTR) selID | ID of object; this case-sensitive string is intended for objects that are automatically named by SolidWorks during entity creation, such as dimensions and drawing views; if you do not know the object ID or if it is an item that is not automatically named by SolidWorks, you can pass an empty string |
| --- | --- | --- |
| Input: | (BSTR) selParams | Uppercase type name of object (for example, "EDGE"); see swSelectType_e for valid names; if you do not know the object type, you can pass in an empty string |
| Input: | (double) x | X selection location; values are in meters; in certain situations you can pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (double) y | Y selection location; values are in meters; in certain situations you can pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (double) z | Z selection location; values are in meters; in certain situations you can pass in ( 0,0,0 ); see ModelDoc::SelectByID for details |
| Input: | (long) mark | The number to use as a mark |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
