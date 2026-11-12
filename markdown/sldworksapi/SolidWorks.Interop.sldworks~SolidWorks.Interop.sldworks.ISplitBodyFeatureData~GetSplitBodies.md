---
title: "GetSplitBodies Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "GetSplitBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html"
---

# GetSplitBodies Method (ISplitBodyFeatureData)

Gets the split bodies in this Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSplitBodies( _
   ByRef BodyVar As System.Object, _
   ByRef PathVar As System.Object, _
   ByRef FlagVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim BodyVar As System.Object
Dim PathVar As System.Object
Dim FlagVar As System.Object

instance.GetSplitBodies(BodyVar, PathVar, FlagVar)
```

### C#

```csharp
void GetSplitBodies(
   out System.object BodyVar,
   out System.object PathVar,
   out System.object FlagVar
)
```

### C++/CLI

```cpp
void GetSplitBodies(
   [Out] System.Object^ BodyVar,
   [Out] System.Object^ PathVar,
   [Out] System.Object^ FlagVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyVar`: Array of split [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `PathVar`: Array of paths and file names of the part documents to which BodyVar bodies are saved; empty string if not saved
- `FlagVar`: Array of booleans indicating whether corresponding BodyVar bodies are consumed; true if removed from the original part, false if not

## VBA Syntax

See [SplitBodyFeatureData::GetSplitBodies](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~GetSplitBodies.html).

## Remarks

Call this method before calling [ISplitBodyFeatureData::SetSplitBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html) to change which split bodies to include in this Split feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::IGetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.html)
[ISplitBodyFeatureData::GetSplitBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.html)
[IFeatureManager::PostSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.html)
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
