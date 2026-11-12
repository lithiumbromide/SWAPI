---
title: "DistanceOffsetStart Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "DistanceOffsetStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetStart.html"
---

# DistanceOffsetStart Property (IPartialEdgeFilletData)

Gets the offset distance from the start point for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DistanceOffsetStart As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Double

value = instance.DistanceOffsetStart
```

### C#

```csharp
System.double DistanceOffsetStart {get;}
```

### C++/CLI

```cpp
property System.double DistanceOffsetStart {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance offset from the start point

## VBA Syntax

See [PartialEdgeFilletData::DistanceOffsetStart](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~DistanceOffsetStart.html).

## Remarks

This property is valid only if [IPartialEdgeFilletData::StartCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition.html) is set to swSimpleFilletPartialEdgeCondition_e.PartialEdgeDistanceOffset.

To modify the start distance offset of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)
[IPartialEdgeFilletData::DistanceOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetEnd.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
