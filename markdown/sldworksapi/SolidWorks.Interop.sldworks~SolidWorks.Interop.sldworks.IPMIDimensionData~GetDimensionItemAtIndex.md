---
title: "GetDimensionItemAtIndex Method (IPMIDimensionData)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionData"
member: "GetDimensionItemAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~GetDimensionItemAtIndex.html"
---

# GetDimensionItemAtIndex Method (IPMIDimensionData)

Gets the PMI dimension item at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimensionItemAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetDimensionItemAtIndex(Index)
```

### C#

```csharp
System.object GetDimensionItemAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetDimensionItemAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the dimension item to get

### Return Value

[IPMIDimensionItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)

## VBA Syntax

See [PMIDimensionData::GetDimensionItemAtIndex](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionData~GetDimensionItemAtIndex.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

Use [IPMIDimensionData::GetDimensionItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~GetDimensionItemCount.html) to set Index.

## See Also

[IPMIDimensionData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.html)
[IPMIDimensionData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
