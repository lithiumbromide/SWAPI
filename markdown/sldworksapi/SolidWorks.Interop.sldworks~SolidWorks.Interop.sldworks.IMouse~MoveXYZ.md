---
title: "MoveXYZ Method (IMouse)"
project: "SOLIDWORKS API Help"
interface: "IMouse"
member: "MoveXYZ"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse~MoveXYZ.html"
---

# MoveXYZ Method (IMouse)

Moves the mouse pointer in the model space.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveXYZ( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Flags As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMouse
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Flags As System.Integer
Dim value As System.Boolean

value = instance.MoveXYZ(X, Y, Z, Flags)
```

### C#

```csharp
System.bool MoveXYZ(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Flags
)
```

### C++/CLI

```cpp
System.bool MoveXYZ(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Flags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate where to move the pointer
- `Y`: y coordinate where to move the pointer
- `Z`: z coordinate where to move the pointer
- `Flags`: Mouse command as defined in [swMouse_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swMouse_e.html) (see **Remarks**)

### Return Value

True if the pointer moved to the specified position, false if not

## VBA Syntax

See [Mouse::MoveXYZ](ms-its:sldworksapivb6.chm::/sldworks~Mouse~MoveXYZ.html).

## Examples

[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)

## Remarks

To use this method and access SOLIDWORKS commands, you must add a reference to SOLIDWORKS `version` Commands type library (substitute the actual SOLIDWORKS version number for `version`) or **SolidWorks.Interop.swcommands.dll**, typically installed in `install_dir`**\api\redist.**

The coordinate system is the model's coordinate system.

## See Also

[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.html)
[IMouse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
