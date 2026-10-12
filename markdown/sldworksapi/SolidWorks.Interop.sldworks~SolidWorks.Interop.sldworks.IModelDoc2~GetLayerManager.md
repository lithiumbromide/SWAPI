---
title: "GetLayerManager Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetLayerManager"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLayerManager.html"
---

# GetLayerManager Method (IModelDoc2)

Gets the layer manager for the current drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLayerManager() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetLayerManager()
```

### C#

```csharp
System.object GetLayerManager()
```

### C++/CLI

```cpp
System.Object^ GetLayerManager();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Layer manager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr.html)

## VBA Syntax

See [ModelDoc2::GetLayerManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetLayerManager.html).

## Examples

[Determine If Layer Is Visible (VBA)](Determine_if_Layer_is_Visible_Example_VB.htm)
[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (C#)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetLayerManager Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetLayerManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
