---
title: "ModifyMemberParameters Method (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "ModifyMemberParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~ModifyMemberParameters.html"
---

# ModifyMemberParameters Method (IBeltChainFeatureData)

Changes diameter and whether to flip the belt side of the specified pulley component.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyMemberParameters( _
   ByVal PulleyCompObject As System.Object, _
   ByVal Diameter As System.Double, _
   ByVal Flip As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim PulleyCompObject As System.Object
Dim Diameter As System.Double
Dim Flip As System.Boolean
Dim value As System.Boolean

value = instance.ModifyMemberParameters(PulleyCompObject, Diameter, Flip)
```

### C#

```csharp
System.bool ModifyMemberParameters(
   System.object PulleyCompObject,
   System.double Diameter,
   System.bool Flip
)
```

### C++/CLI

```cpp
System.bool ModifyMemberParameters(
   System.Object^ PulleyCompObject,
   System.double Diameter,
   System.bool Flip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PulleyCompObject`: Pulley component
- `Diameter`: Diameter > 0.0 to change; 0.0 to not change
- `Flip`: True to flip the belt side, false to not

### Return Value

True if pulley component successfully modifed, false if not

## VBA Syntax

See [BeltChainFeatureData::ModifyMemberParameters](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~ModifyMemberParameters.html).

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
