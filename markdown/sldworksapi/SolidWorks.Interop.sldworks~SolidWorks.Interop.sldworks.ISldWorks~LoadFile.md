---
title: "LoadFile Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "LoadFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile.html"
---

# LoadFile Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::LoadFile4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadFile4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Boolean

value = instance.LoadFile(FileName)
```

### C#

```csharp
System.bool LoadFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool LoadFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [SldWorks::LoadFile](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~LoadFile.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
