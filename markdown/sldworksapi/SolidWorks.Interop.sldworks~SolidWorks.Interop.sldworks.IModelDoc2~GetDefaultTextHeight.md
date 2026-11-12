---
title: "GetDefaultTextHeight Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetDefaultTextHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDefaultTextHeight.html"
---

# GetDefaultTextHeight Method (IModelDoc2)

Gets the default text height in use for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefaultTextHeight() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Double

value = instance.GetDefaultTextHeight()
```

### C#

```csharp
System.double GetDefaultTextHeight()
```

### C++/CLI

```cpp
System.double GetDefaultTextHeight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Default height (in meters) for text for this document

## VBA Syntax

See [ModelDoc2::GetDefaultTextHeight](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetDefaultTextHeight.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
