---
title: "FitType Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "FitType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitType.html"
---

# FitType Property (ICalloutVariable)

Gets or sets the fit type for this hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Integer

instance.FitType = value

value = instance.FitType
```

### C#

```csharp
System.int FitType {get; set;}
```

### C++/CLI

```cpp
property System.int FitType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fit type as defined in [swFitType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFitType_e.html)

## VBA Syntax

See [CalloutVariable::FitType](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~FitType.html).

## Remarks

This property is only available when the [type of tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceType.html) is [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html):

- swTolFIT,
- swTolFITTOLONLY, or
- swTolFITWITHTOL.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
