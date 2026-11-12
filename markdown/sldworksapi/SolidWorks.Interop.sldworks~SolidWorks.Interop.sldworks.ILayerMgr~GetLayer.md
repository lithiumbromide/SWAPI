---
title: "GetLayer Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "GetLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayer.html"
---

# GetLayer Method (ILayerMgr)

Gets the specified layer in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLayer( _
   ByVal NameIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim NameIn As System.String
Dim value As System.Object

value = instance.GetLayer(NameIn)
```

### C#

```csharp
System.object GetLayer(
   System.string NameIn
)
```

### C++/CLI

```cpp
System.Object^ GetLayer(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Layer name

### Return Value

Layer

## VBA Syntax

See [LayerMgr::GetLayer](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~GetLayer.html).

## Examples

[Determine If Layer Is Visible (VBA)](Determine_if_Layer_is_Visible_Example_VB.htm)
[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## Remarks

You can get the layer name by calling [ILayerMgr::GetCurrentLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetCurrentLayer.html), create a new layer calling [ILayerMgr::AddLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~AddLayer.html), or obtain a list of layer names by calling [ILayerMgr::GetLayerList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerList.html).

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::IGetLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayer.html)

## Availability

SOLIDWORKS 99, Revision Number 1999207
