---
title: "PartDoc::InsertBasePart"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__InsertBasePart.htm"
---

# PartDoc::InsertBasePart

This method is obsolete and has been superseded by [PartDoc::InsertPart](PartDoc__InsertPart.htm).

Description

This method inserts a base part into this part document.

Syntax (OLE Automation)

retval = PartDoc.InsertBasePart ( fileName )

| Input: | (BSTR) fileName | Name of part file |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) *retval | TRUE if the part was inserted, FALSE if not |

Syntax (COM)

status = PartDoc->InsertBasePart ( fileName, retval )

| Input: | (BSTR) fileName | Name of part file |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) *retval | TRUE if the part was inserted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
