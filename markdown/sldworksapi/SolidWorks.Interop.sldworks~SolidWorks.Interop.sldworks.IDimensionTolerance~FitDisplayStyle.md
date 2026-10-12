---
title: "FitDisplayStyle Property (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "FitDisplayStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitDisplayStyle.html"
---

# FitDisplayStyle Property (IDimensionTolerance)

Gets or sets how this dimension fit tolerance is displayed.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitDisplayStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Integer

instance.FitDisplayStyle = value

value = instance.FitDisplayStyle
```

### C#

```csharp
System.int FitDisplayStyle {get; set;}
```

### C++/CLI

```cpp
property System.int FitDisplayStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fit tolerance display style as defined in [swFitTolDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFitTolDisplay_e.html)

## VBA Syntax

See [DimensionTolerance::FitDisplayStyle](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~FitDisplayStyle.html).

## Remarks

Use [ICalloutVariable::FitDisplayStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitDisplayStyle.html) for multiple callouts in a display dimension for a hole.

To see the effects of changing the fit tolerance display style, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.html)
[IDimensionTolerance::GetFitFontHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.html)
[IDimensionTolerance::GetFitFontScale Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontScale.html)
[IDimensionTolerance::GetFitFontUseDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.html)
[IDimensionTolerance::GetFitFontUseScale Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.html)
[IDimensionTolerance::GetHoleFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.html)
[IDimensionTolerance::GetShaftFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.html)
[IDimensionTolerance::SetFitFont Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont.html)
[IDimensionTolerance::SetFitValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
