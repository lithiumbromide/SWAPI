---
title: "SetCurrentLayer Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetCurrentLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetCurrentLayer.html"
---

# SetCurrentLayer Method (IDrawingDoc)

Sets the current layer used by this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCurrentLayer( _
   ByVal Layername As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Layername As System.String
Dim value As System.Boolean

value = instance.SetCurrentLayer(Layername)
```

### C#

```csharp
System.bool SetCurrentLayer(
   System.string Layername
)
```

### C++/CLI

```cpp
System.bool SetCurrentLayer(
   System.String^ Layername
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layername`: Name of the layer

## VBA Syntax

See [DrawingDoc::SetCurrentLayer](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetCurrentLayer.html).

## Remarks

SOLIDWORKS creates subsequent items on the specified layer.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ChangeComponentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeComponentLayer.html)
[IDrawingDoc::CreateLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLayer.html)
[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)

## Availability

SOLIDWORKS 99, datecode 1999207
