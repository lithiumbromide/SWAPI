---
title: "UpdatePosition Method (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "UpdatePosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition.html"
---

# UpdatePosition Method (ITriadManipulator)

Updates the position of this triad manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdatePosition() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator
Dim value As System.Boolean

value = instance.UpdatePosition()
```

### C#

```csharp
System.bool UpdatePosition()
```

### C++/CLI

```cpp
System.bool UpdatePosition();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the position of the triad manipulator is updated, false if not

## VBA Syntax

See [TriadManipulator::UpdatePosition](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~UpdatePosition.html).

## Remarks

After setting any of these properties, call this method to update the position of the triad manipulator:

- [ITriadManipulator::Origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator~Origin.html)
- [ITriadManipulator::XAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator~XAxis.html)
- [ITriadManipulator::YAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator~YAxis.html)
- [ITriadManipulator::ZAxis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator~ZAxis.html)

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)
[ITriadManipulator::DoNotShow Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~DoNotShow.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
