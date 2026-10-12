---
title: "GetFaceCount Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "GetFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetFaceCount.html"
---

# GetFaceCount Method (IChamferFeatureData2)

Gets the number of faces that are chamfered.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Integer

value = instance.GetFaceCount()
```

### C#

```csharp
System.int GetFaceCount()
```

### C++/CLI

```cpp
System.int GetFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces

## VBA Syntax

See [ChamferFeatureData2::GetFaceCount](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~GetFaceCount.html).

## Examples

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

## Remarks

Call this method before calling [IChamferFeatureData2::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~IGetFaces.html).

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Faces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
