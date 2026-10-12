---
title: "ModelDoc2::ListExternalFileReferences"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ListExternalFileReferences.htm"
---

# ModelDoc2::ListExternalFileReferences

This method is obsolete and has been superseded by [ModelDoc2::ListExternalFileReferences2](ModelDoc2__ListExternalFileReferences2.htm).

Description

This method gets the names of the external file references on this model.

Syntax (OLE Automation)

void ModelDoc2.IListExternalFileReferences ( useSearchRules, numRefs, retval )

| Input: | (VARIANT_BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Input: | (long) numRefs | Number of external references |
| Output: | (BSTR&) retval | Array of external references |
| Return: | (HRESULT) status | S_OK if Successful |

Syntax (COM)

status = ModelDoc2->IListExternalFileReferences ( useSearchRules, numRefs, retval )

| Input: | (VARIANT_BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Input: | (long) numRefs | Number of external references |
| Output: | (BSTR&) retval | Array of external references |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
