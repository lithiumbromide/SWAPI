---
title: "GetRenderMaterials2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetRenderMaterials2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials2.html"
---

# GetRenderMaterials2 Method (IComponent2)

Gets the appearances applied to this component in the specified display states.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRenderMaterials2( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Object

value = instance.GetRenderMaterials2(DisplayStateOption, DisplayStateNames)
```

### C#

```csharp
System.object GetRenderMaterials2(
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

### C++/CLI

```cpp
System.Object^ GetRenderMaterials2(
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateOption`: Display states as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)
- `DisplayStateNames`: Array of display state names

### Return Value

Array of [appearances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See [Component2::GetRenderMaterials2](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetRenderMaterials2.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetRenderMaterialsCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
