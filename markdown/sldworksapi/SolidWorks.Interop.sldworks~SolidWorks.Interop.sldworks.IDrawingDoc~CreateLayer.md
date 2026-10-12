---
title: "CreateLayer Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLayer.html"
---

# CreateLayer Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateLayer2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateLayer2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLayer( _
   ByVal Layername As System.String, _
   ByVal LayerDesc As System.String, _
   ByVal LayerColor As System.Integer, _
   ByVal LayerStyle As System.Integer, _
   ByVal LayerWidth As System.Integer, _
   ByVal BOn As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Layername As System.String
Dim LayerDesc As System.String
Dim LayerColor As System.Integer
Dim LayerStyle As System.Integer
Dim LayerWidth As System.Integer
Dim BOn As System.Boolean
Dim value As System.Boolean

value = instance.CreateLayer(Layername, LayerDesc, LayerColor, LayerStyle, LayerWidth, BOn)
```

### C#

```csharp
System.bool CreateLayer(
   System.string Layername,
   System.string LayerDesc,
   System.int LayerColor,
   System.int LayerStyle,
   System.int LayerWidth,
   System.bool BOn
)
```

### C++/CLI

```cpp
System.bool CreateLayer(
   System.String^ Layername,
   System.String^ LayerDesc,
   System.int LayerColor,
   System.int LayerStyle,
   System.int LayerWidth,
   System.bool BOn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layername`: Layer name (see **Remarks**)
- `LayerDesc`: Description for the new layer
- `LayerColor`: COLORREF value specifying the color of items in this layer
- `LayerStyle`: Line style as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)
- `LayerWidth`: Line width as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)
- `BOn`: True makes this layer visible, false makes it invisible

### Return Value

True if the layer was created successfully, false if not

## VBA Syntax

See [DrawingDoc::CreateLayer](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateLayer.html).

## Remarks

If this layer is not visible, then SOLIDWORKS does not display entities on the layer.

Do not use the backslash (/) or at sign (@) symbols in LayerName.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::SetCurrentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetCurrentLayer.html)
[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)

## Availability

SOLIDWORKS 99, datecode 1999207
