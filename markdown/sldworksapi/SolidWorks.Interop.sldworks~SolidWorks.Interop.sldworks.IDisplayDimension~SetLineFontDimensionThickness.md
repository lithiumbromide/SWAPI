---
title: "SetLineFontDimensionThickness Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetLineFontDimensionThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontDimensionThickness.html"
---

# SetLineFontDimensionThickness Method (IDisplayDimension)

Sets the thickness of leaders of this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLineFontDimensionThickness( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Style As System.Integer
Dim value As System.Boolean

value = instance.SetLineFontDimensionThickness(UseDoc, Style)
```

### C#

```csharp
System.bool SetLineFontDimensionThickness(
   System.bool UseDoc,
   System.int Style
)
```

### C++/CLI

```cpp
System.bool SetLineFontDimensionThickness(
   System.bool UseDoc,
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True uses the document setting for the thickness of leaders, false uses the setting specified
  in Style
- `Style`: Leader thickness as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html); valid only if UseDoc = false

### Return Value

True if the leader thickness is set, false if not

## VBA Syntax

See [DisplayDimension::SetLineFontDimensionThickness](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetLineFontDimensionThickness.html).

## Remarks

After calling this method, call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetLineFontDimensionStyle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontDimensionStyle.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
