---
title: "GetControllingDimensionName Method (IDimPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDimPatternFeatureData"
member: "GetControllingDimensionName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetControllingDimensionName.html"
---

# GetControllingDimensionName Method (IDimPatternFeatureData)

Gets the name of the controlling dimension for the pattern instance at the specified index in this variable pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControllingDimensionName( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimPatternFeatureData
Dim Index As System.Integer
Dim value As System.String

value = instance.GetControllingDimensionName(Index)
```

### C#

```csharp
System.string GetControllingDimensionName(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetControllingDimensionName(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the controlling dimension pattern (see **Remarks**)

### Return Value

Name of the controlling dimension of the pattern instance

## VBA Syntax

See [DimPatternFeatureData::GetControllingDimensionName](ms-its:sldworksapivb6.chm::/sldworks~DimPatternFeatureData~GetControllingDimensionName.html).

## Examples

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)

## Remarks

Use [IDimPatternFeatureData::GetControllingDimensionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetControllingDimensionCount.html) to get the number of controlling dimensions.

## See Also

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.html)
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
