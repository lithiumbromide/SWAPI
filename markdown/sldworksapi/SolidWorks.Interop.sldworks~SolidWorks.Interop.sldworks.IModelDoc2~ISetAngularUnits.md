---
title: "ISetAngularUnits Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ISetAngularUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.html"
---

# ISetAngularUnits Method (IModelDoc2)

Sets the current angular units.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetAngularUnits( _
   ByVal UType As System.Short, _
   ByVal FractBase As System.Short, _
   ByVal FractDenom As System.Short, _
   ByVal SigDigits As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UType As System.Short
Dim FractBase As System.Short
Dim FractDenom As System.Short
Dim SigDigits As System.Short

instance.ISetAngularUnits(UType, FractBase, FractDenom, SigDigits)
```

### C#

```csharp
void ISetAngularUnits(
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits
)
```

### C++/CLI

```cpp
void ISetAngularUnits(
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UType`: Angular units as defined in [swAngleUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html)
- `FractBase`: Not supported; however, input to this field is required but is not used
- `FractDenom`: Not supported; however, input to this field is required but is not used
- `SigDigits`: Significant digits if using decimal units

## VBA Syntax

See [ModelDoc2::ISetAngularUnits](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ISetAngularUnits.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAngularUnits.html)
[IModelDoc2::IGetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetAngularUnits.html)
[IModelDoc2::GetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAngularUnits.html)
[IModelDoc2::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUnits.html)
[IModelDoc2::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.html)
[IModelDoc2::IGetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits.html)
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.html)
[IModelDoc2::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits.html)
[IModelDoc2::LengthUnit Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LengthUnit.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
