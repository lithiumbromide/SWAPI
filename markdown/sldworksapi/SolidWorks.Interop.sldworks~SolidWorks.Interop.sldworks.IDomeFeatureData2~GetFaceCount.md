---
title: "GetFaceCount Method (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "GetFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~GetFaceCount.html"
---

# GetFaceCount Method (IDomeFeatureData2)

Gets the number of planar and non-planar faces of this dome feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
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

Number of planar and non-planar faces

## VBA Syntax

See [DomeFeatureData2::GetFaceCount](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~GetFaceCount.html).

## Examples

[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IDomeFeatureData2::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~IGetFaces.html).

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
[IDomeFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ISetFaces.html)
[IDomeFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
