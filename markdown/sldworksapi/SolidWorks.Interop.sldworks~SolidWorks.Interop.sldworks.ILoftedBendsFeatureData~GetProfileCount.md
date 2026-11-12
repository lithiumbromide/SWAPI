---
title: "GetProfileCount Method (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "GetProfileCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~GetProfileCount.html"
---

# GetProfileCount Method (ILoftedBendsFeatureData)

Gets the number of profiles in this lofted bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfileCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer

value = instance.GetProfileCount()
```

### C#

```csharp
System.int GetProfileCount()
```

### C++/CLI

```cpp
System.int GetProfileCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of profiles

## VBA Syntax

See [LoftedBendsFeatureData::GetProfileCount](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~GetProfileCount.html).

## Examples

See examples for [ILoftedBendsFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData.html).

## Remarks

Call this method before calling [ILoftedBendsFeatureData::IGetProfiles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~IGetProfiles.html) to determine the size of the array for that method.

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ISetProfiles.html)
[ILoftedBendsFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Profiles.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
