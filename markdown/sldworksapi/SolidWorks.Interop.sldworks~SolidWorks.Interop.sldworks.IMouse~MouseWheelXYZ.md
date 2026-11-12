---
title: "MouseWheelXYZ Method (IMouse)"
project: "SOLIDWORKS API Help"
interface: "IMouse"
member: "MouseWheelXYZ"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse~MouseWheelXYZ.html"
---

# MouseWheelXYZ Method (IMouse)

Zoom in or zoom out using the mouse.

## Syntax

### Visual Basic (Declaration)

```vb
Function MouseWheelXYZ( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Clicks As System.Integer, _
   ByVal Flags As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMouse
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Clicks As System.Integer
Dim Flags As System.Integer
Dim value As System.Boolean

value = instance.MouseWheelXYZ(X, Y, Z, Clicks, Flags)
```

### C#

```csharp
System.bool MouseWheelXYZ(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Clicks,
   System.int Flags
)
```

### C++/CLI

```cpp
System.bool MouseWheelXYZ(
   System.double X,
   System.double Y,
   System.double Z,
   System.int Clicks,
   System.int Flags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate where to move the pointer
- `Y`: y coordinate where to move the pointer
- `Z`: z coordinate where to move the pointer
- `Clicks`: Number of clicks to zoom in and out; specify -120 to to zoom in one click and specify 120 to to zoom out
- `Flags`: Mouse command as defined in [swMouse_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swMouse_e.html) (see **Remarks**)

### Return Value

True if the operation succeeded, false if not

## VBA Syntax

See [Mouse::MouseWheelXYZ](ms-its:sldworksapivb6.chm::/sldworks~Mouse~MouseWheelXYZ.html).

## Examples

**Visual Basic for Applications (VBA)**

'--------------------------------
' Preconditions: Model document is open.
'
' Postconditions: Model is zoomed in and out.
**'--------------------------------**

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelView As SldWorks.ModelView
Dim swMouse As SldWorks.Mouse

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.**ActiveDoc**
Set swModelView = swModel.**ActiveView**
Set swMouse = swModelView.**GetMouse**

swMouse.**MouseWheelXYZ** 0, 0, 0, 120, swMouse_RightUp
swMouse.**MouseWheelXYZ** 0, 0, 0, 120, swMouse_RightUp
swMouse.**MouseWheelXYZ** 0, 0, 0, 240, swMouse_RightUp
swMouse.**MouseWheelXYZ** 0, 0, 0, -120, swMouse_RightUp
swMouse.**MouseWheelXYZ** 0, 0, 0, -240, swMouse_RightUp

End Sub

## Remarks

To use this method and access SOLIDWORKS commands, you must add a reference to SOLIDWORKS `version` Commands type library (substitute the actual SOLIDWORKS version number for `version`) or **SolidWorks.Interop.swcommands.dll**, typically installed in `install_dir`**\api\redist.**

The coordinate system is the model's coordinate system.

## See Also

[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.html)
[IMouse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
