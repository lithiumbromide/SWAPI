---
title: "OpenDoc Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "OpenDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc.html"
---

# OpenDoc Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OpenDoc( _
   ByVal Name As System.String, _
   ByVal Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Name As System.String
Dim Type As System.Integer
Dim value As System.Object

value = instance.OpenDoc(Name, Type)
```

### C#

```csharp
System.object OpenDoc(
   System.string Name,
   System.int Type
)
```

### C++/CLI

```cpp
System.Object^ OpenDoc(
   System.String^ Name,
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Type`:

## VBA Syntax

See [SldWorks::OpenDoc](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~OpenDoc.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
