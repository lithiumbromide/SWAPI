---
title: "QueryInterface Example"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/QueryInterface_Example_CPlusPlus_COM.htm"
---

# QueryInterface Example

## Use QueryInterface Example (C++ COM)

This example shows how to use QueryInterface.

```vb
LPUNKNOWN iUnk = NULL;
LPFEATURE m_Feature = NULL;
HRESULT hres = S_FALSE;

// Your code
...

// Get the underlying object
hres = m_Feature->IGetSpecificFeature( &iUnk );

LPREFPLANE m_RefPlane = NULL;
hres = iUnk->QueryInterface( IID_IRefPlane, (LPVOID*)&m_RefPlane);

// If Feature is a RefPlane
if (hres == S_OK && m_RefPlane != NULL)
{
AfxMessageBox( _T("This feature is a reference plane") );

// Use m_RefPlane object
...

// Release m_RefPlane object
m_RefPlane->Release();
}

// Release iUnk object
iUnk->Release();

/*
   The call to IGetSpecificFeature increases the reference count on iUnk by 1. If the call to QueryInterface is successful, it also increases the reference count on iUnk by 1. The m_RefPlane and iUnk pointers are the same object; you can therefore release either one. m_RefPlane->Release() is shown in this example.
*/
```
