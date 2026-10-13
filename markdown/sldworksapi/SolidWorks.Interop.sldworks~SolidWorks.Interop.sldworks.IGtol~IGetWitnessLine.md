---
title: "IGetWitnessLine Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetWitnessLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetWitnessLine.html"
---

# IGetWitnessLine Method (IGtol)

Gets the extension line that connects the leader of this geometric tolerance with the entity that is being dimensioned.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetWitnessLine() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Double

value = instance.IGetWitnessLine()
```

### C#

```csharp
System.double IGetWitnessLine()
```

### C++/CLI

```cpp
System.double IGetWitnessLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to array of six doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

As you drag a geometric tolerance leader off an entity, SOLIDWORKS dynamically builds a witness or extension line that connects the leader to the entity.

The return value is the following array of six doubles:

```vb
[ startPt[3], endPt[3] ]
```

where:

- startPt[3] = x,y,z start point coordinates of the witness line
- endPt[3] = x,y,z end point coordinates of the witness line

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetWitnessLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetWitnessLine.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
