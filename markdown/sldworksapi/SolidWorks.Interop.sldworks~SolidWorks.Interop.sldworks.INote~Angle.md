---
title: "Angle Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~Angle.html"
---

# Angle Property (INote)

Controls the rotation angle of this note.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Rotation angle, in radians, of this note

## VBA Syntax

See [Note::Angle](ms-its:sldworksapivb6.chm::/sldworks~Note~Angle.html).

## Examples

[Get Corresponding Objects in Assembly Component (C#)](Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm)
[Get Corresponding Objects in Assembly Component (VB.NET)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)
[Get Corresponding Objects in Assembly Component (VBA)](Get_Corresponding_Objects_in_Assembly_Component_Example_VB.htm)

## Remarks

The rotation angle of a note must be in the -360 to +360 range. If a value is specified that is outside of the range, the angle wraps around to be mapped back into range. For example, attempting to set this property to a value of 365 would result in the angle being set to 5.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
