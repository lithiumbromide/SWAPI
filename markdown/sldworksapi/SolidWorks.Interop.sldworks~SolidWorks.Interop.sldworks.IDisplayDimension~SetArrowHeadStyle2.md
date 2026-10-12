---
title: "SetArrowHeadStyle2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetArrowHeadStyle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle2.html"
---

# SetArrowHeadStyle2 Method (IDisplayDimension)

Sets the arrowhead style of this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetArrowHeadStyle2( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style1 As System.Integer, _
   ByVal Style2 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Style1 As System.Integer
Dim Style2 As System.Integer
Dim value As System.Boolean

value = instance.SetArrowHeadStyle2(UseDoc, Style1, Style2)
```

### C#

```csharp
System.bool SetArrowHeadStyle2(
   System.bool UseDoc,
   System.int Style1,
   System.int Style2
)
```

### C++/CLI

```cpp
System.bool SetArrowHeadStyle2(
   System.bool UseDoc,
   System.int Style1,
   System.int Style2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True uses the document setting for arrowhead style, false uses the settings specified
  in Style1 and Style2
- `Style1`: Arrowhead style of first arrowhead as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `Style2`: Arrowhead style of second arrowhead as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

### Return Value

True if the arrowhead styles are set, false if not

## VBA Syntax

See [DisplayDimension::SetArrowHeadStyle2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetArrowHeadStyle2.html).

## Remarks

The arrowhead style for a display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocArrowHeadStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocArrowHeadStyle.html) and [IDisplayDimension::GetArrowHeadStyle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetArrowHeadStyle2.html) to get the current values for these settings.

Setting UseDoc to True indicates that the document default setting for arrowhead style should be used, and Style1 and Style2 will be ignored.

After using this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
