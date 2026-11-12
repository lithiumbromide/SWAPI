---
title: "HasMultipleFonts Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "HasMultipleFonts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts.html"
---

# HasMultipleFonts Property (INote)

Gets whether a note contains multiple fonts.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasMultipleFonts As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

value = instance.HasMultipleFonts
```

### C#

```csharp
System.bool HasMultipleFonts {get;}
```

### C++/CLI

```cpp
property System.bool HasMultipleFonts {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the note contains multiple fonts, false if not

## VBA Syntax

See [Note::HasMultipleFonts](ms-its:sldworksapivb6.chm::/sldworks~Note~HasMultipleFonts.html).

## Examples

[Get Whether Note Contains Rich Embedded Text (VBA)](Get_Whether_Note_Contains_Rich-embedded_Text_Example_VB.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetFontInfo.html)
[INote::IGetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetFontInfo.html)
[INote::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
