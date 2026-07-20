---
title: "Get3DViews Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Get3DViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViews.html"
---

# Get3DViews Method (IModelDocExtension)

Gets the 3D Views for this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DViews() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.Get3DViews()
```

### C#

```csharp
System.object Get3DViews()
```

### C++/CLI

```cpp
System.Object^ Get3DViews();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of

[IView3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView3D.html)

s

## VBA Syntax

See

[ModelDocExtension::Get3DViews](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Get3DViews.html)

.

## Remarks

This method requires that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html))

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

[IModelDocExtension::Refresh3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Refresh3DViews.html)

[IModelDocExtension::Capture3DView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Capture3DView.html)

[IModelDocExtension::Get3DView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DView.html)

[IModelDocExtension::Get3DViewCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewCount.html)

[IModelDocExtension::Get3DViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewNames.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
