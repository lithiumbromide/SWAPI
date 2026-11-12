---
title: "GetPropertyExtension Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "GetPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~GetPropertyExtension.html"
---

# GetPropertyExtension Method (IBody)

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
Dim instance As IBody
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

See [Body::GetPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Body~GetPropertyExtension.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
