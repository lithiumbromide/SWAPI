---
title: "GetPropertyExtension Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension.html"
---

# GetPropertyExtension Method (IBody2)

Obsolete. Superseded by [IBody2::GetPropertyExtension2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetPropertyExtension2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyExtension( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ID As System.Integer
Dim value As System.Object

value = instance.GetPropertyExtension(ID)
```

### C#

```csharp
System.object GetPropertyExtension(
   System.int ID
)
```

### C++/CLI

```cpp
System.Object^ GetPropertyExtension(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:

## VBA Syntax

See [Body2::GetPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetPropertyExtension.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
