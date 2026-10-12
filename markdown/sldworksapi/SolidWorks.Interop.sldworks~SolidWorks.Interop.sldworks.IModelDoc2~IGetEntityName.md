---
title: "IGetEntityName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetEntityName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetEntityName.html"
---

# IGetEntityName Method (IModelDoc2)

Gets the name of the specified face, edge, or vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntityName( _
   ByVal Entity As Entity _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Entity As Entity
Dim value As System.String

value = instance.IGetEntityName(Entity)
```

### C#

```csharp
System.string IGetEntityName(
   Entity Entity
)
```

### C++/CLI

```cpp
System.String^ IGetEntityName(
   Entity^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

### Return Value

Name of the entity

## VBA Syntax

See [ModelDoc2::IGetEntityName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetEntityName.html).

## Examples

[Get Entity Name (C++)](Get_Entity_Name_Example_CPlusPlus_COM.htm)
[Get Named Entities (C++)](Get_Named_Entities_Example_CPlusPlus_COM.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEntityName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
