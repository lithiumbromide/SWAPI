---
title: "FeatureCircularPattern2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureCircularPattern2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern2.html"
---

# FeatureCircularPattern2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCircularPattern3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureCircularPattern2( _
   ByVal Num As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal DName As System.String, _
   ByVal GeometryPattern As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Num As System.Integer
Dim Spacing As System.Double
Dim FlipDir As System.Boolean
Dim DName As System.String
Dim GeometryPattern As System.Boolean
Dim value As Feature

value = instance.FeatureCircularPattern2(Num, Spacing, FlipDir, DName, GeometryPattern)
```

### C#

```csharp
Feature FeatureCircularPattern2(
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.string DName,
   System.bool GeometryPattern
)
```

### C++/CLI

```cpp
Feature^ FeatureCircularPattern2(
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.String^ DName,
   System.bool GeometryPattern
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Num`: Number of instances of the circular pattern to insert, including the original
- `Spacing`: Spacing between each instance of the circular pattern in radians
- `FlipDir`: True to flip the direction of the circular pattern, false to not
- `DName`: Name of the angular dimension defining the direction of the pattern
- `GeometryPattern`: True to use geometry pattern, false to not

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::FeatureCircularPattern2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureCircularPattern2.html).

## Remarks

This method requires ordered selection of the features and components.

- Features and axis: Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a Mark of 4 for the features to pattern and a Mark of 1 for the axis. You can also use [IFeature::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Select2.html) to select the features and the axis.
- Components and axis: Use IModelDocExtension::SelectByID2 with a Mark of 1 for the components to pattern and a Mark of 2 for the axis.

You must select the features or components before selecting the axis.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
