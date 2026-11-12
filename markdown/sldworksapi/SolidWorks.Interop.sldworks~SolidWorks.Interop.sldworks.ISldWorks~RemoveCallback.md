---
title: "RemoveCallback Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveCallback"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.html"
---

# RemoveCallback Method (ISldWorks)

Unregisters a general purpose callback handler.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveCallback( _
   ByVal Cookie As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer

instance.RemoveCallback(Cookie)
```

### C#

```csharp
void RemoveCallback(
   System.int Cookie
)
```

### C++/CLI

```cpp
void RemoveCallback(
   System.int Cookie
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Cookie of callback function to unregister

## VBA Syntax

See [SldWorks::RemoveCallback](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveCallback.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CallBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.html)
[ISldWorks::SetAddinCallbackInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo.html)
[ISldWorks::AddCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 14.0
