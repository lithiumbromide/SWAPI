---
title: "SetSplitBodies Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "SetSplitBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies.html"
---

# SetSplitBodies Method (ISplitBodyFeatureData)

Obsolete. Superseded by [ISplitBodyFeatureData::SetSplitBodies2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSplitBodies( _
   ByVal PathVar As System.Object, _
   ByVal FlagVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim PathVar As System.Object
Dim FlagVar As System.Object

instance.SetSplitBodies(PathVar, FlagVar)
```

### C#

```csharp
void SetSplitBodies(
   System.object PathVar,
   System.object FlagVar
)
```

### C++/CLI

```cpp
void SetSplitBodies(
   System.Object^ PathVar,
   System.Object^ FlagVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathVar`: Array of full paths and file names of the split bodies
- `FlagVar`: Array of Booleans indicating whether to include a body in this split-body feature

## VBA Syntax

See [SplitBodyFeatureData::SetSplitBodies](ms-its:sldworksapivb6.chm::/sldworks~SplitBodyFeatureData~SetSplitBodies.html).

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::ISetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetSplitBodies.html)
[ISplitBodyFeatureData::GetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html)
[ISplitBodyFeatureData::GetSplitBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.html)
[ISplitBodyFeatureData::IGetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
