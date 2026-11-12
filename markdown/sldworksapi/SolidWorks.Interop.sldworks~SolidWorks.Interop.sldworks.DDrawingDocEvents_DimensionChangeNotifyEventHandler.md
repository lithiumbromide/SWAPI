---
title: "DDrawingDocEvents_DimensionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DimensionChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DimensionChangeNotifyEventHandler.html"
---

# DDrawingDocEvents_DimensionChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a dimension is changed through the Dimension dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DimensionChangeNotifyEventHandler( _
   ByVal displayDim As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DimensionChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DimensionChangeNotifyEventHandler(
   System.object displayDim
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DimensionChangeNotifyEventHandler(
   System.Object^ displayDim
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `displayDim`: [Display dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) that changed

## VBA Syntax

See [DimensionChangeNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~DimensionChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingDimensionChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
