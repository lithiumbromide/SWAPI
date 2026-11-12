---
title: "IGetNext Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext.html"
---

# IGetNext Method (INote)

Gets the next note in [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As Note
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As Note

value = instance.IGetNext()
```

### C#

```csharp
Note IGetNext()
```

### C++/CLI

```cpp
Note^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [Note::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~Note~IGetNext.html).

## Remarks

The sheet must be visible. See [ISheet::SheetFormatVisible.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.html)
