---
title: "GetGtolBoxAtIndex Method (IPMIFrameData)"
project: "SOLIDWORKS API Help"
interface: "IPMIFrameData"
member: "GetGtolBoxAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolBoxAtIndex.html"
---

# GetGtolBoxAtIndex Method (IPMIFrameData)

Gets the specified tolerance box in this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGtolBoxAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIFrameData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetGtolBoxAtIndex(Index)
```

### C#

```csharp
System.object GetGtolBoxAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetGtolBoxAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0 <= Gtol frame box index <= 2

### Return Value

[IPMIGtolBoxData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)

## VBA Syntax

See [PMIFrameData::GetGtolBoxAtIndex](ms-its:sldworksapivb6.chm::/sldworks~PMIFrameData~GetGtolBoxAtIndex.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

Use [IPMIFrameData::GetGtolBoxCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolBoxCount.html) to determine Index.

## See Also

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.html)
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
