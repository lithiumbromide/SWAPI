---
title: "Count Property (IFaultEntity)"
project: "SOLIDWORKS API Help"
interface: "IFaultEntity"
member: "Count"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Count.html"
---

# Count Property (IFaultEntity)

Gets the number of faults that the entity has.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Count As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFaultEntity
Dim value As System.Integer

value = instance.Count
```

### C#

```csharp
System.int Count {get;}
```

### C++/CLI

```cpp
property System.int Count {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of faults

## VBA Syntax

See [FaultEntity::Count](ms-its:sldworksapivb6.chm::/sldworks~FaultEntity~Count.html).

## Examples

[Check Edges for Faults (VBA)](Check_Edges_for_Faults_Example_VB.htm)
[Check Faces for Faults (VBA)](Check_Faces_for_Faults_Example_VB.htm)
[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## Remarks

The return value has a 0-based index.

Call this property before calling [IFaultEntity::Entity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~Entity2.html) and [IFaultEntity::ErrorCode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~ErrorCode.html).

## See Also

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.html)
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
