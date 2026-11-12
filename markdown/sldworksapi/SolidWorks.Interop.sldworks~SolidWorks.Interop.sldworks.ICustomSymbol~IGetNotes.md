---
title: "IGetNotes Method (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "IGetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~IGetNotes.html"
---

# IGetNotes Method (ICustomSymbol)

Obsolete. Superseded by [ISketchBlockDefinition::IGetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetNotes.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNotes( _
   ByVal Count As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim Count As System.Integer
Dim value As Note

value = instance.IGetNotes(Count)
```

### C#

```csharp
Note IGetNotes(
   System.int Count
)
```

### C++/CLI

```cpp
Note^ IGetNotes(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:

## VBA Syntax

See [CustomSymbol::IGetNotes](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~IGetNotes.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
