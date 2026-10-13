---
title: "GetTolTypeValues Method (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "GetTolTypeValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypeValues.html"
---

# GetTolTypeValues Method (IPMIGtolBoxData)

Gets the tolerance zone values in this PMI Gtol frame box.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTolTypeValues() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Object

value = instance.GetTolTypeValues()
```

### C#

```csharp
System.object GetTolTypeValues()
```

### C++/CLI

```cpp
System.Object^ GetTolTypeValues();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of tolerance zone values

## VBA Syntax

See [PMIGtolBoxData::GetTolTypeValues](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~GetTolTypeValues.html).

## Remarks

The array returned by this method maps one-to-one and onto with the array returned by [IPMIGtolBoxData::GetTolTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypes.html).

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)
[IPMIGtolBoxData::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
