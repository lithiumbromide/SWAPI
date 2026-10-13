---
title: "IGetUpperRight Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetUpperRight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetUpperRight.html"
---

# IGetUpperRight Method (INote)

Gets the note's upper-right text point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUpperRight() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Double

value = instance.IGetUpperRight()
```

### C#

```csharp
System.double IGetUpperRight()
```

### C++/CLI

```cpp
System.double IGetUpperRight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Format of retval is the following array of 3 doubles:

- return value[0] = x coordinate of upper-right text point
- return value[1] = y coordinate of upper-right text point
- return value[2] = z coordinate of upper-right text point

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetUpperRight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetUpperRight.html)
