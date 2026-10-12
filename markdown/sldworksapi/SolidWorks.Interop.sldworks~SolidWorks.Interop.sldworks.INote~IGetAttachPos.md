---
title: "IGetAttachPos Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetAttachPos"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAttachPos.html"
---

# IGetAttachPos Method (INote)

Gets the attachment point of this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAttachPos() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Double

value = instance.IGetAttachPos()
```

### C#

```csharp
System.double IGetAttachPos()
```

### C++/CLI

```cpp
System.double IGetAttachPos();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This is only meaningful if the note is attached.

Format of return information is the following array of doubles:

- return value[0] = x-coord of attachment point
- return value[1] = y-coord of attachment point
- return value[2] = z-coord of attachment point

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAttachPos.html)
[INote::IsAttached Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.html)
[INote::LockPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.html)
