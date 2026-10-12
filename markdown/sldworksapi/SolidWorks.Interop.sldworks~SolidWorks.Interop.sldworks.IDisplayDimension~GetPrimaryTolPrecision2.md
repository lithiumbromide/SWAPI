---
title: "GetPrimaryTolPrecision2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetPrimaryTolPrecision2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryTolPrecision2.html"
---

# GetPrimaryTolPrecision2 Method (IDisplayDimension)

Gets the primary tolerance precision setting for this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrimaryTolPrecision2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetPrimaryTolPrecision2()
```

### C#

```csharp
System.int GetPrimaryTolPrecision2()
```

### C++/CLI

```cpp
System.int GetPrimaryTolPrecision2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Precision setting as defined by [swDimensionPrecisionSettings_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionPrecisionSettings_e.html)

## VBA Syntax

See [DisplayDimension::GetPrimaryTolPrecision2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetPrimaryTolPrecision2.html).

## Examples

[Get Precisions for a Dimension (VBA)](Get_Precisions_for_a_Dimension_Example_VB.htm)

## Remarks

If the return value equals swPrecisionFollowsDocumentSetting, then the precision being used is the document default for dual dimension values. You can retrieve the value using [IModelDocExtension::GetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html) with swDetailingLinearTolPrecision or swDetailingAngularTolPrecision.

If the return value is swTolerancePrecisionFollowsNominal, then the precision being used is the same as the precision being used for the dimension value. You can retrieve the value using [IDisplayDimension::GetPrimaryPrecision2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetPrimaryPrecision2.html)

Otherwise, the return value is the precision in the dimensions primary units.

Use [IDisplayDimension::SetPrecision2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetPrecision2.html) to set the precision values on this display dimension.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension:GetAlternateTolPrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAlternateTolPrecision2.html)
[IDisplayDimension:GetAlternatePrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAlternatePrecision2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
