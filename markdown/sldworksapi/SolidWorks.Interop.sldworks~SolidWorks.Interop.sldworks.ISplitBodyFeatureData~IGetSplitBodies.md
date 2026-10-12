---
title: "IGetSplitBodies Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "IGetSplitBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.html"
---

# IGetSplitBodies Method (ISplitBodyFeatureData)

Gets the split bodies for this Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetSplitBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2, _
   ByRef PathArr As System.String, _
   ByRef FlagArr As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitBodyFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2
Dim PathArr As System.String
Dim FlagArr As System.Boolean

instance.IGetSplitBodies(Count, BodyArr, PathArr, FlagArr)
```

### C#

```csharp
void IGetSplitBodies(
   System.int Count,
   out Body2 BodyArr,
   out System.string PathArr,
   out System.bool FlagArr
)
```

### C++/CLI

```cpp
void IGetSplitBodies(
   System.int Count,
   [Out] Body2^ BodyArr,
   [Out] System.String^ PathArr,
   [Out] System.bool FlagArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of split bodies (see **Remarks**)
- `BodyArr`: - in-process, unmanaged C++: Pointer to an array of split [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `PathArr`: - in-process, unmanaged C++: Pointer to an array of paths and file names of part documents to which to save BodyArr bodies

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `FlagArr`: - in-process, unmanaged C++: Pointer to an array of booleans indicating whether corresponding BodyArr body is removed from the original part; true if removed, false if not
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISplitBodyFeatureData::GetSplitBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.html) to determine the value for Count. Call this method before calling [ISplitBodyFeatureData::SetSplitBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html) to change which split bodies to include in this Split feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::GetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html)
[IFeatureManager::PreSplitBody2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody2.html)
[IFeatureManager::PostSplitBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
