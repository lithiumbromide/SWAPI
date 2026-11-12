---
title: "IGetProfiles Method (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "IGetProfiles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~IGetProfiles.html"
---

# IGetProfiles Method (ILoftedBendsFeatureData)

Gets the profiles for this lofted bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProfiles( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetProfiles(Count)
```

### C#

```csharp
System.object IGetProfiles(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetProfiles(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of profiles

### Return Value

- in-process, unmanaged C++: Pointer to an array profiles of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ILoftedBendsFeatureData::GetProfileCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~GetProfileCount.html) before calling this method to get the size for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ISetProfiles.html)
[ILoftedBendsFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Profiles.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
