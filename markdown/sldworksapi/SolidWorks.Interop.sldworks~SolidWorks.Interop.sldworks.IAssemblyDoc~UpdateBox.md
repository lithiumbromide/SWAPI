---
title: "UpdateBox Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "UpdateBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateBox.html"
---

# UpdateBox Method (IAssemblyDoc)

Updates the bounding box for this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdateBox()
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc

instance.UpdateBox()
```

### C#

```csharp
void UpdateBox()
```

### C++/CLI

```cpp
void UpdateBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AssemblyDoc::UpdateBox](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~UpdateBox.html).

## Examples

[Recalculate Bounding Box (C#)](Recalculate_Bounding_Box_Example_CSharp.htm)
[Recalculate Bounding Box (VB.NET)](Recalculate_Bounding_Box_Example_VBNET.htm)
[Recalculate Bounding Box (VBA)](Recalculate_Bounding_Box_Example_VB.htm)

## Remarks

Use this method to help avoid clipping in shaded display mode if the assembly bounds change; for example, if you modify a component location using [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.html)
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html)
