---
title: "IGetBox Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.html"
---

# IGetBox Method (IFace2)

Gets the box boundaries for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBox() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Double

value = instance.IGetBox()
```

### C#

```csharp
System.double IGetBox()
```

### C++/CLI

```cpp
System.double IGetBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Two diagonal points that bound the component in the form of a pointer to an array of 6 doubles

## VBA Syntax

See [Face2::IGetBox](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetBox.html).

## Remarks

IMPORTANT: The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

The resulting box encloses the object, but it might not be the tightest box.

This method returns X,Y,Z points that are the lower and upper diagonal corners that bound the face with the box sides parallel to the X, Y and Z axes. The box dimensions enclose the face and are typically close to the minimum possible size, but this is not guaranteed.

The return value is an array of doubles as follows:

```vb
[ XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2 ]
```

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.html)
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.html)
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.html)
[IBody2::GetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.html)
[IBody2::IGetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.html)
[IComponent2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.html)
[IComponent2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.html)
[IFeature::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.html)
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
