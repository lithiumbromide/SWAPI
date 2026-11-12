---
title: "GetUpperRight Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetUpperRight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetUpperRight.html"
---

# GetUpperRight Method (INote)

Gets the note's upper-right text point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpperRight() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Object

value = instance.GetUpperRight()
```

### C#

```csharp
System.object GetUpperRight()
```

### C++/CLI

```cpp
System.Object^ GetUpperRight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Note::GetUpperRight](ms-its:sldworksapivb6.chm::/sldworks~Note~GetUpperRight.html).

## Examples

[Get Upper-right Text Coordinates of Selected Note (VBA)](Get_Upper-right_Text_Coordinates_of_Selected_Note_Example_VB.htm)

## Remarks

Format of retval is the following array of 3 doubles:

- return value[0] = x coordinate of upper-right text point
- return value[1] = y coordinate of upper-right text point
- return value[2] = z coordinate of upper-right text point

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IGetUpperRight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetUpperRight.html)
