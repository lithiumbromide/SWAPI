---
title: "Create3DBoundingBox Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Create3DBoundingBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Create3DBoundingBox.html"
---

# Create3DBoundingBox Method (IModelDocExtension)

Creates a 3D bounding box for a cut list item in a weldment part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Create3DBoundingBox()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension

instance.Create3DBoundingBox()
```

### C#

```csharp
void Create3DBoundingBox()
```

### C++/CLI

```cpp
void Create3DBoundingBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDocExtension::Create3DBoundingBox](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Create3DBoundingBox.html).

## Examples

[Create 3D Bounding Box for Cut List Item (VBA)](Create_3D_Bounding_Box_Example_VB.htm)
[Create 3D Bounding Box for Cut List Item (VB.NET)](Create_3D_Bounding_Box_Example_VBNET.htm)
[Create 3D Bounding Box for Cut List Item (C#)](Create_3D_Bounding_Box_Example_CSharp.htm)

## Remarks

After selecting the bounding box, [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html) returns [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelSKETCHES, while [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) returns an [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) instead of an [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
