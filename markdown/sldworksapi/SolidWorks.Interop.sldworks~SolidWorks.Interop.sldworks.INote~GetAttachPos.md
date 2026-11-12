---
title: "GetAttachPos Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetAttachPos"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAttachPos.html"
---

# GetAttachPos Method (INote)

Gets the attachment point of this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachPos() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Object

value = instance.GetAttachPos()
```

### C#

```csharp
System.object GetAttachPos()
```

### C++/CLI

```cpp
System.Object^ GetAttachPos();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Note::GetAttachPos](ms-its:sldworksapivb6.chm::/sldworks~Note~GetAttachPos.html).

## Examples

[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)

## Remarks

This is only meaningful if the note is attached.

Format of return information is the following array of doubles:

- return value[0] = x-coord of attachment point
- return value[1] = y-coord of attachment point
- return value[2] = z-coord of attachment point

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IGetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAttachPos.html)
[INote::IsAttached Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.html)
[INote::LockPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.html)
