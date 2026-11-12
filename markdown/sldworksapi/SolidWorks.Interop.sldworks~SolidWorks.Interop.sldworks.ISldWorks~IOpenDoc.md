---
title: "IOpenDoc Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IOpenDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IOpenDoc.html"
---

# IOpenDoc Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IOpenDoc( _
   ByVal Name As System.String, _
   ByVal Type As System.Integer _
) As ModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String
Dim Type As System.Integer
Dim value As ModelDoc

value = instance.IOpenDoc(Name, Type)
```

### C#

```csharp
ModelDoc IOpenDoc(
   System.string Name,
   System.int Type
)
```

### C++/CLI

```cpp
ModelDoc^ IOpenDoc(
   System.String^ Name,
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Type`:

## VBA Syntax

See [SldWorks::IOpenDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IOpenDoc.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
