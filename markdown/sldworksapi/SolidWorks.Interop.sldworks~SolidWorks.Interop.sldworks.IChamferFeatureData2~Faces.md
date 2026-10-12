---
title: "Faces Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "Faces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Faces.html"
---

# Faces Property (IChamferFeatureData2)

Gets and sets a list of the faces to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Property Faces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Object

instance.Faces = value

value = instance.Faces
```

### C#

```csharp
System.object Faces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Faces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of IFace2

## VBA Syntax

See [ChamferFeatureData2::Faces](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~Faces.html).

## Examples

[Get Chamfer Distances (C#)](Get_Chamfer_Distances_Example_CSharp.htm)
[Get Chamfer Distances (VB.NET)](Get_Chamfer_Distances_Example_VBNET.htm)
[Get Chamfer Distances (VBA)](Get_Chamfer_Distances_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetFaceCount.html)
[IChamferFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetFaces.html)
[IChamferFeatureData2::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
