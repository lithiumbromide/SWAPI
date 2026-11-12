---
title: "ISetSplitBodies Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "ISetSplitBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetSplitBodies.html"
---

# ISetSplitBodies Method (ISplitBodyFeatureData)

Obsolete. Superseded by [ISplitBodyFeatureData::SetSplitBodies2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSplitBodies( _
   ByVal Count As System.Integer, _
   ByRef PathArr As System.String, _
   ByRef FlagArr As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim Count As System.Integer
Dim PathArr As System.String
Dim FlagArr As System.Boolean

instance.ISetSplitBodies(Count, PathArr, FlagArr)
```

### C#

```csharp
void ISetSplitBodies(
   System.int Count,
   ref System.string PathArr,
   ref System.bool FlagArr
)
```

### C++/CLI

```cpp
void ISetSplitBodies(
   System.int Count,
   System.String^% PathArr,
   System.bool% FlagArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of split bodies for this Split feature
- `PathArr`: - in-process, unmanaged C++: Pointer to an array of paths and file names of the split bodies

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `FlagArr`: - in-process, unmanaged C++: Pointer to an array of booleans indicating whether corresponding PathArr bodies are consumed; true indicates the body is removed from the original part, false otherwise
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::SetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies.html)
[ISplitBodyFeatureData::GetSplitBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.html)
[ISplitBodyFeatureData::IGetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.html)
[ISplitBodyFeatureData::GetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
