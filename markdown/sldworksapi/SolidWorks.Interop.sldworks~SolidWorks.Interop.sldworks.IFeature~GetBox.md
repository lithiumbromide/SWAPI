---
title: "GetBox Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.html"
---

# GetBox Method (IFeature)

Gets the bounding box for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBox( _
   ByRef BBox As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim BBox As System.Object
Dim value As System.Boolean

value = instance.GetBox(BBox)
```

### C#

```csharp
System.bool GetBox(
   out System.object BBox
)
```

### C++/CLI

```cpp
System.bool GetBox(
   [Out] System.Object^ BBox
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BBox`: Array containing the two diagonal points

### Return Value

True if the operation was successful, false if not

## VBA Syntax

See [Feature::GetBox](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetBox.html).

## Examples

[Get Bounding Box (C#)](Get_Bounding_Box_Example_CSharp.htm)
[Get Bounding Box (VB.NET)](Get_Bounding_Box_Example_VBNET.htm)
[Get Bounding Box (VBA)](Get_Bounding_Box_Example_VB.htm)

## Remarks

IMPORTANT: The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

The resulting box encloses the object, but it might not be the tightest box.

The two X, Y, Z points returned are the lower- and upper-diagonal corners that bound the feature. The box is aligned with the model coordinate system. The box dimensions enclose the feature. However, the box might not be the minimum bounding box for the model.

The return value is an array of 6 doubles as follows:

[ XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2 ]

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.html)
[IBody2::GetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.html)
[IBody2::IGetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.html)
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.html)
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.html)
[IFace2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.html)
[IComponent2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.html)
[IComponent2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
