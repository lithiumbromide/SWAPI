---
title: "LBDownAt Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "LBDownAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LBDownAt.html"
---

# LBDownAt Method (IModelDoc2)

Generates a left mouse button press (down) event.

## Syntax

### Visual Basic (Declaration)

```vb
Sub LBDownAt( _
   ByVal Flags As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Flags As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.LBDownAt(Flags, X, Y, Z)
```

### C#

```csharp
void LBDownAt(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void LBDownAt(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flags`: Any combination of:

  - MK_CONTROL
  - MK_LBUTTON
  - MK_MBUTTON
  - MK_RBUTTON
  - MK_SHIFT
- `X`: X coordinate of position of cursor
- `Y`: Y coordinate of position of cursor
- `Z`: Z coordinate of position of cursor

## VBA Syntax

See [ModelDoc2::LBDownAt](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~LBDownAt.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::LBUpAt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LBUpAt.html)
[IModelDoc2::DragTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DragTo.html)
[IMouse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
