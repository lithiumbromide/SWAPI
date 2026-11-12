---
title: "SetPrecision3 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetPrecision3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision3.html"
---

# SetPrecision3 Method (IDisplayDimension)

Sets the number of digits to display after the decimal point for precision and tolerance values in this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPrecision3( _
   ByVal Primary As System.Integer, _
   ByVal Dual As System.Integer, _
   ByVal PrimaryTol As System.Integer, _
   ByVal DualTol As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Primary As System.Integer
Dim Dual As System.Integer
Dim PrimaryTol As System.Integer
Dim DualTol As System.Integer
Dim value As System.Integer

value = instance.SetPrecision3(Primary, Dual, PrimaryTol, DualTol)
```

### C#

```csharp
System.int SetPrecision3(
   System.int Primary,
   System.int Dual,
   System.int PrimaryTol,
   System.int DualTol
)
```

### C++/CLI

```cpp
System.int SetPrecision3(
   System.int Primary,
   System.int Dual,
   System.int PrimaryTol,
   System.int DualTol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Primary`: Number of digits displayed after the decimal point in the primary precision value (see **Remarks**)
- `Dual`: Number of digits displayed after the decimal point in the dual precision value
- `PrimaryTol`: Number of digits displayed after the decimal point in the primary tolerance value (see **Remarks**)
- `DualTol`: Number of digits displayed after the decimal point in the dual tolerance value

### Return Value

Return status (see **Remarks**)

## VBA Syntax

See [DisplayDimension::SetPrecision3](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetPrecision3.html).

## Remarks

The specified values must be in the range from 0 to 8, which indicates the number of digits after the decimal place to display that value. Alternatively, the values can be defined by [swDimensionPrecisionSettings_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionPrecisionSettings_e.html).

| Parameter | swDimensionPrecisionSettings_e value | Result |
| --- | --- | --- |
| Primary Dual PrimaryTol DualTol | swDoNotChangePrecisionSetting | The current setting is not changed. |
| Primary Dual PrimaryTol DualTol | swPrecisionFollowsDocumentSetting | The number of decimal places to display adheres to the document setting. Use IModelDocExtension::GetUserPreferenceInteger / IModelDocExtension::SetUserPreferenceInteger .swDetailingLinearDimPrecision, swDetailingAngularDimPrecision, or swDetailingAltLinearDimPrecision to get or set that value. |
| PrimaryTol DualTol | swTolerancePrecisionFollowsNominal | The number of decimal places to display is the same as for the dimension or dual dimension value. |

This method does not support setting the Primary and PrimaryTol values for [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html). Use [ICalloutLengthVariable::Precision](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable~Precision.html) and [ICalloutLengthVariable::TolerancePrecision](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable~TolerancePrecision.html) to set these values for hole callouts. However, you must use this method to set Dual and DualTol values for hole callouts, because Dual and DualTol are global settings.

The return value indicates the success or failure of this method. In general, a value less than 0 indicates that the method failed and SOLIDWORKS did not set any precision values. A value of 0 indicates success. A value greater than 0 indicates that a problem occurred, but that the method did not fail.

- -1 Method failed; no precision values were set.
- 0 Method was successful; all precision values were set.
- 1 Primary precision value was invalid.
- 2 Alternate precision value was invalid.
- 3 Primary tolerance precision value was invalid.
- 4 Alternate tolerance precision value was invalid.

After using this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetAlternatePrecision2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAlternatePrecision2.html)
[IDisplayDimension::GetAlternateTolPrecision2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAlternateTolPrecision2.html)
[IDisplayDimension::GetPrimaryPrecision2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryPrecision2.html)
[IDisplayDimension::GetPrimaryTolPrecision2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryTolPrecision2.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
