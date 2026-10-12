---
title: "SetDeletedFaces Method (IDeleteFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteFaceFeatureData"
member: "SetDeletedFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~SetDeletedFaces.html"
---

# SetDeletedFaces Method (IDeleteFaceFeatureData)

Sets the faces for the DeleteFace feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDeletedFaces( _
   ByVal Faces As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteFaceFeatureData
Dim Faces As System.Object
Dim value As System.Boolean

value = instance.SetDeletedFaces(Faces)
```

### C#

```csharp
System.bool SetDeletedFaces(
   System.object Faces
)
```

### C++/CLI

```cpp
System.bool SetDeletedFaces(
   System.Object^ Faces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Faces`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

### Return Value

True if the faces are set, false if not

## VBA Syntax

See [DeleteFaceFeatureData::SetDeletedFaces](ms-its:sldworksapivb6.chm::/sldworks~DeleteFaceFeatureData~SetDeletedFaces.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.html)
[IDeleteFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.html)
[IDeleteFaceFeatureData::GetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFaces.html)
[IDeleteFaceFeatureData::GetDeletedFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFacesCount.html)
[IDeleteFaceFeatureData::IGetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces.html)
[IDeleteFaceFeatureData::ISetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~ISetDeletedFaces.html)

## Availability

SolidWork 2010 FCS, Revision Number 18.0
