---
title: "GetFeatureScopeBodiesCount Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "GetFeatureScopeBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetFeatureScopeBodiesCount.html"
---

# GetFeatureScopeBodiesCount Method (ILoftFeatureData)

Gets the number of solid bodies affected by the loft feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureScopeBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Integer

value = instance.GetFeatureScopeBodiesCount()
```

### C#

```csharp
System.int GetFeatureScopeBodiesCount()
```

### C++/CLI

```cpp
System.int GetFeatureScopeBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of solid bodies affected by the loft feature in a multibody part

## VBA Syntax

See [LoftFeatureData::GetFeatureScopeBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~GetFeatureScopeBodiesCount.html).

## Remarks

Call this method before calling [ILoftFeatureData::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~IGetFeatureScopeBodies.html) to determine the size of the array for that method.

If [ILoftFeatureData::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~FeatureScope.html) is false, then the return value will be 0.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetFeatureScopeBodies.html)
[ILoftFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~FeatureScopeBodies.html)
[ILoftFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~AutoSelect.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
