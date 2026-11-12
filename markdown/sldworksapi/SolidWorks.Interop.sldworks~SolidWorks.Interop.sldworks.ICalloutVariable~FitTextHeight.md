---
title: "FitTextHeight Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "FitTextHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextHeight.html"
---

# FitTextHeight Property (ICalloutVariable)

Gets or sets the height of the fit tolerance font in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitTextHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Double

instance.FitTextHeight = value

value = instance.FitTextHeight
```

### C#

```csharp
System.double FitTextHeight {get; set;}
```

### C++/CLI

```cpp
property System.double FitTextHeight {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height of the fit tolerance font

## VBA Syntax

See [CalloutVariable::FitTextHeight](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~FitTextHeight.html).

## Remarks

This property supports fit and fit-with-tolerance types only.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::TextHeight Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextHeight.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
