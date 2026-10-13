---
title: "DistanceOffsetEnd Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "DistanceOffsetEnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetEnd.html"
---

# DistanceOffsetEnd Property (IPartialEdgeFilletData)

Gets the offset distance from the end point for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DistanceOffsetEnd As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Double

value = instance.DistanceOffsetEnd
```

### C#

```csharp
System.double DistanceOffsetEnd {get;}
```

### C++/CLI

```cpp
property System.double DistanceOffsetEnd {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance offset from the end point

## VBA Syntax

See [PartialEdgeFilletData::DistanceOffsetEnd](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~DistanceOffsetEnd.html).

## Remarks

This property is valid only if [IPartialEdgeFilletData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~EndCondition.html) is set to swSimpleFilletPartialEdgeCondition_e.PartialEdgeDistanceOffset.

To modify the end distance offset of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)
[IPartialEdgeFilletData::DistanceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetStart.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
