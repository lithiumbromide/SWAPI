---
title: "Document Version History Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Document_Version_History_Example_CPlusPlus_COM.htm"
---

# Document Version History Example (C++ COM)

## Obtain Version History Example (C++ COM)

This example shows how to obtain a version history of a file. IModelDoc2::IVersionHistory returns an array, so this code must be used in an in-process DLL.

```vb
DocumentVersionHistory(ISldWorks* m_pSldWorks)
{
 BSTR* versionHistStrings = NULL;
 LPMODELDOC2 pModelDoc = NULL;
 HRESULT hres= S_OK;

 hres = m_pSldWorks->get_IActiveDoc2(&pModelDoc);
 if (hres != S_OK || pModelDoc == NULL)
  return;

 int versHistCount = 0;
 hres = pModelDoc->IGetVersionHistoryCount(&versHistCount);
 if (hres != S_OK || versHistCount == 0)
 {
  pModelDoc->Release();
  return;
 }
 versionHistStrings = new BSTR[versHistCount];
 hres = pModelDoc->IVersionHistory(versionHistStrings);
 if (hres != S_OK || versionHistStrings == NULL)
 {
  delete [] versionHistStrings;
  pModelDoc->Release();
  return;
 }

 // For each version found
 for (int ii = 0;ii < versHistCount;ii++)
 {
  CString tempstr2(versionHistStrings[ii]);
  AfxMessageBox (tempstr2);

  SysFreeString( versionHistStrings[ii]);
 }

 // default destructor
 pModelDoc->Release();
 delete [] versionHistStrings;
}
```
