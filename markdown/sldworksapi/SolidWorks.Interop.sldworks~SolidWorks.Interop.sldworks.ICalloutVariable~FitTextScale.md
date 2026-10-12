---
title: "FitTextScale Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "FitTextScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextScale.html"
---

# FitTextScale Property (ICalloutVariable)

Gets or sets the value with which to scale the fit tolerance font in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitTextScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Double

instance.FitTextScale = value

value = instance.FitTextScale
```

### C#

```csharp
System.double FitTextScale {get; set;}
```

### C++/CLI

```cpp
property System.double FitTextScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= value with which to scale the fit tolerance font <= 10.0

## VBA Syntax

See [CalloutVariable::FitTextScale](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~FitTextScale.html).

## Remarks

This property supports fit and fit-with-tolerance types only.

Set [ICalloutVariable::FitUseTextScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitUseTextScale.html) to true to enable setting this property.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::TextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextScale.html)
[ICalloutVariable::UseTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UseTextScale.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
