---
title: "CurveChordTolerance Property (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "CurveChordTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~CurveChordTolerance.html"
---

# CurveChordTolerance Property (ITessellation)

Gets or sets the maximum permitted distance from a chord (facet fin) to the curve (edge entity).

## Syntax

### Visual Basic (Declaration)

```vb
Property CurveChordTolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Double

instance.CurveChordTolerance = value

value = instance.CurveChordTolerance
```

### C#

```csharp
System.double CurveChordTolerance {get; set;}
```

### C++/CLI

```cpp
property System.double CurveChordTolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for the curve chord tolerance

## VBA Syntax

See [Tessellation::CurveChordTolerance](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~CurveChordTolerance.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
