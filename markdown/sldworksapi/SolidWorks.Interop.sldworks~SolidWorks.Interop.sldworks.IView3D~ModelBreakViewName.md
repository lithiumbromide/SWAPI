---
title: "ModelBreakViewName Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "ModelBreakViewName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~ModelBreakViewName.html"
---

# ModelBreakViewName Property (IView3D)

Gets the name of the Model Break View in this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ModelBreakViewName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As System.String

value = instance.ModelBreakViewName
```

### C#

```csharp
System.string ModelBreakViewName {get;}
```

### C++/CLI

```cpp
property System.String^ ModelBreakViewName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the Model Break View in this 3D View

## VBA Syntax

See [View3D::ModelBreakViewName.](ms-its:sldworksapivb6.chm::/sldworks~View3D~ModelBreakViewName.html)

## Examples

[Capture 3D View (C#)](Capture_3DView_Example_CSharp.htm)
[Capture 3D View (VB.NET)](Capture_3DView_Example_VBNET.htm)
[Capture 3D View (VBA)](Capture_3DView_Example_VB.htm)

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)
[IModelDocExtension::GetModelBreakViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelBreakViewNames.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
