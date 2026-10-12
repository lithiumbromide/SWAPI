---
title: "ErrorCode Property (IFaultEntity)"
project: "SOLIDWORKS API Help"
interface: "IFaultEntity"
member: "ErrorCode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~ErrorCode.html"
---

# ErrorCode Property (IFaultEntity)

Gets the error for the fault for the specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ErrorCode( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFaultEntity
Dim Index As System.Integer
Dim value As System.Integer

value = instance.ErrorCode(Index)
```

### C#

```csharp
System.int ErrorCode(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.int ErrorCode {
   System.int get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index number indicating the entity with the fault

### Property Value

Error as defined by [swFaultEntityErrorCode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaultEntityErrorCode_e.html); -1 indicates an unknown error

## VBA Syntax

See [FaultEntity::ErrorCode](ms-its:sldworksapivb6.chm::/sldworks~FaultEntity~ErrorCode.html).

## Examples

[Check Bodies for Faults (VBA)](Check_Bodies_for_Faults_Example_VB.htm)
[Check Faces for Faults (VBA)](Check_Faces_for_Faults_Example_VB.htm)
[Check Edges for Faults (C#)](Check_Edges_for_Faults_Example_CSharp.htm)
[Check Edges for Faults (VB.NET)](Check_Edges_for_Faults_Example_VBNET.htm)
[Check Edges for Faults (VBA)](Check_Edges_for_Faults_Example_VB.htm)

## Remarks

To determine the value for index, call [IFaultEntity::Count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~Count.html) before calling this property. Call [IFaultEntity::Entity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~Entity2.html) to get the entity.

## See Also

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.html)
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
