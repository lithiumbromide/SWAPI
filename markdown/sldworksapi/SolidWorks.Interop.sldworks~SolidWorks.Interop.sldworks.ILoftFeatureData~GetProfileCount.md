---
title: "GetProfileCount Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "GetProfileCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetProfileCount.html"
---

# GetProfileCount Method (ILoftFeatureData)

Gets the number of profiles associated with this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfileCount() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Short

value = instance.GetProfileCount()
```

### C#

```csharp
System.short GetProfileCount()
```

### C++/CLI

```cpp
System.short GetProfileCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of profiles

## VBA Syntax

See [LoftFeatureData::GetProfileCount](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~GetProfileCount.html).

## Remarks

Call this method before calling [ILoftFeatureData::IGetProfiles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~IGetProfiles.html) to determine the size of the array for that method.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::ISetProfiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetProfiles.html)
[ILoftFeatureData::Profiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Profiles.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
