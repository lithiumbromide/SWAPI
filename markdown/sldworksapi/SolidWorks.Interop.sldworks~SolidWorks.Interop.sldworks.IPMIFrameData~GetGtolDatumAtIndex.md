---
title: "GetGtolDatumAtIndex Method (IPMIFrameData)"
project: "SOLIDWORKS API Help"
interface: "IPMIFrameData"
member: "GetGtolDatumAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolDatumAtIndex.html"
---

# GetGtolDatumAtIndex Method (IPMIFrameData)

Gets the specified datum box in this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGtolDatumAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIFrameData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetGtolDatumAtIndex(Index)
```

### C#

```csharp
System.object GetGtolDatumAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetGtolDatumAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0 <= Gtol frame datum index <= 2

### Return Value

[IPMIGtolFrameDatum](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)

## VBA Syntax

See [PMIFrameData::GetGtolDatumAtIndex](ms-its:sldworksapivb6.chm::/sldworks~PMIFrameData~GetGtolDatumAtIndex.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

Use [IPMIFrameData::GetGtolDatumCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolDatumCount.html) to determine Index.

## See Also

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.html)
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
