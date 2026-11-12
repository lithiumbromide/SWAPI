---
title: "GetDeletedFaces Method (IDeleteFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteFaceFeatureData"
member: "GetDeletedFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFaces.html"
---

# GetDeletedFaces Method (IDeleteFaceFeatureData)

Get the faces of the DeleteFace feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDeletedFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteFaceFeatureData
Dim value As System.Object

value = instance.GetDeletedFaces()
```

### C#

```csharp
System.object GetDeletedFaces()
```

### C++/CLI

```cpp
System.Object^ GetDeletedFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [DeleteFaceFeatureData::GetDeletedFaces](ms-its:sldworksapivb6.chm::/sldworks~DeleteFaceFeatureData~GetDeletedFaces.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.html)
[IDeleteFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.html)
[IDeleteFaceFeatureData::GetDeletedFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFacesCount.html)
[IDeleteFaceFeatureData::IGetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces.html)
[IDeleteFaceFeatureData::ISetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~ISetDeletedFaces.html)
[IDeleteFaceFeatureData::SetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~SetDeletedFaces.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
