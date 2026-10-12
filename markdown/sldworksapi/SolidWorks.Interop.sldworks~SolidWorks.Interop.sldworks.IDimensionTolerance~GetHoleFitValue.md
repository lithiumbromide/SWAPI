---
title: "GetHoleFitValue Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetHoleFitValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.html"
---

# GetHoleFitValue Method (IDimensionTolerance)

Gets the tolerance hole fit value.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleFitValue() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.String

value = instance.GetHoleFitValue()
```

### C#

```csharp
System.string GetHoleFitValue()
```

### C++/CLI

```cpp
System.String^ GetHoleFitValue();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Tolerance hole fit value

## VBA Syntax

See [DimensionTolerance::GetHoleFitValue](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetHoleFitValue.html).

## Remarks

Depending on the [type of fit tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.html), to:

- get the tolerance shaft fit value, use [IDimensionTolerance::GetShaftFitValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.html).
- set the tolerance fit values, use [IDimensionTolerance::SetFitValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFitValues.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
