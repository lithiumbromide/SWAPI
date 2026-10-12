---
title: "GetRenderStockReferences Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetRenderStockReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.html"
---

# GetRenderStockReferences Method (IModelDocExtension)

Gets the SOLIDWORKS-supplied (stock) render references for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRenderStockReferences() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetRenderStockReferences()
```

### C#

```csharp
System.object GetRenderStockReferences()
```

### C++/CLI

```cpp
System.Object^ GetRenderStockReferences();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Stock render references

## VBA Syntax

See [ModelDocExtension::GetRenderStockReferences](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetRenderStockReferences.html).

## Examples

[Get Render References (C#)](Get_Render_References_Example_CSharp.htm)
[Get Render References (VB.NET)](Get_Render_References_Example_VBNET.htm)
[Get Render References (VBA)](Get_Render_References_Example_VB.htm)
[Add and Remove Files from Pack and Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)
[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IModelDocExtension::InsertScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertScene.html)
[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
