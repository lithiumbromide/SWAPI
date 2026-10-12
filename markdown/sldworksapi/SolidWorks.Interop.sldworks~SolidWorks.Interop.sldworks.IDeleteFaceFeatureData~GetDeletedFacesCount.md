---
title: "GetDeletedFacesCount Method (IDeleteFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteFaceFeatureData"
member: "GetDeletedFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFacesCount.html"
---

# GetDeletedFacesCount Method (IDeleteFaceFeatureData)

Gets the number of faces in the DeleteFace feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDeletedFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteFaceFeatureData
Dim value As System.Integer

value = instance.GetDeletedFacesCount()
```

### C#

```csharp
System.int GetDeletedFacesCount()
```

### C++/CLI

```cpp
System.int GetDeletedFacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces

## VBA Syntax

See [DeleteFaceFeatureData::GetDeletedFacesCount](ms-its:sldworksapivb6.chm::/sldworks~DeleteFaceFeatureData~GetDeletedFacesCount.html).

## Examples

[Insert and Change DeleteFace Features (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)
[Insert and Change DeleteFace Features (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IDeleteFaceFeatureData::IGetDeletedFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces.html) to determine the size of its array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.html)
[IDeleteFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.html)
[IDeleteFaceFeatureData::GetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFaces.html)
[IDeleteFaceFeatureData::IGetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces.html)
[IDeleteFaceFeatureData::ISetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~ISetDeletedFaces.html)
[IDeleteFaceFeatureData::SetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~SetDeletedFaces.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
