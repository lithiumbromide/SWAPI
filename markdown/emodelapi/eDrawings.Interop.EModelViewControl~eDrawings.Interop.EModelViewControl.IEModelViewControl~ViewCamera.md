---
title: "ViewCamera Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ViewCamera"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ViewCamera.html"
---

# ViewCamera Property (IEModelViewControl)

Gets or sets the current camera properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewCamera As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Object

instance.ViewCamera = value

value = instance.ViewCamera
```

### C#

```csharp
System.object ViewCamera {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ViewCamera {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Array of 12 doubles of the camera properties (see **Remarks**)

## VBA Syntax

See [EModelViewControl::ViewCamera](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ViewCamera.html).

## Remarks

The 12 array elements of type double are:

- x, y, and z coordinates of the camera position
- x, y, and z coordiantes of the camera target
- x, y, and z coordiantes of the camera up vector
- x and y coordinates of the camera field of view
- Projection:

  - 0.0 for orthographic
  - 1.0 for persepctive
  - -1.0 to keep current camera projection

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2008 SP0
