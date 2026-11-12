---
title: "CreateBodyFromBox3 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateBodyFromBox3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox3.html"
---

# CreateBodyFromBox3 Method (IModeler)

Creates a temporary body from the specified box dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBodyFromBox3( _
   ByVal BoxDimArray As System.Object _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim BoxDimArray As System.Object
Dim value As Body2

value = instance.CreateBodyFromBox3(BoxDimArray)
```

### C#

```csharp
Body2 CreateBodyFromBox3(
   System.object BoxDimArray
)
```

### C++/CLI

```cpp
Body2^ CreateBodyFromBox3(
   System.Object^ BoxDimArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxDimArray`: Array of 9 doubles (see Remarks)

### Return Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [IModeler::CreateBodyFromBox3](ms-its:sldworksapivb6.chm::/Sldworks~Modeler~CreateBodyFromBox3.html).

## Examples

[Create Multibody Macro Feature (VBA)](Create_Multibody_Macro_Feature_Example_VB.htm)
[Create Multibody Macro Feature (VB.NET)](Create_Multibody_Macro_Feature_Example_VBNET.htm)
[Create Multibody Macro Feature (C#)](Create_Multibody_Macro_Feature_Example_CSharp.htm)

## Remarks

The input parameter is the following array of doubles:

[ boxFaceCenter[3], boxAxis[3], boxWidth, boxLength, boxHeight ]

where:

| boxFaceCenter [3] | XYZ location that represents the center of one of the box faces. |
| --- | --- |
| boxAxis [3] | XYZ direction. The box will be extruded along this vector from the boxFaceCenter location , a distance of boxHeight. |
| boxWidth | Box width. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the X-axis; the new body is rotated to the input boxAxis direction and translates it to the boxFaceCenter . |
| boxLength | Box length. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the Y axis; the new body is rotated to the input boxAxis direction and translates it to the boxFaceCenter . |
| boxHeight | Height to extrude along the boxAxis direction. If boxHeight is 0, a sheet body and whose normal is defined by boxAxis . |

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IFeature::ISetBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.html)
[IFeature::SetBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody2.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
