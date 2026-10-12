---
title: "FeatureLinearPattern3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureLinearPattern3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLinearPattern3.html"
---

# FeatureLinearPattern3 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureLinearPattern4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLinearPattern4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureLinearPattern3( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal FlipDir1 As System.Boolean, _
   ByVal FlipDir2 As System.Boolean, _
   ByVal DName1 As System.String, _
   ByVal DName2 As System.String, _
   ByVal GeometryPattern As System.Boolean, _
   ByVal VaryInstance As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Num1 As System.Integer
Dim Spacing1 As System.Double
Dim Num2 As System.Integer
Dim Spacing2 As System.Double
Dim FlipDir1 As System.Boolean
Dim FlipDir2 As System.Boolean
Dim DName1 As System.String
Dim DName2 As System.String
Dim GeometryPattern As System.Boolean
Dim VaryInstance As System.Boolean
Dim value As Feature

value = instance.FeatureLinearPattern3(Num1, Spacing1, Num2, Spacing2, FlipDir1, FlipDir2, DName1, DName2, GeometryPattern, VaryInstance)
```

### C#

```csharp
Feature FeatureLinearPattern3(
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.string DName1,
   System.string DName2,
   System.bool GeometryPattern,
   System.bool VaryInstance
)
```

### C++/CLI

```cpp
Feature^ FeatureLinearPattern3(
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.String^ DName1,
   System.String^ DName2,
   System.bool GeometryPattern,
   System.bool VaryInstance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Num1`: Number of instances of the linear pattern in Direction 1, including the original
- `Spacing1`: Spacing between each instance of the linear pattern in Direction 1 in meters
- `Num2`: Number of instances of the linear pattern in Direction 2, including the original
- `Spacing2`: Spacing between each instance of the linear pattern in Direction 2 in meters
- `FlipDir1`: True if you want to reverse the direction of the linear pattern in Direction 1, false if not
- `FlipDir2`: True if you want to reverse the direction of the linear pattern in Direction 2, false if not
- `DName1`: Name of the dimension defining Direction 1
- `DName2`: Name of the dimension defining Direction 2
- `GeometryPattern`: True to use geometry pattern, false to not
- `VaryInstance`: True to vary the dimensions and spacing of individual pattern instances, false to not; valid only if GeometryPattern = false (see **Remarks**)

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureLinearPattern3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureLinearPattern3.html).

## Remarks

| If... | To select a feature, use... | To select a component, use... |
| --- | --- | --- |
| Using IModelDocExtension::SelectByID2 to select features and components, ordered selection of the features and components is required | 1 and 2 to mark the directions 4 to mark the features to pattern | 1 to mark the components to pattern 2 and 4 to mark the directions |
| Directly selecting a feature or component | IFeature::Select2 | ISelectData::Mark and IComponent2::Select3 |

If VaryInstance = true, then to indicate how to vary the individual pattern instances, decide on the type of pattern and call its corresponding method before calling this method:

| Type... | Method... |
| --- | --- |
| Increment | IFeatureManager::InsertVaryInstanceIncrement |
| Override | IFeatureManager::InsertVaryInstanceOverride |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
