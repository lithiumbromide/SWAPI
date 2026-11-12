---
title: "RemoveVisibleBox Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RemoveVisibleBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html"
---

# RemoveVisibleBox Method (IModelDocExtension)

Removes the visible bounding box set by [IModelDocExtension::SetVisibleBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetVisibleBox.html) and resets the size of the bounding box to the size calculated by SOLIDWORKS for a part or an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveVisibleBox()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension

instance.RemoveVisibleBox()
```

### C#

```csharp
void RemoveVisibleBox()
```

### C++/CLI

```cpp
void RemoveVisibleBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDocExtension::RemoveVisibleBox](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RemoveVisibleBox.html).

## Examples

[Set Visible Bounding Box for Zoom to Fit (C#)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_CSharp.htm)
[Set Visible Bounding Box for Zoom to Fit (VB.NET)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VBNET.htm)
[Set Visible Bounding Box for Zoom to Fit (VBA)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
