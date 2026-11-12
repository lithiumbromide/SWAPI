---
title: "PercentOffsetStart Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "PercentOffsetStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetStart.html"
---

# PercentOffsetStart Property (IPartialEdgeFilletData)

Gets the percentage offset from the start point for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PercentOffsetStart As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Double

value = instance.PercentOffsetStart
```

### C#

```csharp
System.double PercentOffsetStart {get;}
```

### C++/CLI

```cpp
property System.double PercentOffsetStart {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= percentage offset from the start point < 100.0

## VBA Syntax

See [PartialEdgeFilletData::PercentOffsetStart](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~PercentOffsetStart.html).

## Remarks

This property is valid only if [IPartialEdgeFilletData::StartCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition.html) is swSimpleFilletPartialEdgeCondition_e.PartialEdgePercentOffset.

To modify the start percent offset of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)
[IPartialEdgeFilletData::PercentOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetEnd.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
