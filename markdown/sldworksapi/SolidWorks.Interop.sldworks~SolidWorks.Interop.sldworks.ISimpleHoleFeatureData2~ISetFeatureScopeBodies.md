---
title: "ISetFeatureScopeBodies Method (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "ISetFeatureScopeBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ISetFeatureScopeBodies.html"
---

# ISetFeatureScopeBodies Method (ISimpleHoleFeatureData2)

Sets the solid bodies that the simple hole feature affects in the multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFeatureScopeBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim Count As System.Integer
Dim BodyArr As Body2

instance.ISetFeatureScopeBodies(Count, BodyArr)
```

### C#

```csharp
void ISetFeatureScopeBodies(
   System.int Count,
   ref Body2 BodyArr
)
```

### C++/CLI

```cpp
void ISetFeatureScopeBodies(
   System.int Count,
   Body2^% BodyArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bodies that this simple hole feature affects
- `BodyArr`: Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that this simple hole feature affects

## VBA Syntax

See [SimpleHoleFeatureData2::ISetFeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~ISetFeatureScopeBodies.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetFeatureScopeBodiesCount.html)
[ISimpleHoleFeatureData2::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.html)
[ISimpleHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.html)
[ISimpleHoleFeatureData2::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScope.html)
[ISimpleHoleFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
