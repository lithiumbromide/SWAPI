---
title: "SetLineFontDimensionStyle Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetLineFontDimensionStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontDimensionStyle.html"
---

# SetLineFontDimensionStyle Method (IDisplayDimension)

Sets the style of leader for this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLineFontDimensionStyle( _
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

value = instance.SetLineFontDimensionStyle(UseDoc, Style)
```

### C#

```csharp
System.bool SetLineFontDimensionStyle(
   System.bool UseDoc,
   System.int Style
)
```

### C++/CLI

```cpp
System.bool SetLineFontDimensionStyle(
   System.bool UseDoc,
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True uses the document setting for the leader style, false uses the setting specified
  in Style
- `Style`: Leader style as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html); valid only if UseDoc = false

### Return Value

True if the leader style is set, false if not

## VBA Syntax

See [DisplayDimension::SetLineFontDimensionStyle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetLineFontDimensionStyle.html).

## Remarks

After calling this method, call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetLineFontDimensionThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontDimensionThickness.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
