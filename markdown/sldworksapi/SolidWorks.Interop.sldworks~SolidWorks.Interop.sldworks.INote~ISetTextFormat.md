---
title: "ISetTextFormat Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "ISetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ISetTextFormat.html"
---

# ISetTextFormat Method (INote)

Obsolete. Superseded by [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html) and [IAnnotation::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ISetTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetTextFormat( _
   ByVal TextFormatType As System.Integer, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim TextFormatType As System.Integer
Dim TextFormat As TextFormat
Dim value As System.Boolean

value = instance.ISetTextFormat(TextFormatType, TextFormat)
```

### C#

```csharp
System.bool ISetTextFormat(
   System.int TextFormatType,
   TextFormat TextFormat
)
```

### C++/CLI

```cpp
System.bool ISetTextFormat(
   System.int TextFormatType,
   TextFormat^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TextFormatType`:
- `TextFormat`:

## VBA Syntax

See [Note::ISetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~Note~ISetTextFormat.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
