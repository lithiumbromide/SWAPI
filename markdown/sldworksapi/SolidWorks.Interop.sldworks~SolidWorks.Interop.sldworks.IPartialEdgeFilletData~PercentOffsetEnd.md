---
title: "PercentOffsetEnd Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "PercentOffsetEnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetEnd.html"
---

# PercentOffsetEnd Property (IPartialEdgeFilletData)

Gets the percentage offset from the end point for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PercentOffsetEnd As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Double

value = instance.PercentOffsetEnd
```

### C#

```csharp
System.double PercentOffsetEnd {get;}
```

### C++/CLI

```cpp
property System.double PercentOffsetEnd {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= percentage offset from the end point < 100.0

## VBA Syntax

See [PartialEdgeFilletData::PercentOffsetEnd](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~PercentOffsetEnd.html).

## Remarks

This property is valid only if [IPartialEdgeFilletData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~EndCondition.html) is swSimpleFilletPartialEdgeCondition_e.PartialEdgePercentOffset.

To modify the end percent offset of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)
[IPartialEdgeFilletData::PercentOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetStart.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
