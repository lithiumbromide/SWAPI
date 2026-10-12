---
title: "Move Method (IMouse)"
project: "SOLIDWORKS API Help"
interface: "IMouse"
member: "Move"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse~Move.html"
---

# Move Method (IMouse)

Moves the mouse pointer in the window space.

## Syntax

### Visual Basic (Declaration)

```vb
Function Move( _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal Flags As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMouse
Dim X As System.Integer
Dim Y As System.Integer
Dim Flags As System.Integer
Dim value As System.Boolean

value = instance.Move(X, Y, Flags)
```

### C#

```csharp
System.bool Move(
   System.int X,
   System.int Y,
   System.int Flags
)
```

### C++/CLI

```cpp
System.bool Move(
   System.int X,
   System.int Y,
   System.int Flags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate where to move the pointer
- `Y`: y coordinate where to move the pointer
- `Flags`: Mouse command as defined in [swMouse_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swMouse_e.html) (see **Remarks**)

### Return Value

True if the pointer moves to the specified position, false if not

## VBA Syntax

See [Mouse::Move](ms-its:sldworksapivb6.chm::/sldworks~Mouse~Move.html).

## Examples

[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)

## Remarks

To use this method and access SOLIDWORKS commands, you must add a reference to SOLIDWORKS `version` Commands type library (substitute the actual SOLIDWORKS version number for `version`) or **SolidWorks.Interop.swcommands.dll**, typically installed in `install_dir`**\api\redist.**

In window space, the origin of the coordinate system is the upper-left corner of the window. Positive x is to the right; positive y is down.

## See Also

[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.html)
[IMouse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
