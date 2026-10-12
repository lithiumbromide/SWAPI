---
title: "GetFrameSymbols Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFrameSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols.html"
---

# GetFrameSymbols Method (IGtol)

Obsolete. Superseded by [IGtol::GetFrameSymbols2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetFrameSymbols2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameSymbols( _
   ByVal FrameNumber As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim value As System.Object

value = instance.GetFrameSymbols(FrameNumber)
```

### C#

```csharp
System.object GetFrameSymbols(
   System.short FrameNumber
)
```

### C++/CLI

```cpp
System.Object^ GetFrameSymbols(
   System.short FrameNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`:

## VBA Syntax

See [Gtol::GetFrameSymbols](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFrameSymbols.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
