---
title: "IGetEntityName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetEntityName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetEntityName.html"
---

# IGetEntityName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetEntityName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetEntityName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntityName( _
   ByVal Entity As Entity _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
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

- `Entity`:

## VBA Syntax

See [ModelDoc::IGetEntityName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetEntityName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
