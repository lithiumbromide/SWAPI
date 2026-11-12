---
title: "LoadFile2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "LoadFile2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile2.html"
---

# LoadFile2 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::LoadFile4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadFile4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadFile2( _
   ByVal FileName As System.String, _
   ByVal ArgString As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim ArgString As System.String
Dim value As System.Boolean

value = instance.LoadFile2(FileName, ArgString)
```

### C#

```csharp
System.bool LoadFile2(
   System.string FileName,
   System.string ArgString
)
```

### C++/CLI

```cpp
System.bool LoadFile2(
   System.String^ FileName,
   System.String^ ArgString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:
- `ArgString`:

## VBA Syntax

See [SldWorks::LoadFile2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~LoadFile2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
