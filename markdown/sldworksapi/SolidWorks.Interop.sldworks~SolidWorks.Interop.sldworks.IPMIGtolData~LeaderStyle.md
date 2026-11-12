---
title: "LeaderStyle Property (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "LeaderStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~LeaderStyle.html"
---

# LeaderStyle Property (IPMIGtolData)

Gets the leader style of this PMI Gtol.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.Integer

instance.LeaderStyle = value

value = instance.LeaderStyle
```

### C#

```csharp
System.int LeaderStyle {get; set;}
```

### C++/CLI

```cpp
property System.int LeaderStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Leader style as defined in [swPMILeaderStyle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMILeaderStyle_e.html)

## VBA Syntax

See [PMIGtolData::LeaderStyle](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~LeaderStyle.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
