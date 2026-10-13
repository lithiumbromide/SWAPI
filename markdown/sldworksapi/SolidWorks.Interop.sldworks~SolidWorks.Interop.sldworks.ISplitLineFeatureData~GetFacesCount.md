---
title: "GetFacesCount Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "GetFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetFacesCount.html"
---

# GetFacesCount Method (ISplitLineFeatureData)

Gets the number of faces split by this split line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Integer

value = instance.GetFacesCount()
```

### C#

```csharp
System.int GetFacesCount()
```

### C++/CLI

```cpp
System.int GetFacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces

## VBA Syntax

See [SplitLineFeatureData::GetFacesCount](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~GetFacesCount.html).

## Remarks

Call this method before calling [ISplitLineFeatureData::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~IGetFaces.html) to determine the size of the array for that method.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetFaces.html)
[ISplitLineFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Faces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
