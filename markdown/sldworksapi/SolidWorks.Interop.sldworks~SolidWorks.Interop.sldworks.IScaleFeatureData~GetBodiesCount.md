---
title: "GetBodiesCount Method (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "GetBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetBodiesCount.html"
---

# GetBodiesCount Method (IScaleFeatureData)

Gets the number of scaled bodies for this scale feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Integer

value = instance.GetBodiesCount()
```

### C#

```csharp
System.int GetBodiesCount()
```

### C++/CLI

```cpp
System.int GetBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bodies that are scaled

## VBA Syntax

See [ScaleFeatureData::GetBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~GetBodiesCount.html).

## Examples

See [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) examples.

## Remarks

Call this method before calling [IScaleFeatureDta::IGetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~IGetBodies.html) to get the size of the array for that method.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)
[IScaleFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IGetBodies.html)
[IScaleFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ISetBodies.html)
[IScaleFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~Bodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
