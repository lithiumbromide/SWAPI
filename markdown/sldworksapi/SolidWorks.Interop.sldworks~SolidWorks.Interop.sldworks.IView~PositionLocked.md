---
title: "PositionLocked Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "PositionLocked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~PositionLocked.html"
---

# PositionLocked Property (IView)

Gets or sets whether this drawing view's position is locked.

## Syntax

### Visual Basic (Declaration)

```vb
Property PositionLocked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.PositionLocked = value

value = instance.PositionLocked
```

### C#

```csharp
System.bool PositionLocked {get; set;}
```

### C++/CLI

```cpp
property System.bool PositionLocked {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if view position is locked, false if not

## VBA Syntax

See [View::PositionLocked](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~PositionLocked.html).

## Examples

[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)
[Get View Bounding Box and Position (VB.NET)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::Position Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Position.html)

## Availability

SOLIDWORKS 2016 SP2, Revision Number 24.2
