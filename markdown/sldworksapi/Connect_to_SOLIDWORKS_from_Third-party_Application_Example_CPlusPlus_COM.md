---
title: "Connect to SOLIDWORKS Design from Third-party Application Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Connect_to_SOLIDWORKS_from_Third-party_Application_Example_CPlusPlus_COM.htm"
---

# Connect to SOLIDWORKS Design from Third-party Application Example (C++)

This example shows how to connect to SOLIDWORKS Design from a third-party application using C++.

```vb
// HelloSW.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include "objbase.h"

#import "sldworks.tlb" no_namespace raw_interfaces_only

int _tmain(int argc, _TCHAR* argv[])
{
::CoInitialize(NULL);
{
CLSID clsid;
::CLSIDFromProgID(L"SldWorks.Application", &clsid);

ISldWorks *swApp = NULL;
::CoCreateInstance(clsid, NULL, CLSCTX_LOCAL_SERVER, __uuidof(ISldWorks), (void**)&swApp);
if (swApp != NULL)
{
BSTR bstrHello = ::SysAllocString(L"Hello from SOLIDWORKS.");
swApp->SendMsgToUser(bstrHello);

::SysFreeString(bstrHello);
swApp->Release();
}
}
::CoUninitialize();
return 0;
}
```
