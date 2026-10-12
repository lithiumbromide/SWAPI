---
title: "ISetBoundaries Method (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "ISetBoundaries"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~ISetBoundaries.html"
---

# ISetBoundaries Method (ISwOLEObject)

Sets the boundaries of this OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBoundaries( _
   ByRef Boundary As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim Boundary As System.Double

instance.ISetBoundaries(Boundary)
```

### C#

```csharp
void ISetBoundaries(
   ref System.double Boundary
)
```

### C++/CLI

```cpp
void ISetBoundaries(
   System.double% Boundary
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Boundary`: - in-process, unmanaged C++: Pointer to an array of doubles of these coordinates:

    - Drawings: sheet coordinates
    - Parts or assemblies: screen pixel coordinates
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)
[ISwOLEObject::IGetBoundaries Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBoundaries.html)
[ISwOLEObject::Boundaries Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Boundaries.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
