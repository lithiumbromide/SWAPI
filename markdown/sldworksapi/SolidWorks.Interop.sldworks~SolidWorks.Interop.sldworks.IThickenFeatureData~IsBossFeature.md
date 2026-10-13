---
title: "IsBossFeature Method (IThickenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData"
member: "IsBossFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~IsBossFeature.html"
---

# IsBossFeature Method (IThickenFeatureData)

Gets whether this feature is a boss or a cut.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBossFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IThickenFeatureData
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

True if the feature is a boss, false if a cut

## VBA Syntax

See [ThickenFeatureData::IsBossFeature](ms-its:sldworksapivb6.chm::/sldworks~ThickenFeatureData~IsBossFeature.html).

## Examples

[Create Thicken Feature (VBA)](Create_Thicken_Feature_Example_VB.htm)

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
