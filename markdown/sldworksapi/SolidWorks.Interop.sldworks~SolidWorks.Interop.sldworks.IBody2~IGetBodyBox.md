---
title: "IGetBodyBox Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetBodyBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.html"
---

# IGetBodyBox Method (IBody2)

Gets the bounding box for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetBodyBox( _
   ByRef BoxCorners As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim BoxCorners As System.Double

instance.IGetBodyBox(BoxCorners)
```

### C#

```csharp
void IGetBodyBox(
   ref System.double BoxCorners
)
```

### C++/CLI

```cpp
void IGetBodyBox(
   System.double% BoxCorners
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxCorners`: Pointer to an array of 6 doubles representing the extents of the bounding box (see **Remarks**)

## VBA Syntax

See [Body2::IGetBodyBox](ms-its:sldworksapivb6.chm::/sldworks~Body2~IGetBodyBox.html).

## Remarks

The X,Y,Z points returned by SOLIDWORKS are the lower and upper diagonal corners which bound the body with the box sides parallel to the X, Y and Z axes. The box dimensions returned by SOLIDWORKS enclose the body and are typically close to the minimum possible size (this is typical, but not always true).

The return value is an array of doubles as follows:

**[** `XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2` **]**

**IMPORTANT:** The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)
[IFeature::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.html)
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.html)
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.html)
[IFace2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.html)
[IComponent2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.html)
[IComponent2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.html)
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.html)
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
