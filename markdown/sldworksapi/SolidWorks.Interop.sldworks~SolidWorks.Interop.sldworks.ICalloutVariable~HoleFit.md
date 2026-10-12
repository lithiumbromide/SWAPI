---
title: "HoleFit Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "HoleFit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html"
---

# HoleFit Property (ICalloutVariable)

Gets or sets the fit tolerance in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleFit As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.String

instance.HoleFit = value

value = instance.HoleFit
```

### C#

```csharp
System.string HoleFit {get; set;}
```

### C++/CLI

```cpp
property System.String^ HoleFit {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fit tolerance

## VBA Syntax

See [CalloutVariable::HoleFit](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~HoleFit.html).

## Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceType.html), tolerance fit might not be visible. You cannot set tolerance fit if the tolerance type is [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html).swTolNONE.

To see the effects of setting tolerance fit, use [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html).

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::FitDisplayStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitDisplayStyle.html)
[ICalloutVariable::FitTextHeight Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextHeight.html)
[ICalloutVariable::FitTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextScale.html)
[ICalloutVariable::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitType.html)
[ICalloutVariable::FitUseTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitUseTextScale.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)
[IDimensionTolerance::GetHoleFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.html)
[IDimensionTolerance::SetFitValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
