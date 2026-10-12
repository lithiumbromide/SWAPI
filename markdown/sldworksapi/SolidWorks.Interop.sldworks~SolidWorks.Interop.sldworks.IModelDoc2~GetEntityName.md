---
title: "GetEntityName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetEntityName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEntityName.html"
---

# GetEntityName Method (IModelDoc2)

Gets the name of the specified face, edge, or vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityName( _
   ByVal Entity As System.Object _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Entity As System.Object
Dim value As System.String

value = instance.GetEntityName(Entity)
```

### C#

```csharp
System.string GetEntityName(
   System.object Entity
)
```

### C++/CLI

```cpp
System.String^ GetEntityName(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

### Return Value

Name of the entity

## VBA Syntax

See [ModelDoc2::GetEntityName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetEntityName.html).

## Examples

[Select Component Face By Name (VBA)](Get_Component_Face_By_Name_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetEntityName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
