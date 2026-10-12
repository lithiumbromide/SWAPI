---
title: "IGetFaces Method (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~IGetFaces.html"
---

# IGetFaces Method (IHealEdgesFeatureData)

Gets the faces whose edges to heal.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IHealEdgesFeatureData
Dim Count As System.Integer
Dim value As Face2

value = instance.IGetFaces(Count)
```

### C#

```csharp
Face2 IGetFaces(
   System.int Count
)
```

### C++/CLI

```cpp
Face2^ IGetFaces(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces whose edges to heal

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) whose edges to heal
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IHealEdgesFeatureData::GetFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHealEdgesFeatureData~GetFacesCount.html) before using this method.

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)
[IHealEdgesFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~ISetFaces.html)
[IHealEdgesFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
