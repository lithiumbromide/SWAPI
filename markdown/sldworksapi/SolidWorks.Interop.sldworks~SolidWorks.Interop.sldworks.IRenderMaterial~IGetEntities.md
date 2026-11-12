---
title: "IGetEntities Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "IGetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IGetEntities.html"
---

# IGetEntities Method (IRenderMaterial)

Gets the entities on which this appearance is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetEntities(Count)
```

### C#

```csharp
System.object IGetEntities(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of entities on which this appearance is applied

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IRenderMaterial::GetEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetEntitiesCount.html) to get the value of Count.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntities.html)
[IRenderMaterial::AddEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AddEntity.html)
[IRenderMaterial::RemoveAllEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RemoveAllEntities.html)
