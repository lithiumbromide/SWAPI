---
title: "GetLines Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLines.html"
---

# GetLines Method (IModelDoc2)

Gets all of the lines in the current sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLines() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetLines()
```

### C#

```csharp
System.object GetLines()
```

### C++/CLI

```cpp
System.Object^ GetLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [ModelDoc2::GetLines](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetLines.html).

## Remarks

The return value is the following array of doubles:

[ LineType, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ... ]

where this array of 7 values repeats itself for each line in the current sketch. The number of doubles returned is (lineCount * 7). To determine the number of lines in the current sketch, use [IModelDoc2::GetLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLineCount.html).

See [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) for valid line types.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetLines.html)
[IModelDoc2::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLineCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
