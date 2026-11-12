---
title: "GetFacesForReplacementCount Method (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "GetFacesForReplacementCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetFacesForReplacementCount.html"
---

# GetFacesForReplacementCount Method (IReplaceFaceFeatureData)

Gets the number of faces to replace in this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesForReplacementCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IReplaceFaceFeatureData
Dim value As System.Integer

value = instance.GetFacesForReplacementCount()
```

### C#

```csharp
System.int GetFacesForReplacementCount()
```

### C++/CLI

```cpp
System.int GetFacesForReplacementCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces to replace

## VBA Syntax

See [ReplaceFaceFeatureData::GetFacesForReplacementCount](ms-its:sldworksapivb6.chm::/sldworks~ReplaceFaceFeatureData~GetFacesForReplacementCount.html).

## Examples

See the [IReplaceFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html) examples.

## Remarks

Call this method before calling [IReplaceFaceFeatureData::IGetFacesForReplacement](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReplaceFaceFeatureData~IGetFacesForReplacement.html).

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFaceFeatureData::ISetFacesForReplacement Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetFacesForReplacement.html)
[IReplaceFaceFeatureData::FacesForReplacement Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~FacesForReplacement.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
