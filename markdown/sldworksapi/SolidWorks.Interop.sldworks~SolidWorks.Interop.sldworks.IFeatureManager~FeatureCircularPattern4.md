---
title: "FeatureCircularPattern4 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureCircularPattern4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern4.html"
---

# FeatureCircularPattern4 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureCircularPattern4( _
   ByVal Number As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDirection As System.Boolean, _
   ByVal DName As System.String, _
   ByVal GeometryPattern As System.Boolean, _
   ByVal EqualSpacing As System.Boolean, _
   ByVal VaryInstance As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Number As System.Integer
Dim Spacing As System.Double
Dim FlipDirection As System.Boolean
Dim DName As System.String
Dim GeometryPattern As System.Boolean
Dim EqualSpacing As System.Boolean
Dim VaryInstance As System.Boolean
Dim value As Feature

value = instance.FeatureCircularPattern4(Number, Spacing, FlipDirection, DName, GeometryPattern, EqualSpacing, VaryInstance)
```

### C#

```csharp
Feature FeatureCircularPattern4(
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.string DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing,
   System.bool VaryInstance
)
```

### C++/CLI

```cpp
Feature^ FeatureCircularPattern4(
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.String^ DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing,
   System.bool VaryInstance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Number`: Number of instances of the circular pattern to insert, including the original instance
- `Spacing`: Spacing between each instance of the circular pattern; total angle in radians if EqualSpacing is true
- `FlipDirection`: True to flip the direction of the circular pattern, false to not
- `DName`: Name of the angular dimension defining the direction of the pattern
- `GeometryPattern`: True to use geometry pattern, false to not
- `EqualSpacing`: True to use equal spacing, false to not
- `VaryInstance`: True to vary the dimensions or spacing of individual pattern instances, false to not; valid only if GeometryPattern = false (see **Remarks**)

### Return Value

Circular pattern [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FeatureCircularPattern4](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureCircularPattern4.html).

## Examples

[Create Circular Pattern (VBA)](Create_Circular_Pattern_Example_VB.htm)
[Create Circular Pattern (VB.NET)](Create_Circular_Pattern_Example_VBNET.htm)
[Create Circular Pattern (C#)](Create_Circular_Pattern_Example_CSharp.htm)

## Remarks

| If... | To select a feature, use... | To select a component, use... |
| --- | --- | --- |
| Using IModelDocExtension::SelectByID2 to select features and components, ordered selection of the features and components is required | 1 to mark the direction axis 4 to mark the features to pattern | 1 to mark the components to pattern 2 to mark the direction axis |
| Directly selecting a feature or axis using IFeature::Select2 | 1 to mark the direction axis 4 to mark the features to pattern | ISelectData::Mark and Component2::Select3 1 to mark the components to pattern 2 to mark the direction axis |

If VaryInstance = true, then to indicate how to vary the individual pattern instances, decide on the type of pattern and call its corresponding method before calling this method:

| Type... | Method... |
| --- | --- |
| Increment | IFeatureManager::InsertVaryInstanceIncrement |
| Override | IFeatureManager::InsertVaryInstanceOverride |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
