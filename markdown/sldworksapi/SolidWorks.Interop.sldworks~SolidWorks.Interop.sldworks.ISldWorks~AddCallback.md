---
title: "AddCallback Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddCallback"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.html"
---

# AddCallback Method (ISldWorks)

Registers a general purpose callback handler.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddCallback( _
   ByVal Cookie As System.Integer, _
   ByVal CallbackFunction As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim CallbackFunction As System.String

instance.AddCallback(Cookie, CallbackFunction)
```

### C#

```csharp
void AddCallback(
   System.int Cookie,
   System.string CallbackFunction
)
```

### C++/CLI

```cpp
void AddCallback(
   System.int Cookie,
   System.String^ CallbackFunction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Cookie specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `CallbackFunction`: Name of the function to call (see **Remarks**)

## VBA Syntax

See [SldWorks::AddCallback](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddCallback.html).

## Remarks

The callback function has three arguments:

| Callback function parameter name in example | Data Type | Description |
| --- | --- | --- |
| cmd | Integer | Command ID as defined in swAppCallBackCmd_e |
| data | Integer | Data related to the event |
| dsp | LPDISPATCH | Not currently used |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CallBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.html)
[ISldWorks::RemoveCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.html)
[ISldWorks::SetAddinCallbackInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo.html)
[ISldWorks::PostMessageToApplication Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplication.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
