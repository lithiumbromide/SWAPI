---
title: "Open Assembly Component Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Assembly_Component_Example_CPlusPlus_COM.htm"
---

# Open Assembly Component Example (C++ COM)

This example shows how to open a component that is part of the current assembly document.

```vb
// Your code
...

LPMODELDOC m_ModelDoc = NULL;
 HRESULT hres = NOERROR;

 // Retrieve IModelDoc pointer
 hres = UserApp->getSWApp()->get_IActiveDoc( &m_ModelDoc );
 if( m_ModelDoc == NULL )
  return;

 LPASSEMBLYDOC m_AssemblyDoc = NULL;
 hres = m_ModelDoc->QueryInterface(IID_IAssemblyDoc, (LPVOID *)&m_AssemblyDoc);

 // If current document is not an assembly then return
 if(hres!=S_OK || m_AssemblyDoc==NULL)
return;

 VARIANT_BOOL selOK;
 hres = m_ModelDoc->SelectByID(_T("Lever-1@LeverAssem"), _T("COMPONENT"), 0, 0, 0, &selOK);

 // Open the component file
 hres = m_AssemblyDoc->OpenCompFile();

 // Make the Lever component the active document
 // Note: Use the correct filename extension
 hres = m_pSOLIDWORKS->IActivateDoc(_T("Lever.SLDPRT"), &m_ModelDoc);

// Your code
...

 // Releasing
 m_AssemblyDoc->Release();
 m_ModelDoc->Release();
```
