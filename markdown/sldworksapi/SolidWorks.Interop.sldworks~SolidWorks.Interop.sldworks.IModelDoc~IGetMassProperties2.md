---
title: "IGetMassProperties2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetMassProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetMassProperties2.html"
---

# IGetMassProperties2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetMassProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetMassProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMassProperties2( _
   ByRef Status As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Status As System.Integer
Dim value As System.Double

value = instance.IGetMassProperties2(Status)
```

### C#

```csharp
System.double IGetMassProperties2(
   out System.int Status
)
```

### C++/CLI

```cpp
System.double IGetMassProperties2(
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Status`:

## VBA Syntax

See [ModelDoc::IGetMassProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetMassProperties2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
