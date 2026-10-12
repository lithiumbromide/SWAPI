---
title: "GetLayerList Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "GetLayerList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerList.html"
---

# GetLayerList Method (ILayerMgr)

Gets a list of layers in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLayerList() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim value As System.Object

value = instance.GetLayerList()
```

### C#

```csharp
System.object GetLayerList()
```

### C++/CLI

```cpp
System.Object^ GetLayerList();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings containing the name of each [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object in this [ILayerMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr.html) object

## VBA Syntax

See [LayerMgr::GetLayerList](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~GetLayerList.html).

## Examples

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## Remarks

This is a 0-based array (first element is at position 0).

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::IGetLayerList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerList.html)

## Availability

SOLIDWORKS 99, datecode 1999207
