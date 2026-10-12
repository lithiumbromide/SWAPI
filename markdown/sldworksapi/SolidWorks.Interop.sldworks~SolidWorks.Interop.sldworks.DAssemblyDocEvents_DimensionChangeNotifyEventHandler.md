---
title: "DAssemblyDocEvents_DimensionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_DimensionChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DimensionChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_DimensionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a dimension is changed through the **Dimension** dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_DimensionChangeNotifyEventHandler( _
   ByVal displayDim As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_DimensionChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_DimensionChangeNotifyEventHandler(
   System.object displayDim
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_DimensionChangeNotifyEventHandler(
   System.Object^ displayDim
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `displayDim`: [Display dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) that has changed

## VBA Syntax

See [DimensionChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~DimensionChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyDimensionChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
