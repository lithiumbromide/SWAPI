---
title: "IGetProfiles Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "IGetProfiles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetProfiles.html"
---

# IGetProfiles Method (ILoftFeatureData)

Gets the profiles associated with this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProfiles( _
   ByVal Count As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim Count As System.Short
Dim value As System.Object

value = instance.IGetProfiles(Count)
```

### C#

```csharp
System.object IGetProfiles(
   System.short Count
)
```

### C++/CLI

```cpp
System.Object^ IGetProfiles(
   System.short Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of profiles

### Return Value

- in-process, unmanaged C++: Pointer to an array of profiles of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ILoftFeatureData::GetProfileCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~GetProfileCount.html) to get the size of Count.

Each profile returned is a [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object. A [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) object can be extracted from this IFeature object by using [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Profiles.html)
[ILoftFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetProfiles.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
