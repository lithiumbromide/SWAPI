---
title: "IGetLines Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetLines.html"
---

# IGetLines Method (IModelDoc2)

Gets all of the lines in the current sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLines() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Double

value = instance.IGetLines()
```

### C#

```csharp
System.double IGetLines()
```

### C++/CLI

```cpp
System.double IGetLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of doubles:

[ LineType, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ... ]

where this array of 7 values repeats itself for each line in the current sketch. The number of doubles returned is (lineCount * 7). To determine the number of lines in the current sketch, use [IModelDoc2::GetLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLineCount.html).

See [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) for valid line types.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLineCount.html)
[IModelDoc2::GetLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLines.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
