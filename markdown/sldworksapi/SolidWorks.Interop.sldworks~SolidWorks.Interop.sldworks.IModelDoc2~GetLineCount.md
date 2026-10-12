---
title: "GetLineCount Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLineCount.html"
---

# GetLineCount Method (IModelDoc2)

Gets the number of lines in the current sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetLineCount()
```

### C#

```csharp
System.int GetLineCount()
```

### C++/CLI

```cpp
System.int GetLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of lines in the current sketch

## VBA Syntax

See [ModelDoc2::GetLineCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetLineCount.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLines.html)
[IModelDoc2::IGetLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetLines.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
