---
title: "GetMassProperties2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetMassProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetMassProperties2.html"
---

# GetMassProperties2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetMassProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetMassProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassProperties2( _
   ByRef Status As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Status As System.Integer
Dim value As System.Object

value = instance.GetMassProperties2(Status)
```

### C#

```csharp
System.object GetMassProperties2(
   out System.int Status
)
```

### C++/CLI

```cpp
System.Object^ GetMassProperties2(
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Status`:

## VBA Syntax

See [ModelDoc::GetMassProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetMassProperties2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
