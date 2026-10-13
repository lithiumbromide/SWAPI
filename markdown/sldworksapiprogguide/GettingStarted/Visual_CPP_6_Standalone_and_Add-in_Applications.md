---
title: "Visual C++ 6 Standalone and Add-in Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Visual_CPP_6_Standalone_and_Add-in_Applications.htm"
---

# Visual C++ 6 Standalone and Add-in Applications

## Visual C++ 6.0 Standalone and Add-in Applications

### Standalone Applications (.exe files)

To create an instance of SOLIDWORKS, your executable project should contain lines of code similar to the following:

```vb
//Import the SOLIDWORKS type library
#import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids
//Import the SOLIDWORKS constant type library
#import "swconst.tlb"  raw_interfaces_only, raw_native_types, no_namespace, named_guids

int _tmain(int argc, _TCHAR* argv[])
{
//Initialize COM
CoInitialize(NULL);

//Use ATL smart pointers
CComPtr<ISldWorks> swApp;

//Create an instance of SOLIDWORKS
HRESULT hres = swApp.CoCreateInstance(__uuidof(SldWorks), NULL, CLSCTX_LOCAL_SERVER);
.
. // Your code
.
//Shut down SOLIDWORKS
swApp->ExitApp();

//Release COM reference
swApp = NULL;

//Uninitialize COM
CoUninitialize();

return 0;
}
```

### Add-in Applications (.dll files)

Visual C++ applications have the option of using a COM or Dispatch interface. See [COM vs. Dispatch](../Overview/COM_vs_Dispatch.htm) for details.

NOTE: For COM DLL add-ins, success or failure on import/export is returned by the add-in through the HRESULT.
