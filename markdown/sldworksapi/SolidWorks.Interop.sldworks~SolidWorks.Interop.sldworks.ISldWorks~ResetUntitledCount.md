---
title: "ResetUntitledCount Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ResetUntitledCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ResetUntitledCount.html"
---

# ResetUntitledCount Method (ISldWorks)

Resets the index of untitled documents.

## Syntax

### Visual Basic (Declaration)

```vb
Function ResetUntitledCount( _
   ByVal PartValue As System.Integer, _
   ByVal AssemValue As System.Integer, _
   ByVal DrawingValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim PartValue As System.Integer
Dim AssemValue As System.Integer
Dim DrawingValue As System.Integer
Dim value As System.Integer

value = instance.ResetUntitledCount(PartValue, AssemValue, DrawingValue)
```

### C#

```csharp
System.int ResetUntitledCount(
   System.int PartValue,
   System.int AssemValue,
   System.int DrawingValue
)
```

### C++/CLI

```cpp
System.int ResetUntitledCount(
   System.int PartValue,
   System.int AssemValue,
   System.int DrawingValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PartValue`: Starting index for part documents
- `AssemValue`: Starting index for assembly documents
- `DrawingValue`: Starting index for drawing documents

### Return Value

Total number of successful resets

## VBA Syntax

See [SldWorks::ResetUntitledCount](ms-its:sldworksapivb6.chm::/Sldworks~Sldworks~ResetUntitledCount.html)

## Examples

[Reset Untitled Document Count (VBA)](Reset_Untitled_Document_Count_Example_VB.htm)
[Reset Untitled Document Count (VB.NET)](Reset_Untitled_Document_Count_Example_VBNET.htm)
[Reset Untitled Document Count (C#)](Reset_Untitled_Document_Count_Example_CSharp.htm)

## Remarks

Use this method to reset untitled document indexes so that playbacks of the macro recorder increment untitled documents in a reproducible fashion.

For example, if the first playback of a macro creates Part1 and Part2, then the second playback may fail because it creates Part3 and Part4 instead of Part1 and Part2.

To ensure reproducible results, call ISldWorks::ResetUntitledCount at the beginning or end of a macro program.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
