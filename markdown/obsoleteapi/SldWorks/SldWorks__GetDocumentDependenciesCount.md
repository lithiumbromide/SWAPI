---
title: "SldWorks::GetDocumentDependenciesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__GetDocumentDependenciesCount.htm"
---

# SldWorks::GetDocumentDependenciesCount

This method is obsolete and has been superseded by [SldWorks::IGetDocumentDependenciesCount2](sldworksAPI.chm::/SldWorks/SldWorks__IGetDocumentDependenciesCount2.htm).

Description

This method determines the number of strings returned by the SldWorks::GetDocumentDependencies method.

Syntax (OLE Automation)

retval = SldWorks.GetDocumentDependenciesCount( docName, traverseflag, SearchFlag )

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies, FALSE to search where the documents were last saved |
| Return: | (long) retval | Number of strings returned by SldWorks::GetDocumentDependencies |

Syntax (COM)

status = SldWorks->GetDocumentDependenciesCount(docName, traverseflag, SearchFlag, &retval)

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies, FALSE to search where the documents were last saved |
| Output: | (long) retval | Number of strings returned by SldWorks::GetDocumentDependencies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the SearchFlag is set to TRUE then the current directory is set to the directory of the docName file. This replicates the interactive behavior of the References button in the File Open dialog window.

For a complete description of this function and its arguments, see SldWorks::GetDocumentDependencies.
