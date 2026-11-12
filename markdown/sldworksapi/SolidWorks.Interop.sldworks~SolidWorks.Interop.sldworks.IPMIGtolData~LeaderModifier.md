---
title: "LeaderModifier Property (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "LeaderModifier"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~LeaderModifier.html"
---

# LeaderModifier Property (IPMIGtolData)

Gets the leader modifier of this PMI Gtol.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderModifier As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.Integer

instance.LeaderModifier = value

value = instance.LeaderModifier
```

### C#

```csharp
System.int LeaderModifier {get; set;}
```

### C++/CLI

```cpp
property System.int LeaderModifier {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Leader modifier as defined in [swPMILeaderModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMILeaderModifier_e.html)

## VBA Syntax

See [PMIGtolData::LeaderModifier](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~LeaderModifier.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
