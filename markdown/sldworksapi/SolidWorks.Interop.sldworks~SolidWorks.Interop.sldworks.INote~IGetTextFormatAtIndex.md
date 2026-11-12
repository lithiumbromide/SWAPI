---
title: "IGetTextFormatAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetTextFormatAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextFormatAtIndex.html"
---

# IGetTextFormatAtIndex Method (INote)

Obsolete. Superseded by [IAnnotation::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetTextFormat.html) and [IAnnotation::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextFormatAtIndex( _
   ByVal Index As System.Integer _
) As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As TextFormat

value = instance.IGetTextFormatAtIndex(Index)
```

### C#

```csharp
TextFormat IGetTextFormatAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
TextFormat^ IGetTextFormatAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [Note::IGetTextFormatAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~IGetTextFormatAtIndex.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
