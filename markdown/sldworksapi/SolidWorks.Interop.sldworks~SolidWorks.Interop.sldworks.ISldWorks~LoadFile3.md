---
title: "LoadFile3 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "LoadFile3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile3.html"
---

# LoadFile3 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::LoadFile4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadFile4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadFile3( _
   ByVal FileName As System.String, _
   ByVal ArgString As System.String, _
   ByVal ImportData As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim ArgString As System.String
Dim ImportData As System.Object
Dim value As System.Boolean

value = instance.LoadFile3(FileName, ArgString, ImportData)
```

### C#

```csharp
System.bool LoadFile3(
   System.string FileName,
   System.string ArgString,
   System.object ImportData
)
```

### C++/CLI

```cpp
System.bool LoadFile3(
   System.String^ FileName,
   System.String^ ArgString,
   System.Object^ ImportData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:
- `ArgString`:
- `ImportData`:

## VBA Syntax

See [SldWorks::LoadFile3](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~LoadFile3.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
