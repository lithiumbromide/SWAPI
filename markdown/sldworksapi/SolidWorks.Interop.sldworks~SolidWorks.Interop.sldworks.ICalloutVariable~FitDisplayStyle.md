---
title: "FitDisplayStyle Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "FitDisplayStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitDisplayStyle.html"
---

# FitDisplayStyle Property (ICalloutVariable)

Gets or sets how fit tolerance is displayed in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitDisplayStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
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

See [CalloutVariable::FitDisplayStyle](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~FitDisplayStyle.html).

## Remarks

To see the effects of changing the fit tolerance display style, use [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html).

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[IDimensionTolerance::FitDisplayTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitDisplayStyle.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)
[ICalloutVariable::FitTextHeight Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextHeight.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
