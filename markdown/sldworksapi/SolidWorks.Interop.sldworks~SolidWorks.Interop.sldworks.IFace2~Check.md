---
title: "Check Property (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "Check"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Check.html"
---

# Check Property (IFace2)

Checks whether the face is a valid, and, if not, returns the faults.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Check As FaultEntity
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As FaultEntity

value = instance.Check
```

### C#

```csharp
FaultEntity Check {get;}
```

### C++/CLI

```cpp
property FaultEntity^ Check {
   FaultEntity^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to [IFaultEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity.html) object

## VBA Syntax

See [Face2::Check](ms-its:sldworksapivb6.chm::/sldworks~Face2~Check.html).

## Examples

[Check Faces for Faults (VBA)](Check_Faces_for_Faults_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IEdge::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Check.html)
[IBody2::Check3 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
