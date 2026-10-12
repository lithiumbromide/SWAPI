---
title: "ModelDoc2::ListExternalFileReferencesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ListExternalFileReferencesCount.htm"
---

# ModelDoc2::ListExternalFileReferencesCount

This method is obsolete and has been superseded by [ModelDoc2::ListExternalFileReferencesCount2](ModelDoc2__ListExternalFileReferencesCount2.htm).

Description

This method gets the number of external file references on this model.

Syntax (OLE Automation)

retval = ModelDoc2.ListExternalFileReferencesCount ( useSearchRules )

| Input: | (BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Return: | (long) retval | Number of external references |

Syntax (COM)

status = ModelDoc2->ListExternalFileReferencesCount ( useSearchRules, &retval )

| Input: | (VARIANT_BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Output: | (long) retval | Number of external references |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use this method with ModelDoc2::ListExternalFileReferences to determine the array size required.
