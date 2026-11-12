---
title: "IGetBox Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IGetBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.html"
---

# IGetBox Method (IAssemblyDoc)

Gets the bounding box.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBox( _
   ByVal Options As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Options As System.Integer
Dim value As System.Double

value = instance.IGetBox(Options)
```

### C#

```csharp
System.double IGetBox(
   System.int Options
)
```

### C++/CLI

```cpp
System.double IGetBox(
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Type of bounding box as defined by [swBoundingBoxOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBoundingBoxOptions_e.html)

### Return Value

Two diagonal points that bound the object; the format is a pointer to an array of 6 doubles (see **Remarks**)

## VBA Syntax

See [AssemblyDoc::IGetBox](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IGetBox.html).

## Remarks

**IMPORTANT:** The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.The resulting box encloses the object, but it might not be the tightest box.

The X, Y, Z points returned by SOLIDWORKS are the lower- and upper-diagonal corners that bound the component with the box sides parallel to the X, Y and Z axes. SOLIDWORKS returns box dimensions that enclose the object and are typically close to the minimum possible size.

The return value is an array of doubles as follows:

**[** `XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2` **]**

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.html)
[IComponent2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)
[IAssemblyDoc::UpdateBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateBox.html)
[IFeature::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.html)
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.html)
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetBox.html)
[IFace2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetBox.html)
[IComponent2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.html)
[IBody2::GetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.html)
[IBody2::IGetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
