---
title: "Traverse All Open Documents Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_All_Open_Documents_Example_CPlusPlus_COM.htm"
---

# Traverse All Open Documents Example (C++ COM)

This example shows how to traverse all open documents.

```vb
bool CFileReferenceTests::isFileOpen(CString fileSpec)
{

 bool retval = FALSE;
 HRESULT hres = S_FALSE;

 if (fileSpec.IsEmpty())
  return retval;

 LPENUMDOCUMENTS pDocEnum = NULL;
 hres = TheApplication->m_pSldWorks->EnumDocuments2(&pDocEnum);

 // No documents open
 if (pDocEnum == NULL)
  return retval;

 int docNum = 0;
 LPMODELDOC pModelDoc = NULL;
 hres = pDocEnum->Next(1, &pModelDoc, NULL);
 while (S_OK == hres)
 {
  BSTR bdocName;
  hres = pModelDoc->GetPathName(&bdocName);
  CString docName(bdocName);

  // File name matches
  if (fileSpec.CompareNoCase(docName) == 0)
   retval = TRUE;

  pModelDoc->Release();
  pModelDoc = NULL;
  hres = pDocEnum->Next(1, &pModelDoc, NULL);
 }

 if (pDocEnum != NULL) pDocEnum->Release();

 return retval;

}
```
