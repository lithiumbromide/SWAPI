---
title: "DPartDocEvents_DimensionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DimensionChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DimensionChangeNotifyEventHandler.html"
---

# DPartDocEvents_DimensionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a dimension is changed through the Dimension dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DimensionChangeNotifyEventHandler( _
   ByVal displayDim As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DimensionChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DimensionChangeNotifyEventHandler(
   System.object displayDim
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DimensionChangeNotifyEventHandler(
   System.Object^ displayDim
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `displayDim`: [Display dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) that changed

## VBA Syntax

See [DimensionChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DimensionChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartDimensionChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
