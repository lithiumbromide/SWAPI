---
title: "IGetMassProperties2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetMassProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetMassProperties2.html"
---

# IGetMassProperties2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::IGetMassProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetMassProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMassProperties2( _
   ByRef Status As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::IGetMassProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetMassProperties2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
