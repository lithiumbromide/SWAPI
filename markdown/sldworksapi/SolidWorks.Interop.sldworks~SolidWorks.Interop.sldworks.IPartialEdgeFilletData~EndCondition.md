---
title: "EndCondition Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~EndCondition.html"
---

# EndCondition Property (IPartialEdgeFilletData)

Gets the type of end condition for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Integer

value = instance.EndCondition
```

### C#

```csharp
System.int EndCondition {get;}
```

### C++/CLI

```cpp
property System.int EndCondition {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition as defined in [swSimpleFilletPartialEdgeCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletPartialEdgeCondition_e.html)

## VBA Syntax

See [PartialEdgeFilletData::EndCondition](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~EndCondition.html).

## Remarks

To modify the end condition of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)
[IPartialEdgeFilletData::StartCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition.html)
[IPartialEdgeFilletData::DistanceOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetEnd.html)
[IPartialEdgeFilletData::PercentOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetEnd.html)
[IPartialEdgeFilletData::ReferenceOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetEnd.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
