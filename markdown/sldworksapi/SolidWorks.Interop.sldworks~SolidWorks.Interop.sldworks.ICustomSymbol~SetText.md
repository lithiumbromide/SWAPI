---
title: "SetText Method (ICustomSymbol)"
project: "SOLIDWORKS API Help"
interface: "ICustomSymbol"
member: "SetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol~SetText.html"
---

# SetText Method (ICustomSymbol)

Obsolete. Superseded by [ISketchBlockDefintion::GetNoteCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetNoteCount.html) and [ISketchBlockDefinition::GetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetNotes.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetText( _
   ByVal Index As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomSymbol
Dim Index As System.Integer
Dim Text As System.String
Dim value As System.Boolean

value = instance.SetText(Index, Text)
```

### C#

```csharp
System.bool SetText(
   System.int Index,
   System.string Text
)
```

### C++/CLI

```cpp
System.bool SetText(
   System.int Index,
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `Text`:

## VBA Syntax

See [CustomSymbol::SetText](ms-its:sldworksapivb6.chm::/sldworks~CustomSymbol~SetText.html).

## See Also

[ICustomSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol.html)
[ICustomSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomSymbol_members.html)
