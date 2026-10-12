---
title: "GetTextFormatAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetTextFormatAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFormatAtIndex.html"
---

# GetTextFormatAtIndex Method (INote)

Obsolete. Superseded by [IAnnotation::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetTextFormat.html) and [IAnnotation::IGetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextFormatAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetTextFormatAtIndex(Index)
```

### C#

```csharp
System.object GetTextFormatAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetTextFormatAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [Note::GetTextFormatAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetTextFormatAtIndex.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
