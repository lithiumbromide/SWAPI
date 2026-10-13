---
title: "IsBossFeature Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "IsBossFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsBossFeature.html"
---

# IsBossFeature Method (ILoftFeatureData)

Gets whether the loft feature is a boss feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBossFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Boolean

value = instance.IsBossFeature()
```

### C#

```csharp
System.bool IsBossFeature()
```

### C++/CLI

```cpp
System.bool IsBossFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if it is a boss feature, false if not

## VBA Syntax

See [LoftFeatureData::IsBossFeature](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~IsBossFeature.html).

## Examples

[Get Guide Curves in Loft Feature (C#)](Get_Guide_Curves_in_Loft_Feature_Example_CSharp.htm)
[Get Guide Curves in Loft Feature (VB.NET)](Get_Guide_Curves_in_Loft_Feature_Example_VBNET.htm)
[Get Guide Curves in Loft Feature (VBA)](Get_Guide_Curves_in_Loft_Feature_Example_VB.htm)

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsThinFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
