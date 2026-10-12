---
title: "GetRenderMaterialsCount Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetRenderMaterialsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterialsCount.html"
---

# GetRenderMaterialsCount Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetRenderMaterialsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetRenderMaterialsCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRenderMaterialsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetRenderMaterialsCount()
```

### C#

```csharp
System.int GetRenderMaterialsCount()
```

### C++/CLI

```cpp
System.int GetRenderMaterialsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of appearances

## VBA Syntax

See [Component2::GetRenderMaterialsCount](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetRenderMaterialsCount.html).

## Remarks

Call this method before calling [IComponent::IGetRenderMaterials](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetRenderMaterials.html) to get the size of the array for that method.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRenderMaterials.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
