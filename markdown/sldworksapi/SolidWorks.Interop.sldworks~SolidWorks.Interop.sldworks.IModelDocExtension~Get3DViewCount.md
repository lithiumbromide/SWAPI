---
title: "Get3DViewCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Get3DViewCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewCount.html"
---

# Get3DViewCount Method (IModelDocExtension)

Gets the number of

[3D Views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)

in this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DViewCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.Get3DViewCount()
```

### C#

```csharp
System.int Get3DViewCount()
```

### C++/CLI

```cpp
System.int Get3DViewCount();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Number of 3D Views

## VBA Syntax

See

[ModelDocExtension::Get3DViewCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Get3DViewCount.html)

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

[IModelDocExtension::Refresh3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Refresh3DViews.html)

[IModelDocExtension::Get3DView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DView.html)

[IModelDocExtension::Get3DViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewNames.html)

[IModelDocExtension::Get3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViews.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
