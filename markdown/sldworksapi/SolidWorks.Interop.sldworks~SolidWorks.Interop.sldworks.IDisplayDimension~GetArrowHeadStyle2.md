---
title: "GetArrowHeadStyle2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetArrowHeadStyle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArrowHeadStyle2.html"
---

# GetArrowHeadStyle2 Method (IDisplayDimension)

Gets the arrowhead style used by this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadStyle2( _
   ByRef Style1 As System.Integer, _
   ByRef Style2 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Style1 As System.Integer
Dim Style2 As System.Integer
Dim value As System.Boolean

value = instance.GetArrowHeadStyle2(Style1, Style2)
```

### C#

```csharp
System.bool GetArrowHeadStyle2(
   out System.int Style1,
   out System.int Style2
)
```

### C++/CLI

```cpp
System.bool GetArrowHeadStyle2(
   [Out] System.int Style1,
   [Out] System.int Style2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style1`: Arrowhead style of first arrowhead as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `Style2`: Arrowhead style of second arrowhead as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

### Return Value

True if the styles are set, false if not

## VBA Syntax

See [DisplayDimension::GetArrowHeadStyle2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetArrowHeadStyle2.html).

## Remarks

The arrowhead style for a display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use this method and [IDisplayDimension::GetUseDocArrowHeadStyle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocArrowHeadStyle.html) to get the current values for these settings. Use [IDisplayDimension::SetArrowHeadStyle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle2.html) to set the arrowhead style.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
