---
title: "GetAlternatePrecision2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetAlternatePrecision2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAlternatePrecision2.html"
---

# GetAlternatePrecision2 Method (IDisplayDimension)

Gets the displayed precision for the dual portion of this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAlternatePrecision2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetAlternatePrecision2()
```

### C#

```csharp
System.int GetAlternatePrecision2()
```

### C++/CLI

```cpp
System.int GetAlternatePrecision2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Precision setting as defined in [swDimensionPrecisionSettings_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionPrecisionSettings_e.html)

## VBA Syntax

See [DisplayDimension::GetAlternatePrecision2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetAlternatePrecision2.html).

## Examples

[Get Precisions for a Dimension (VBA)](Get_Precisions_for_a_Dimension_Example_VB.htm)

## Remarks

If the return value equals swPrecisionFollowsDocumentSetting, then the precision used is the document default for dual dimension values. You can retrieve the value using [IModelDocExtension::GetUserPreferenceInteger](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html) with swDetailingAltLinearDimPrecision. Otherwise, the return value is the precision in the dimensions dual units.

Use [IDisplayDimension::SetPrecision2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetPrecision2.html) to set precision values on this display dimension.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetPrimaryTolPrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryTolPrecision2.html)
[IDisplayDimension:GetPrimaryPrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryPrecision2.html)
[IDisplayDimension:GetPrimaryTolPrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryTolPrecision2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
