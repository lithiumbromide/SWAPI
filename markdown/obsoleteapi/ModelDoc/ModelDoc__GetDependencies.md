---
title: "ModelDoc::GetDependencies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetDependencies.htm"
---

# ModelDoc::GetDependencies

This method is obsolete and has been superseded by [ModelDoc::GetDependencies2](ModelDoc__GetDependencies2.htm).

Description

This method gets all of the model's dependencies.

Syntax (OLE Automation)

retval = ModelDoc.GetDependencies ( traverseflag, Unused)

| Input: | (long) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (long) SearchFlag | TRUE if you wish to use the search rules to find dependencies, FALSE looks where the documents were last saved |
| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; there are two strings for each document returned in this list of dependent files; the first is the file name and the second is the filename with the complete path name; this combination repeats itself for each dependent file found for this ModelDoc |

Syntax (COM)

status = ModelDoc->IGetDependencies ( traverseflag, Unused, &retval )

| Input: | (long) traverseflag | TRUE if you wish to traverse down into all dependent files, FALSE if you want only the highest level within the dependencies |
| --- | --- | --- |
| Input: | (long) SearchFlag | TRUE if you wish to use the search rules to find dependencies, FALSE looks where the documents were last saved |
| Output: | (BSTR) retval | Array of strings; there are two strings for each document returned in this list of dependent files; the first is the file name and the second is the filename with the complete path name; this combination repeats itself for each dependent file found for this ModelDoc |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Calling this method on a drawing document returns a list of all the part and assemblies used in the drawing. If you set the traverseFlag to TRUE, then each of the parts within the assembly file are also returned in this array of strings.

Because a derived mirror part is generated from another part, the list of model dependencies returned by this method would include the original configuration the part used to generate the derived mirror part.

Library features are completely unassociated. They do not require the library nor do they update when changes are made to the library feature. Therefore, this method does not return library features.

For the COM implementation, call ModelDoc::GetNumDependencies first to determine the number of strings to be returned.

If you use this methodwith an assembly that contains two documents, Part1 and SubAssem1, an example of what might be returned is:

[ "Part1", "C:\temp\Part1.SLDPRT", "SubAssem1", "c:\temp\SubAssem1.SLDASM" ]

If traverseFlag is set to TRUE, then all of the documents contained in SubAssem1.ASM are also returned. Suppressed components are still recognized and returned by this method as a dependent file.

NOTE: The return value for file references for assemblies containing suppressed or lightweight components point to the as-saved component reference because the actual component is not loaded into memory. Because the suppressed and lightweight components are not actually loaded, SolidWorks does not apply current search criteria to update the file references. Setting the SearchFlag argument to TRUE vs. FALSE, causes this method to apply the current search criteria rules to locate the particular reference and may result in a different return value. Likewise, unsuppressing or resolving these components causes SolidWorks to apply the current search criteria and update the assembly's component references in memory, if necessary.

When calling this method with the seachFlag argument set to TRUE, you may want to explicitly set the search folders first. This is important because this method uses the current SolidWorks directory as its second search criteria. Because the user may have interactively opened files from some random directory, you cannot be certain that the current SolidWorks directory is pointing at the desired location. You may want to set the search folders to that of the document used. For example:

// Get the current search folder settings so we can reset them later

VARIANT_BOOL currentSearchFolderSetting = FALSE;

BSTR currentSearchFolders = NULL;

hres = TheApplication->m_pSldWorks->GetUserPreferenceToggle ( swUseFolderSearchRules, ¤tSearchFolderSetting );

hres = TheApplication->m_pSldWorks->GetSearchFolders ( swDocumentType, ¤tSearchFolders );

```vb
// Set the search folders to use the path of the document
 BSTR bdocName;
 hres = pModelDoc->GetPathName(&bdocName);
 CString docName(bdocName);

 VARIANT_BOOL ok = FALSE;
 CString searchFolder = getFileLocation(docName); // Function to extract directory from full filename
 hres = TheApplication->m_pSldWorks->SetSearchFolders ( swDocumentType, au2B(searchFolder), &ok );

// Reset search folders to previous values
 hres = TheApplication->m_pSldWorks->SetUserPreferenceToggle ( swUseFolderSearchRules, currentSearchFolderSetting );
 hres = TheApplication->m_pSldWorks->SetSearchFolders ( swDocumentType, currentSearchFolders, &ok );
```
