---
title: "GetBodyBox Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetBodyBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.html"
---

# GetBodyBox Method (IBody2)

Gets the bounding box for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyBox() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetBodyBox()
```

### C#

```csharp
System.object GetBodyBox()
```

### C++/CLI

```cpp
System.Object^ GetBodyBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 6 doubles representing the extents of the bounding box (see **Remarks**)

## VBA Syntax

See [Body2::GetBodyBox](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetBodyBox.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## Remarks

The X,Y,Z points returned by SOLIDWORKS are the lower and upper diagonal corners which bound the body with the box sides parallel to the X, Y and Z axes. The box dimensions returned by SOLIDWORKS enclose the body and are typically close to the minimum possible size (this is typical, but not always true).

The return value is an array of doubles as follows:

**[** `XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2` **]**

**IMPORTANT:** The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.html)
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.html)
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.html)
[IComponent2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.html)
[IComponent2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.html)
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.html)
[IFace2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.html)
[IFeature::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.html)
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
