---
title: "IVisualizeAddinManager Interface"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager"
member: ""
kind: "interface"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html"
---

# IVisualizeAddinManager Interface

Allows access to the Visualize Addin Manager.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IVisualizeAddinManager
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager
```

### C#

```csharp
public interface IVisualizeAddinManager
```

### C++/CLI

```cpp
public interface class IVisualizeAddinManager
```

## VBA Syntax

See [IVisualizeAddinManager](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager.html).

## Examples

The example below demonstrates how to render a model using the API in a VBA macro.

'VBA

'=========================================================================
'Preconditions:
'1. Activate the SOLIDWORKS Visualize Add-in (**SOLIDWORKS Tools menu > Add-ins... > SOLIDWORKS Visualize**).
'2. Ensure that **E:\SOLIDWORKS Visualize Content\Images** exists.
'3. Open `public_documents`**\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\api\toaster.sldprt**.
'
'Postconditions:
'1. Depending on the complexity, the render can take some time.
'2. After the macro is finished, inspect **E:\SOLIDWORKS Visualize Content\Images\toaster\toaster.jpeg**.
'
'NOTE: Because the model is used elsewhere, do not save changes to it.
'================================================================================
Dim swApp As SldWorks.SldWorks
Dim testViz As IVisualizeAddin
Dim visualizeAddinMgr As IVisualizeAddinManager

Sub main()

' Get the Visualize add-in object

Set swApp = Application.SldWorks
Set testViz = swApp.**GetAddInObject**("SolidWorks.Visualize.Implementation.VisualizeAddin")
Set visualizeAddinMgr = testViz.**GetAddinManager**

' Set render options as needed

Set vizRenderOptions = visualizeAddinMgr.**RenderOptions**
vizRenderOptions.**ImageFormat** = ImageFormat_e.JPEG
vizRenderOptions.**FrameCount** = 1000
vizRenderOptions.**Width** = 800
vizRenderOptions.**Height** = 800
vizRenderOptions.**JobName** = "Toaster"
vizRenderOptions.**OutputFolder** = "E:\SOLIDWORKS Visualize Content\Images"
vizRenderOptions.**DenoiserEnabled** = False

' Render the model

Call visualizeAddinMgr.**Render**

End Sub

## Accessors

[IVisualizeAddin::GetAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddin~GetAddinManager.html)

## See Also

[IVisualizeAddinManager Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager_members.html)
[SolidWorks.Visualize.Interfaces Namespace](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces_namespace.html)
