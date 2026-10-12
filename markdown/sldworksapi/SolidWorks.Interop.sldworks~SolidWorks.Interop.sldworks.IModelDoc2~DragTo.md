---
title: "DragTo Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DragTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DragTo.html"
---

# DragTo Method (IModelDoc2)

Drags the specified end point.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DragTo( _
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

instance.DragTo(Flags, X, Y, Z)
```

### C#

```csharp
void DragTo(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void DragTo(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flags`: Mouse-event flags as defined by the operating system. They can be combined to indicate the selection state. For example:

  - Left-mouse button is pressed: 0x0001
  - Right-mouse button is pressed: 0x0002
  - Shift key is pressed: 0x0004
  - Ctrl key is pressed: 0x0008
  - Middle-mouse button is pressed: 0x0010
- `X`: X coordinate of end point
- `Y`: Y coordinate of end point
- `Z`: Z coordinate of end point

## VBA Syntax

See [ModelDoc2::DragTo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DragTo.html).

## Remarks

This method is only valid for assemblies.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
