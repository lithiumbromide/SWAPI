---
title: "GetText Method (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "GetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~GetText.html"
---

# GetText Method (ICustomSymbol)

Obsolete. Superseded by [ISketchBlockDefinition::GetNoteCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetNoteCount.html) and [ISketchBlockDefinition::GetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetNotes.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetText( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim value As System.String

value = instance.GetText(Index)
```

### C#

```csharp
System.string GetText(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetText(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [CustomSymbol::GetText](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~GetText.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
