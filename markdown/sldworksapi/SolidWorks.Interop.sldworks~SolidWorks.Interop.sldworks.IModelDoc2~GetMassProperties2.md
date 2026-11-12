---
title: "GetMassProperties2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetMassProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetMassProperties2.html"
---

# GetMassProperties2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetMassProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetMassProperties.html) and [IModelDocExtension::IGetMassProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetMassProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassProperties2( _
   ByRef Status As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::GetMassProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetMassProperties2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
