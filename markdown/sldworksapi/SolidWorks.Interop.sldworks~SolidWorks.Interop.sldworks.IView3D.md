---
title: "IView3D Interface"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html"
---

# IView3D Interface

Allows access to a 3D View of a part or assembly.

**NOTE:**Click the**Members**link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IView3D
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
```

### C#

```csharp
public interface IView3D
```

### C++/CLI

```cpp
public interface class IView3D
```

## VBA Syntax

See

[View3D](ms-its:sldworksapivb6.chm::/sldworks~View3D.html)

.

## Examples

[Capture 3D View (VBA)](Capture_3DView_Example_VB.htm)

[Capture 3D View (VB.NET)](Capture_3DView_Example_VBNET.htm)

[Capture 3D View (C#)](Capture_3DView_Example_CSharp.htm)

## Remarks

This interface supports SOLIDWORKS Model Based Definition (MBD), which is an integrated drawingless manufacturing solution for SOLIDWORKS. Use[ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html)to load the MBD add-in.

See the SOLIDWORKS Help for details about MBD.

## Accessors

[IModelDocExtension::Capture3DView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Capture3DView.html)

[IModelDocExtension::Get3DView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Get3DView.html)

[IModelDocExtension::Get3DViews](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Get3DViews.html)

## Access Diagram

[View3D](SWObjectModel.pdf#View3D)

## See Also

[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IModelDocExtension::Get3DViewCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewCount.html)

[IModelDocExtension::Get3DViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewNames.html)

[IModelDocExtension::Refresh3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Refresh3DViews.html)

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
