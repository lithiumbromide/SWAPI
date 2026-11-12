---
title: "GetTolTypes Method (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "GetTolTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypes.html"
---

# GetTolTypes Method (IPMIGtolBoxData)

Gets the tolerance zone types in this PMI Gtol frame box.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTolTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Object

value = instance.GetTolTypes()
```

### C#

```csharp
System.object GetTolTypes()
```

### C++/CLI

```cpp
System.Object^ GetTolTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of tolerance zone types as defined in [swGtolTolType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolTolType_e.html)

## VBA Syntax

See [PMIGtolBoxData::GetTolTypes](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~GetTolTypes.html).

## Remarks

The tolerance zone types returned by this method map on-to-one and onto with tolerance zone values returned by [IPMIGtolBoxData::GetTolTypeValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypeValues.html).

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
