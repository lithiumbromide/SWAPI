---
title: "ModelDoc::GetNumDependencies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetNumDependencies.htm"
---

# ModelDoc::GetNumDependencies

This method is obsolete and has been superseded by [ModelDoc::IGetNumDependencies2](ModelDoc__IGetNumDependencies2.htm).

Description

This method determines the number of strings returned by ModelDoc::GetDependencies.

Syntax (OLE Automation)

retval = ModelDoc.GetNumDependencies ( traverseflag, searchflag)

| Input: | (long) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (long) searchflag | TRUE if you wish to apply the current search criteria, FALSE if you want to return the dependent file information as it was stored |
| Return: | (long) retval | Number of strings returned by ModelDoc::GetDependencies2 |

Syntax (COM)

status = ModelDoc->IGetNumDependencies ( traverseflag, searchflag, &retval )

| Input: | (long) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (long) searchflag | TRUE if you wish to apply the current search criteria, FALSE if you want to return the dependent file information as it was stored |
| Output: | (long) retval | Number of strings returned by ModelDoc::GetDependencies2 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
