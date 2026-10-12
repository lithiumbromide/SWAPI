---
title: "C++ Add-ins and Windows Vista"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/Vista.htm"
---

# C++ Add-ins and Windows Vista

Add-ins written in .NET should work in Windows Vista. However, native add-ins written in C++ that register type libraries might encounter problems. The Windows Vista operating system has a limitation that prevents registration of such add-ins.

If you do not need the type library, the best solution is to remove its registration from the code. Do this in C++ by setting the **bRegTypeLib** argument to **FALSE** in CAtlDllModuleT::DllRegisterServer() and CAtlDllModuleT::DLLUnregisterServer():

```vb
 // DllRegisterServer - Adds entries to the system registry
 STDAPI DllRegisterServer(void)
{
  AFX_MANAGE_STATE(AfxGetStaticModuleState());
  // registers object
  HRESULT hr = _AtlModule.DllRegisterServer(  FALSE );
  return hr;
}
// DllUnregisterServer - Removes entries from the system registry
 STDAPI DllUnregisterServer(void)
{
  AFX_MANAGE_STATE(AfxGetStaticModuleState());
  HRESULT hr = _AtlModule.DllUnregisterServer(  FALSE );
  return hr;
}
```
