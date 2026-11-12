---
title: "ModelDoc::ForceRebuild3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ForceRebuild3.htm"
---

# ModelDoc::ForceRebuild3

This method is obsolete and has been superseded by [ModelDoc2::ForceRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ForceRebuild3.htm).

Description

This method forces a rebuild of the complete model.

Syntax (OLE Automation)

retval = ModelDoc.ForceRebuild3 ( topOnly )

| Input: | (VARIANT_BOOL) topOnly | TRUE rebuilds top-level assembly only; FALSE rebuilds the top-level and all subassemblies |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the rebuild was successful, FALSE if not |

Syntax (COM)

status = ModelDoc->ForceRebuild3 ( topOnly, &retval )

| Input: | (VARIANT_BOOL) topOnly | TRUE rebuilds top-level assembly only; FALSE rebuilds the top-level and all subassemblies |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the rebuild was successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
