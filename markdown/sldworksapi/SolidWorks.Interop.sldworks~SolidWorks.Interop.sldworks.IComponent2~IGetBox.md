---
title: "IGetBox Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.html"
---

# IGetBox Method (IComponent2)

Gets the bounding box for component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBox( _
   ByVal IncludeRefPlanes As System.Boolean, _
   ByVal IncludeSketches As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim IncludeRefPlanes As System.Boolean
Dim IncludeSketches As System.Boolean
Dim value As System.Double

value = instance.IGetBox(IncludeRefPlanes, IncludeSketches)
```

### C#

```csharp
System.double IGetBox(
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

### C++/CLI

```cpp
System.double IGetBox(
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncludeRefPlanes`: True includes reference planes with the returned bounding box, false does not
- `IncludeSketches`: True includes sketches with the returned bounding box, false does not

### Return Value

Two diagonal points that bound the component; the format is a pointer to an array of 6 doubles

## Remarks

The resulting box encloses the object, but it might not be the tightest box.

The X, Y, Z points returned by SOLIDWORKS are the lower- and upper-diagonal corners that bound the component with the box sides parallel to the X, Y and Z axes. SOLIDWORKS returns box dimensions that enclose the component and are typically close to the minimum possible size.

The return value is an array of doubles as follows:

**[** `XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2` **]**

It is possible for this method to return S_false for COM or a NULL VARIANT for Dispatch. This occurs if your application calls IComponent2::IGetBox with a component that represented a subassembly and that subassembly is not loaded. Once the subassembly is loaded, SOLIDWORKS returns the correct bounds and IComponent2::IGetBox returns S_OK.

The user interface behavior is the same. When the user selects a subassembly that is not loaded, there is no selection box around the subassembly. However, once the subassembly is loaded, there is a selection box.

**IMPORTANT:** The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)
[IFeature::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.html)
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.html)
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.html)
[IFace2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.html)
[IBody2::GetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.html)
[IBody2::IGetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.html)
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.html)
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
