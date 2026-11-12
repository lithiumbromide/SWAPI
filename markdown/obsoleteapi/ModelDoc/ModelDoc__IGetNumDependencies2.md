---
title: "ModelDoc::IGetNumDependencies2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IGetNumDependencies2.htm"
---

# ModelDoc::IGetNumDependencies2

This method is obsolete and has been superseded by [ModelDoc2::IGetNumDependencies2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IGetNumDependencies2.htm).

Description

This method gets the number of dependencies for the model.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = ModelDoc->IGetNumDependencies2 ( traverseFlag, searchFlag, addReadOnlyInfo, &retval )

| Input: | (VARIANT_BOOL) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) searchflag | TRUE if you wish to apply the current search criteria, FALSE if you want to return the dependent file information as it was stored |
| Input: | (VARIANT_BOOL) addReadOnlyInfo | TRUE if you wish to obtain read-only information with each dependent file |
| Output: | (long*) retval | Number of strings that will be returned by ModelDoc::GetDependencies2 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
