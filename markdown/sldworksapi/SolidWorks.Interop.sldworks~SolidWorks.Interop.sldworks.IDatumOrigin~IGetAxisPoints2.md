---
title: "IGetAxisPoints2 Method (IDatumOrigin)"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin"
member: "IGetAxisPoints2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~IGetAxisPoints2.html"
---

# IGetAxisPoints2 Method (IDatumOrigin)

Gets the points that define the geometry of this datum origin.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAxisPoints2() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumOrigin
Dim value As System.Double

value = instance.IGetAxisPoints2()
```

### C#

```csharp
System.double IGetAxisPoints2()
```

### C++/CLI

```cpp
System.double IGetAxisPoints2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 8 doubles is 4 (X,Y) coordinates in drawing space:

  - The first coordinate (array items 0 and 1) is the start of the X leader portion of the symbol.
  - The second coordinate (array items 2 and 3) is the tip of the arrowhead on the X leader portion of the symbol.
  - The third coordinate (array items 4 and 5) is the start of the Y leader portion of the symbol.
  - The fourth coordinate (array items 6 and 7) is the tip of the arrowhead on the Y leader portion of the symbol.
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html)
[IDatumOrigin::GetAxisPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetAxisPoints2.html)
[IDatumOrigin::SetAxisPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~SetAxisPoints.html)
[IDatumOrigin::ISetAxisPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~ISetAxisPoints.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
