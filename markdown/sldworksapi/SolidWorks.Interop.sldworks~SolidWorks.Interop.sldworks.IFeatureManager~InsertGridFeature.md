---
title: "InsertGridFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertGridFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGridFeature.html"
---

# InsertGridFeature Method (IFeatureManager)

Inserts a Grid System feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGridFeature( _
   ByVal HeightDoubles As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim HeightDoubles As System.Object
Dim value As Feature

value = instance.InsertGridFeature(HeightDoubles)
```

### C#

```csharp
Feature InsertGridFeature(
   System.object HeightDoubles
)
```

### C++/CLI

```cpp
Feature^ InsertGridFeature(
   System.Object^ HeightDoubles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HeightDoubles`: Array of doubles specifying distances between Grid System levels

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertGridFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertGridFeature.html).

## Examples

[Insert Grid System Feature (C#)](Insert_Grid_System_Feature_Example_CSharp.htm)
[Insert Grid System Feature (VB.NET)](Insert_Grid_System_Feature_Example_VBNET.htm)
[Insert Grid System Feature (VBA)](Insert_Grid_System_Feature_Example_VB.htm)

## Remarks

The number of elements in HeightDoubles determines the number of levels in this Grid System feature.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
