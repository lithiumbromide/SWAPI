---
title: "GetChamferUnits Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetChamferUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetChamferUnits.html"
---

# GetChamferUnits Method (IDisplayDimension)

Gets the local units of measurement for a chamfer display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetChamferUnits( _
   ByRef LengthUnit As System.Integer, _
   ByRef AngularUnit As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim LengthUnit As System.Integer
Dim AngularUnit As System.Integer
Dim value As System.Boolean

value = instance.GetChamferUnits(LengthUnit, AngularUnit)
```

### C#

```csharp
System.bool GetChamferUnits(
   out System.int LengthUnit,
   out System.int AngularUnit
)
```

### C++/CLI

```cpp
System.bool GetChamferUnits(
   [Out] System.int LengthUnit,
   [Out] System.int AngularUnit
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LengthUnit`: Unit of length as defined in [swLengthUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html)
- `AngularUnit`: Unit of angle as defined in [swAngleUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::GetChamferUnits](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetChamferUnits.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## Remarks

The unit display setting of a chamfer display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html) to determine whether the units settings are local or from the owning document. If IDisplayDimension::GetUseDocUnits returns true, then the units settings are from the owning document, and this API returns -1 for both length and angle units of measurement.

Local unit information for a chamfer display dimension is in force when Override Units is selected on the Other tab of the dimension's PropertyManager page. If Override Units is selected, then this API returns units as defined in swLengthUnit_e (length measurement) and swAngleUnit_e (angle measurement).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.html)
[IDisplayDimension::ChamferPrecision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ChamferPrecision.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
