---
title: "PostIntersect Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PostIntersect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostIntersect.html"
---

# PostIntersect Method (IFeatureManager)

Creates an intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function PostIntersect( _
   ByVal IntersectionsToExclude As System.Object, _
   ByVal Merge As System.Boolean, _
   ByVal Consume As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim IntersectionsToExclude As System.Object
Dim Merge As System.Boolean
Dim Consume As System.Boolean
Dim value As Feature

value = instance.PostIntersect(IntersectionsToExclude, Merge, Consume)
```

### C#

```csharp
Feature PostIntersect(
   System.object IntersectionsToExclude,
   System.bool Merge,
   System.bool Consume
)
```

### C++/CLI

```cpp
Feature^ PostIntersect(
   System.Object^ IntersectionsToExclude,
   System.bool Merge,
   System.bool Consume
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IntersectionsToExclude`: Array of booleans indicating which bodies returned by [IFeatureManager::PreIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PreIntersect.html) to exclude from this intersect feature
- `Merge`: True to merge all intersect regions into one body, false to not
- `Consume`: True to remove input surfaces from the FeatureManager design tree, false to not

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::PostIntersect](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PostIntersect.html).

## Examples

[Get Intersect Feature Data (VBA)](Get_Intersect_Feature_Data_Example_VB.htm)
[Get Intersect Feature Data (VB.NET)](Get_Intersect_Feature_Data_Example_VBNET.htm)
[Get Intersect Feature Data (C#)](Get_Intersect_Feature_Data_Example_CSharp.htm)

## Remarks

Before calling this method, you must call [IFeatureManager::PreIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PreIntersect.html) to obtain the intersect bodies.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
