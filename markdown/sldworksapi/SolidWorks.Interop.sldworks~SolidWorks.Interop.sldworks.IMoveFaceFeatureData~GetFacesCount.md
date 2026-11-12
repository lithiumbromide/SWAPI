---
title: "GetFacesCount Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "GetFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetFacesCount.html"
---

# GetFacesCount Method (IMoveFaceFeatureData)

Gets the number of faces for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
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

See [MoveFaceFeatureData::GetFacesCount](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~GetFacesCount.html).

## Remarks

Call this method before calling [IMoveFaceFeatureData::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveFaceFeatureData~IGetFaces.html) to dimension that method's array.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetFaces.html)
[IMoveFaceFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
