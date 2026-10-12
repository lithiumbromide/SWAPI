---
title: "Get and Set Units Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Units_Example_CPlusPlus_COM.htm"
---

# Get and Set Units Example (C++ COM)

This example shows how to get the current unit settings of the document and change them to inches. Be sure to import swconst.tlb.

The method IModelDoc2::IGetUnits returns an array, so this code must be used in an in-process DLL. Otherwise, use the method IModelDoc2::GetUnits that returns a VARIANT.

```vb
GetAndSetUnits(ISldWorks* m_pSldWorks)
{
 LPMODELDOC2 pModelDoc = NULL;
 // Retrieve Model Document pointer
 if( S_OK != m_pSldWorks->get_IActiveDoc2( &pModelDoc ) || pModelDoc == NULL )
  return;
 short unitArray[5];
 HRESULT hres = S_OK;
 hres = pModelDoc->IGetUnits(unitArray);
 CString message;    // Create message string
 message.Format(_T("Unit Settings are:\n%d \t%d \t%d \t%d \t%d"),
 unitArray[0],unitArray[1],unitArray[2],unitArray[3],unitArray[4]);
 // Send message to the user
 AfxMessageBox (message);
 // If units are not inches, change them to inches
 if (unitArray[0] != swINCHES)
 {
  short denom = 16;
  hres = pModelDoc->SetUnits(swINCHES, swFRACTION, denom, unitArray[3], FALSE);
 }
 pModelDoc->Release();
}
```
