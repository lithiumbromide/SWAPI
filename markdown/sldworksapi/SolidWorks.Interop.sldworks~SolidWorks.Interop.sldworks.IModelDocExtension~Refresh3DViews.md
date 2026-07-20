---
title: "Refresh3DViews Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Refresh3DViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Refresh3DViews.html"
---

# Refresh3DViews Method (IModelDocExtension)

Updates the

[3D Views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)

of this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Refresh3DViews()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension

instance.Refresh3DViews()
```

### C#

```csharp
void Refresh3DViews()
```

### C++/CLI

```cpp
void Refresh3DViews();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[ModelDocExtension::Refresh3DViews](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Refresh3DViews.html)

.

## Examples

[Capture 3D View (VBA)](Capture_3DView_Example_VB.htm)

[Capture 3D View (VB.NET)](Capture_3DView_Example_VBNET.htm)

[Capture 3D View (C#)](Capture_3DView_Example_CSharp.htm)

## Remarks

This method requires that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html))

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IModelDocExtension::Capture3DView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Capture3DView.html)

[IModelDocExtension::Get3DView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DView.html)

[IModelDocExtension::Get3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViews.html)

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)

[IModelDocExtension::Get3DViewCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewCount.html)

[IModelDocExtension::Get3DViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewNames.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
