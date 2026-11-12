---
title: "IGetFontInfo Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetFontInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetFontInfo.html"
---

# IGetFontInfo Method (INote)

Gets with the note's font information.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFontInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Double

value = instance.IGetFontInfo()
```

### C#

```csharp
System.double IGetFontInfo()
```

### C++/CLI

```cpp
System.double IGetFontInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Currently this method returns only a line type index. See [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) for line type index information.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.html)
[INote::GetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetFontInfo.html)
[INote::HasMultipleFonts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts.html)
