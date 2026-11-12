---
title: "Faces Property (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "Faces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~Faces.html"
---

# Faces Property (IClosedCornerFeatureData)

Gets or sets the faces for this closed corner feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Faces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData
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

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that describe the closed corner

## VBA Syntax

See [ClosedCornerFeatureData::Faces](ms-its:sldworksapivb6.chm::/sldworks~ClosedCornerFeatureData~Faces.html).

## Examples

[Create and Modify Closed Corner Feature (C#)](Create_and_Modify_Closed_Corner_Feature_Example_CSharp.htm)
[Create and Modify Closed Corner Feature (VB.NET)](Create_and_Modify_Closed_Corner_Feature_Example_VBNET.htm)
[Create and Modify Closed Corner Feature (VBA)](Create_and_Modify_Closed_Corner_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)
[IClosedCornerFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~IGetFaces.html)
[IClosedCornerFeatureData::IGetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~IGetFacesCount.html)
[IClosedCornerFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~ISetFaces.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
