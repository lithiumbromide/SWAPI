---
title: "SetTextFormatAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "SetTextFormatAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextFormatAtIndex.html"
---

# SetTextFormatAtIndex Method (INote)

Obsolete. Superseded by [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html) and [IAnnotation::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ISetTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTextFormatAtIndex( _
   ByVal Index As System.Integer, _
   ByVal TextFormat As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim TextFormat As System.Object

instance.SetTextFormatAtIndex(Index, TextFormat)
```

### C#

```csharp
void SetTextFormatAtIndex(
   System.int Index,
   System.object TextFormat
)
```

### C++/CLI

```cpp
void SetTextFormatAtIndex(
   System.int Index,
   System.Object^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `TextFormat`:

## VBA Syntax

See [Note::SetTextFormatAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~SetTextFormatAtIndex.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
