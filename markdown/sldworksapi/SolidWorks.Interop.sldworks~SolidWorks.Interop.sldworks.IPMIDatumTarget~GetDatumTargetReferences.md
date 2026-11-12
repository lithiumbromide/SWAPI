---
title: "GetDatumTargetReferences Method (IPMIDatumTarget)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumTarget"
member: "GetDatumTargetReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~GetDatumTargetReferences.html"
---

# GetDatumTargetReferences Method (IPMIDatumTarget)

Gets the datum references for this PMI datum target.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumTargetReferences() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumTarget
Dim value As System.Object

value = instance.GetDatumTargetReferences()
```

### C#

```csharp
System.object GetDatumTargetReferences()
```

### C++/CLI

```cpp
System.Object^ GetDatumTargetReferences();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of datum string references (see **Remarks**)

## VBA Syntax

See [PMIDatumTarget::GetDatumTargetReferences](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumTarget~GetDatumTargetReferences.html).

## Remarks

The datum references appear in the lower half of the datum target symbols.

## See Also

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.html)
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
