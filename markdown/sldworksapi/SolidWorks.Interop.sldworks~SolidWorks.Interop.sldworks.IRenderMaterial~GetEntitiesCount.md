---
title: "GetEntitiesCount Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntitiesCount.html"
---

# GetEntitiesCount Method (IRenderMaterial)

Gets the number of entities on which this appearance was applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

value = instance.GetEntitiesCount()
```

### C#

```csharp
System.int GetEntitiesCount()
```

### C++/CLI

```cpp
System.int GetEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities on which this appearance was applied

## VBA Syntax

See [RenderMaterial::GetEntitiesCount](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetEntitiesCount.html).

## Remarks

Call this method before calling [IRenderMaterial::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~IGetEntities.html) to get the size of the array for that method.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::AddEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AddEntity.html)
[IRenderMaterial::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntities.html)
[IRenderMaterial::RemoveAllEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RemoveAllEntities.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
