---
title: "SetSplitBodies2 Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "SetSplitBodies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html"
---

# SetSplitBodies2 Method (ISplitBodyFeatureData)

Edits the current split bodies in this Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSplitBodies2( _
   ByVal PathVar As System.Object, _
   ByVal FlagVar As System.Object, _
   ByVal BodyOrigin As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim PathVar As System.Object
Dim FlagVar As System.Object
Dim BodyOrigin As System.Object

instance.SetSplitBodies2(PathVar, FlagVar, BodyOrigin)
```

### C#

```csharp
void SetSplitBodies2(
   System.object PathVar,
   System.object FlagVar,
   System.object BodyOrigin
)
```

### C++/CLI

```cpp
void SetSplitBodies2(
   System.Object^ PathVar,
   System.Object^ FlagVar,
   System.Object^ BodyOrigin
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathVar`: Array of paths and file names of the part documents to which to save the split bodies in this Split feature
- `FlagVar`: Array of booleans indicating whether to consume each corresponding PathVar body; true to remove it from the original part, false to not
- `BodyOrigin`: Array of sketch points, vertices, or reference points indicating the origins of each PathVar body; null elements are also permitted

## VBA Syntax

See [SplitBodyFeatureData::SetSplitBodies2](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~SetSplitBodies2.html).

## Remarks

Call this method after calling [ISplitBodyFeatureData::GetSplitBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html) or [ISplitBodyFeatureData::IGetSplitBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.html) to change which split bodies to include in this Split feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[IFeatureManager::PreSplitBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody2.html)
[IFeatureManager::PostSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
