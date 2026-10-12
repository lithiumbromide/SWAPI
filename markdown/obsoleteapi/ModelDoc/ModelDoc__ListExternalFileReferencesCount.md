---
title: "ModelDoc::ListExternalFileReferencesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ListExternalFileReferencesCount.htm"
---

# ModelDoc::ListExternalFileReferencesCount

This method is obsolete and has been superseded by [ModelDoc2::ListExternalFileReferencesCount](../ModelDoc2/ModelDoc2__ListExternalFileReferencesCount.htm).

Description

This method gets the number of external file references on this model. Use this method with ModelDoc.ListExternalFileReferences to determine the array size required.

Syntax (OLE Automation)

retval = ModelDoc.ListExternalFileReferencesCount ( useSearchRules )

| Input: | (BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Return: | (long) retval | Number of external references |

Syntax (COM)

status = ModelDoc->ListExternalFileReferencesCount ( useSearchRules, &retval )

| Input: | (VARIANT_BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Output: | (long) retval | Number of external references |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
