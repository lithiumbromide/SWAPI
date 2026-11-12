---
title: "UpdateScale Method (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "UpdateScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdateScale.html"
---

# UpdateScale Method (ITriadManipulator)

Sets scale for the triad manipulator's x,y,z axes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdateScale( _
   ByVal Scale As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator
Dim Scale As System.Double

instance.UpdateScale(Scale)
```

### C#

```csharp
void UpdateScale(
   System.double Scale
)
```

### C++/CLI

```cpp
void UpdateScale(
   System.double Scale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Scale`: Scale

## VBA Syntax

See [TriadManipulator::UpdateScale](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~UpdateScale.html).

## Remarks

The initial length of an axis is 40 pixels, and the length is unrestricted. Each axis is the same length.

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)
[ITriadManipulator::DoNotShow Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~DoNotShow.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
