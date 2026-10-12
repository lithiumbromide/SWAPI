---
title: "LeaderLocation Property (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "LeaderLocation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~LeaderLocation.html"
---

# LeaderLocation Property (IPMIGtolData)

Gets the leader location of this PMI Gtol.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderLocation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.Integer

instance.LeaderLocation = value

value = instance.LeaderLocation
```

### C#

```csharp
System.int LeaderLocation {get; set;}
```

### C++/CLI

```cpp
property System.int LeaderLocation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Leader location as defined in [swPMILeaderLocation_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMILeaderLocation_e.html)

## VBA Syntax

See [PMIGtolData::LeaderLocation](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~LeaderLocation.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
