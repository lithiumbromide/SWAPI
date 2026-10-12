---
title: "ShaftFit Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "ShaftFit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html"
---

# ShaftFit Property (ICalloutVariable)

Gets or sets the shaft fit tolerance in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShaftFit As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.String

instance.ShaftFit = value

value = instance.ShaftFit
```

### C#

```csharp
System.string ShaftFit {get; set;}
```

### C++/CLI

```cpp
property System.String^ ShaftFit {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Shaft fit tolerance

## VBA Syntax

See [CalloutVariable::ShaftFit](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~ShaftFit.html).

## Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceType.html), tolerance shaft fit might not be visible. You cannot set tolerance shaft fit if the tolerance type is [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html).swTolNONE.

To see the effects of setting the tolerance shaft fit, use [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html).

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::FitDisplayStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitDisplayStyle.html)
[ICalloutVariable::FitTextHeight Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextHeight.html)
[ICalloutVariable::FitTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextScale.html)
[ICalloutVariable::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitType.html)
[ICalloutVariable::FitUseTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitUseTextScale.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)
[IDimensionTolerance::GetShaftFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.html)
[IDimensionTolerance::SetFitValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
