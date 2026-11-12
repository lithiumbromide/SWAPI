---
title: "ISetProfiles Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "ISetProfiles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetProfiles.html"
---

# ISetProfiles Method (ILoftFeatureData)

Sets the profiles for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetProfiles( _
   ByVal Count As System.Short, _
   ByRef PDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim Count As System.Short
Dim PDisp As System.Object

instance.ISetProfiles(Count, PDisp)
```

### C#

```csharp
void ISetProfiles(
   System.short Count,
   ref System.object PDisp
)
```

### C++/CLI

```cpp
void ISetProfiles(
   System.short Count,
   System.Object^% PDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of profiles
- `PDisp`: - in-process, unmanaged C++: Pointer to an array of profiles of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Each profile is an [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object that contains a [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetProfileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetProfileCount.html)
[ILoftFeatureData::IGetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetProfiles.html)
[ILoftFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Profiles.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
