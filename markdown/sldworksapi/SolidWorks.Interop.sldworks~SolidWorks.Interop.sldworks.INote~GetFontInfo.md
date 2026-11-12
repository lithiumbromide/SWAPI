---
title: "GetFontInfo Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetFontInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetFontInfo.html"
---

# GetFontInfo Method (INote)

Gets with the note's font information.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFontInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Object

value = instance.GetFontInfo()
```

### C#

```csharp
System.object GetFontInfo()
```

### C++/CLI

```cpp
System.Object^ GetFontInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles containing the font information (see **Remarks**)

## VBA Syntax

See [Note::GetFontInfo](ms-its:sldworksapivb6.chm::/sldworks~Note~GetFontInfo.html).

## Remarks

Currently this method returns only a line type index. See [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) for line type index information.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IGetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetFontInfo.html)
[INote::HasMultipleFonts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts.html)
[INote::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.html)
