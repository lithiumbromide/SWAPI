---
title: "DSWPropertySheetEvents_CreateControlNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSWPropertySheetEvents_CreateControlNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_CreateControlNotifyEventHandler.html"
---

# DSWPropertySheetEvents_CreateControlNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the ActiveX control is created on the property page.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSWPropertySheetEvents_CreateControlNotifyEventHandler( _
   ByVal PageIndex As System.Integer, _
   ByVal ControlDispatch As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSWPropertySheetEvents_CreateControlNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSWPropertySheetEvents_CreateControlNotifyEventHandler(
   System.int PageIndex,
   System.object ControlDispatch
)
```

### C++/CLI

```cpp
public delegate System.int DSWPropertySheetEvents_CreateControlNotifyEventHandler(
   System.int PageIndex,
   System.Object^ ControlDispatch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PageIndex`: Index of property page within the property sheet for the add-in (see **Remarks**)
- `ControlDispatch`: ActiveX control

### Return Value

ActiveX control

## VBA Syntax

See [CreateControlNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SWPropertySheet~CreateControlNotify_EV.html).

## Remarks

If PageIndex is the same index as returned by [ISWPropertySheet::AddActivePage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet~AddActivePage.html), then ControlDispatch will contain the Dispatch pointer of the ActiveX control.

If developing a C++ application, use [swPropertySheetCreateControlNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 SP5, Revision Number 12.5
