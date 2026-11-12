---
title: "GetUnits Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUnits.html"
---

# GetUnits Method (IModelDoc2)

Gets the current unit settings, fraction base, fraction value, and significant digits.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUnits() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetUnits()
```

### C#

```csharp
System.object GetUnits()
```

### C++/CLI

```cpp
System.Object^ GetUnits();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 5 shorts (see **Remarks**)

## VBA Syntax

See [ModelDoc2::GetUnits](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetUnits.html).

## Remarks

The format of the returned data is an array of shorts:

[ LengthUnit, FractionBase, FractionValue, SignificantDigits, RoundToFraction ]

where:

- LengthUnit = current model units as defined in [swLengthUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html).
- FractionBase = decimal or fraction as defined in [swFractionDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html); fractional units are only valid if the model units are set to swINCHES or swFEETINCHES.
- FractionValue = denominator value if using fractional units.
- SignificantDigits = significant digits if using decimal units.
- RoundToFraction = flag denoting whether or not to round to the fraction; for example, if 4 was the denominator value and the actual value was .27, it is rounded to .25

You can also use [IModelDoc2::LengthUnit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~LengthUnit.html), which provides access to the LengthUnit parameter.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits.html)
[IModelDoc2::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits.html)
[IModelDoc2::GetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAngularUnits.html)
[IModelDoc2::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.html)
[IModelDoc2::IGetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetAngularUnits.html)
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.html)
[IModelDoc2::ISetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.html)
[IModelDoc2::SetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAngularUnits.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
