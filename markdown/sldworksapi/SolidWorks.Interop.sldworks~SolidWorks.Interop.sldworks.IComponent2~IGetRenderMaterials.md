---
title: "IGetRenderMaterials Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetRenderMaterials"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetRenderMaterials.html"
---

# IGetRenderMaterials Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetRenderMaterials2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRenderMaterials( _
   ByVal Count As System.Integer _
) As RenderMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Count As System.Integer
Dim value As RenderMaterial

value = instance.IGetRenderMaterials(Count)
```

### C#

```csharp
RenderMaterial IGetRenderMaterials(
   System.int Count
)
```

### C++/CLI

```cpp
RenderMaterial^ IGetRenderMaterials(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of appearances

### Return Value

- in-process, unmanaged C++: Pointer to an array of [appearances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IComponent2::GetRenderMaterialsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetRenderMaterialsCount.html) to get the value of Count.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
