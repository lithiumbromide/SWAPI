---
title: "IGetAngularUnits Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetAngularUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetAngularUnits.html"
---

# IGetAngularUnits Method (IModelDoc2)

Gets the current angular unit settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAngularUnits() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Short

value = instance.IGetAngularUnits()
```

### C#

```csharp
System.short IGetAngularUnits()
```

### C++/CLI

```cpp
System.short IGetAngularUnits();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 5 shorts (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The format of the returned data is an array of 5 shorts:

[ AngleUnit, FractionBase, FractionValue, SignificantDigits, RoundToFraction ]

where:

- AngleUnit = current angular units. You can find the unit types in [swAngleUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html).
- FractionBase = Not currently supported. Do not use the return value in this field.
- FractionValue = Not currently supported. Do not use the return value in this field.
- SignificantDigits = significant digits if using decimal units.
- RoundToFraction = Not currently supported. Do not use the return value in this field.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAngularUnits.html)
[IModelDoc2::ISetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.html)
[IModelDoc2::SetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAngularUnits.html)
[IModelDoc2::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUnits.html)
[IModelDoc2::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.html)
[IModelDoc2::IGetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits.html)
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.html)
[IModelDoc2::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits.html)
[IModelDoc2::LengthUnit Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LengthUnit.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
