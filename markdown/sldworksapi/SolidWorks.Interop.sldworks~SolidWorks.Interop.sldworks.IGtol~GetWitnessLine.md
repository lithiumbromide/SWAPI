---
title: "GetWitnessLine Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetWitnessLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetWitnessLine.html"
---

# GetWitnessLine Method (IGtol)

Gets the extension line that connects the leader of this geometric tolerance with the entity being dimensioned.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWitnessLine() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Object

value = instance.GetWitnessLine()
```

### C#

```csharp
System.object GetWitnessLine()
```

### C++/CLI

```cpp
System.Object^ GetWitnessLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

An array of six doubles (see **Remarks**)

## VBA Syntax

See [Gtol::GetWitnessLine](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetWitnessLine.html).

## Examples

[Get GTol Witness Line (VBA)](Get_GTol_Witness_Line_Example_VB.htm)
[Get GTol Witness Line (VB.NET)](Get_GTol_Witness_Line_Example_VBNET.htm)
[Get GTol Witness Line (C#)](Get_GTol_Witness_Line_Example_CSharp.htm)

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
[IGtol::IGetWitnessLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetWitnessLine.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
