---
title: "LockPosition Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "LockPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.html"
---

# LockPosition Property (INote)

Gets and sets whether to anchor this note.

## Syntax

### Visual Basic (Declaration)

```vb
Property LockPosition As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.LockPosition = value

value = instance.LockPosition
```

### C#

```csharp
System.bool LockPosition {get; set;}
```

### C++/CLI

```cpp
property System.bool LockPosition {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to anchor the note, false to not

## VBA Syntax

See [Note::LockPosition](ms-its:sldworksapivb6.chm::/sldworks~Note~LockPosition.html).

## Examples

[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)
[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[IAnnotation::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.html)
[IAnnotation::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.html)
[INote::GetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAttachPos.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
