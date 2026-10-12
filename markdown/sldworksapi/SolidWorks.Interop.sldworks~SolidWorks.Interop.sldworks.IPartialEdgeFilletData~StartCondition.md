---
title: "StartCondition Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "StartCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition.html"
---

# StartCondition Property (IPartialEdgeFilletData)

Gets the type of start condition for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StartCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Integer

value = instance.StartCondition
```

### C#

```csharp
System.int StartCondition {get;}
```

### C++/CLI

```cpp
property System.int StartCondition {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Start condition as defined in [swSimpleFilletPartialEdgeCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletPartialEdgeCondition_e.html)

## VBA Syntax

See [PartialEdgeFilletData::StartCondition](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~StartCondition.html).

## Remarks

To modify the start condition of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)
[IPartialEdgeFilletData::EndCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~EndCondition.html)
[IPartialEdgeFilletData::DistanceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetStart.html)
[IPartialEdgeFilletData::PercentOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetStart.html)
[IPartialEdgeFilletData::ReferenceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
