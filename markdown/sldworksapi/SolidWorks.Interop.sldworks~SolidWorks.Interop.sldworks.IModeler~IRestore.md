---
title: "IRestore Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IRestore"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore.html"
---

# IRestore Method (IModeler)

Obsolete. Superseded by [IModeler::IRestore2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IRestore2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IRestore( _
   ByVal StreamIn As System.Object _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim StreamIn As System.Object
Dim value As Body

value = instance.IRestore(StreamIn)
```

### C#

```csharp
Body IRestore(
   System.object StreamIn
)
```

### C++/CLI

```cpp
Body^ IRestore(
   System.Object^ StreamIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StreamIn`:

## VBA Syntax

See [Modeler::IRestore](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IRestore.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
