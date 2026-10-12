---
title: "GetShaftFitValue Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetShaftFitValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.html"
---

# GetShaftFitValue Method (IDimensionTolerance)

Gets the tolerance shaft fit value.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShaftFitValue() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.String

value = instance.GetShaftFitValue()
```

### C#

```csharp
System.string GetShaftFitValue()
```

### C++/CLI

```cpp
System.String^ GetShaftFitValue();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Tolerance shaft fit value

## VBA Syntax

See [DimensionTolerance::GetShaftFitValue](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetShaftFitValue.html).

## Remarks

Depending on the [type of fit tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.html), to:

- get the tolerance hole fit value, use [IDimensionTolerance::GetHoleFitValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.html).
- set the tolerance fit values, use [IDimensionTolerance::SetFitValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFitValues.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
