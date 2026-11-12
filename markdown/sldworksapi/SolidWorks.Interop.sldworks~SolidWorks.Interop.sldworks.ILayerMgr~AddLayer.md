---
title: "AddLayer Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "AddLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~AddLayer.html"
---

# AddLayer Method (ILayerMgr)

Adds a layer to this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLayer( _
   ByVal NameIn As System.String, _
   ByVal DescIn As System.String, _
   ByVal ColorIn As System.Integer, _
   ByVal StyleIn As System.Integer, _
   ByVal WidthIn As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim NameIn As System.String
Dim DescIn As System.String
Dim ColorIn As System.Integer
Dim StyleIn As System.Integer
Dim WidthIn As System.Integer
Dim value As System.Integer

value = instance.AddLayer(NameIn, DescIn, ColorIn, StyleIn, WidthIn)
```

### C#

```csharp
System.int AddLayer(
   System.string NameIn,
   System.string DescIn,
   System.int ColorIn,
   System.int StyleIn,
   System.int WidthIn
)
```

### C++/CLI

```cpp
System.int AddLayer(
   System.String^ NameIn,
   System.String^ DescIn,
   System.int ColorIn,
   System.int StyleIn,
   System.int WidthIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Layer name
- `DescIn`: Description for the new layer
- `ColorIn`: COLORREF value specifying the desired color of items within this layer
- `StyleIn`: Line style as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)
- `WidthIn`: Line width as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

### Return Value

1 if the layer was created successfully

## VBA Syntax

See [LayerMgr::AddLayer](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~AddLayer.html).

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
