---
title: "OpenDocSilent Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "OpenDocSilent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDocSilent.html"
---

# OpenDocSilent Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OpenDocSilent( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByRef Errors As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim Errors As System.Integer
Dim value As System.Object

value = instance.OpenDocSilent(FileName, Type, Errors)
```

### C#

```csharp
System.object OpenDocSilent(
   System.string FileName,
   System.int Type,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.Object^ OpenDocSilent(
   System.String^ FileName,
   System.int Type,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:
- `Type`:
- `Errors`:

## VBA Syntax

See [SldWorks::OpenDocSilent](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~OpenDocSilent.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
