---
title: "ModelDoc::ListExternalFileReferences"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ListExternalFileReferences.htm"
---

# ModelDoc::ListExternalFileReferences

This method is obsolete and has been superseded by [ModelDoc2::ListExternalFileReferences](../ModelDoc2/ModelDoc2__ListExternalFileReferences.htm).

Description

This method gets the names of the external file references on this model.

Syntax (OLE Automation)

retval = ModelDoc.ListExternalFileReferences ( useSearchRules )

| Input: | (BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Return: | (VARIANT) retval | Array of external references |

Syntax (COM)

status = ModelDoc->IListExternalFileReferences ( useSearchRules, numRefs, retval )

| Input: | (VARIANT_BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Input: | (long) numRefs | Number of external references |
| Output: | (BSTR) retval | Array of external references |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
