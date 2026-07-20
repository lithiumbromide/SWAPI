---
title: "Capture3DView Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Capture3DView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Capture3DView.html"
---

# Capture3DView Method (IModelDocExtension)

Captures the 3D View of this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function Capture3DView() As View3D
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As View3D

value = instance.Capture3DView()
```

### C#

```csharp
View3D Capture3DView()
```

### C++/CLI

```cpp
View3D^ Capture3DView();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

[IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html)

## VBA Syntax

See

[ModelDocExtension::Capture3DView](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Capture3DView.html)

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

[IModelDocExtension::Get3DView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DView.html)

[IModelDocExtension::Get3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViews.html)

[IModelDocExtension::Refresh3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Refresh3DViews.html)

[IModelDocExtension::Get3DViewCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewCount.html)

[IModelDocExtension::Get3DViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewNames.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
