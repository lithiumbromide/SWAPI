---
title: "GetEntityName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetEntityName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetEntityName.html"
---

# GetEntityName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetEntityName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityName( _
   ByVal Entity As System.Object _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
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

- `Entity`:

## VBA Syntax

See [ModelDoc::GetEntityName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetEntityName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
