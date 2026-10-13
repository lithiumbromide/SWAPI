---
title: "ISetProfiles Method (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "ISetProfiles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ISetProfiles.html"
---

# ISetProfiles Method (ILoftedBendsFeatureData)

Sets the profiles for this lofted bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetProfiles( _
   ByVal Count As System.Integer, _
   ByRef PDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim Count As System.Integer
Dim PDisp As System.Object

instance.ISetProfiles(Count, PDisp)
```

### C#

```csharp
void ISetProfiles(
   System.int Count,
   ref System.object PDisp
)
```

### C++/CLI

```cpp
void ISetProfiles(
   System.int Count,
   System.Object^% PDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of profiles
- `PDisp`: in-process, unmanaged C++: Pointer to an array of profiles of size Count

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::GetProfileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~GetProfileCount.html)
[ILoftedBendsFeatureData::IGetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~IGetProfiles.html)
[ILoftedBendsFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Profiles.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
