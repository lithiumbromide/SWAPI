---
title: "LeaderType Property (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "LeaderType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~LeaderType.html"
---

# LeaderType Property (IPMIGtolData)

Gets the leader type of this PMI Gtol.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.Integer

instance.LeaderType = value

value = instance.LeaderType
```

### C#

```csharp
System.int LeaderType {get; set;}
```

### C++/CLI

```cpp
property System.int LeaderType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Leader type as defined in [swPMILeaderType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMILeaderType_e.html)

## VBA Syntax

See [PMIGtolData::LeaderType](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~LeaderType.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
