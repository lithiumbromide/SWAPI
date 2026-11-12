---
title: "Faces Property (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "Faces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Faces.html"
---

# Faces Property (IDomeFeatureData2)

Gets or sets the planar or non-planar faces of this dome feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Faces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
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

Array of planar or non-planar [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of this dome feature

## VBA Syntax

See [DomeFeatureData2::Faces](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~Faces.html).

## Examples

[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

## Remarks

This property does not affect geometry until you call [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
[IDomeFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IGetFaces.html)
[IDomeFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ISetFaces.html)
[IDomeFeatureData2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~GetFaceCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
