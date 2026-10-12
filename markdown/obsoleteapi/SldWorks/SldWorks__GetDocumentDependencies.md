---
title: "SldWorks::GetDocumentDependencies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__GetDocumentDependencies.htm"
---

# SldWorks::GetDocumentDependencies

This method is obsolete and has been superseded by [SldWorks::GetDocumentDependencies2](sldworksAPI.chm::/SldWorks/SldWorks__GetDocumentDependencies2.htm).

Description

This method gets all the model dependencies for a document. The document does not have to be open.

Syntax (OLE Automation)

retval = SldWorks.GetDocumentDependencies( docName, traverseflag, SearchFlag)

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies, FALSE to look where the documents were last saved |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; there are two strings for each document returned in this list of dependent files; the first is the file name and the second is the filename with the complete pathname; this combination repeats itself for each dependent file found for this ModelDoc2 |

Syntax (COM)

status = SldWorks->IGetDocumentDependencies(docName, traverseflag, SearchFlag, &retval)

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies, FALSE to look where the documents were last saved |
| Output: | (BSTR) retval | Array of strings; there are two strings for each document returned in this list of dependent files; the first is the file name and the second is the filename with the complete pathname; this combination repeats itself for each dependent file found for this ModelDoc2 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

As an example, calling this method on a drawing document returns a list of all the part, assemblies, or both, used in the drawing. If you set the traverseFlag to TRUE, then each of the parts within the assembly file are also returned in this array of strings.

Another example would be calling this method with a derived mirror part. Because a derived mirror part is generated from another part, the list of model dependencies returned by this method would include the original the part used to generate the derived mirror part.

Library features are unassociated. They do not require the library nor do they update when changes are made to the Library feature. Therefore, this method does not return Library features.

For the COM implementation, see SldWorks::GetDocumentDependenciesCount to determine the number of strings to be returned.

If you use this method with an assembly that contains two documents, Part1 and SubAssem1, an example of what might be returned is:

[ "Part1", "C:\temp\Part1.SLDPRT", "SubAssem1", "c:\temp\SubAssem1.SLDASM" ]

If traverseFlag is set to TRUE, then all the documents contained in SubAssem1.ASM would also be returned. Suppressed components are still recognized and returned by this method as a dependent file.

NOTE: If the SearchFlag is set to TRUE, then the current directory is set to the directory of the docName file. This replicates the interactive behavior of the References button in the File Open dialog window.
