---
title: "GetAdditionalSymbols Method (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "GetAdditionalSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetAdditionalSymbols.html"
---

# GetAdditionalSymbols Method (IPMIGtolBoxData)

Gets additional material conditions in this PMI Gtol frame box.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAdditionalSymbols() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Object

value = instance.GetAdditionalSymbols()
```

### C#

```csharp
System.object GetAdditionalSymbols()
```

### C++/CLI

```cpp
System.Object^ GetAdditionalSymbols();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of material conditions as defined in [swAdditionalSymbol_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdditionalSymbol_e.html)

## VBA Syntax

See [PMIGtolBoxData::GetAdditionalSymbols](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~GetAdditionalSymbols.html).

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)
[IPMIGtolBoxData::MaterialModifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~MaterialModifier.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
