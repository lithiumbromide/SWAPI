---
title: "OpenDoc4 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "OpenDoc4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc4.html"
---

# OpenDoc4 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OpenDoc4( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal Configuration As System.String, _
   ByRef Errors As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim Options As System.Integer
Dim Configuration As System.String
Dim Errors As System.Integer
Dim value As System.Object

value = instance.OpenDoc4(FileName, Type, Options, Configuration, Errors)
```

### C#

```csharp
System.object OpenDoc4(
   System.string FileName,
   System.int Type,
   System.int Options,
   System.string Configuration,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.Object^ OpenDoc4(
   System.String^ FileName,
   System.int Type,
   System.int Options,
   System.String^ Configuration,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:
- `Type`:
- `Options`:
- `Configuration`:
- `Errors`:

## VBA Syntax

See [SldWorks::OpenDoc4](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~OpenDoc4.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
