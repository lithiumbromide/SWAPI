---
title: "ISetTextFormatAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "ISetTextFormatAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ISetTextFormatAtIndex.html"
---

# ISetTextFormatAtIndex Method (INote)

Obsolete. Superseded by [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html) and [IAnnotation::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ISetTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetTextFormatAtIndex( _
   ByVal Index As System.Integer, _
   ByVal TextFormat As TextFormat _
)
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim TextFormat As TextFormat

instance.ISetTextFormatAtIndex(Index, TextFormat)
```

### C#

```csharp
void ISetTextFormatAtIndex(
   System.int Index,
   TextFormat TextFormat
)
```

### C++/CLI

```cpp
void ISetTextFormatAtIndex(
   System.int Index,
   TextFormat^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:
- `TextFormat`:

## VBA Syntax

See [Note::ISetTextFormatAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~ISetTextFormatAtIndex.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
