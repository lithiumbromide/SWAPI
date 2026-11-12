---
title: "IGetTessTriStripSize Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetTessTriStripSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripSize.html"
---

# IGetTessTriStripSize Method (IComponent2)

Gets the array size of floats required to contain the data returned when calling [IComponent2::IGetTessTriStrips](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetTessTriStrips.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStripSize() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.IGetTessTriStripSize()
```

### C#

```csharp
System.int IGetTessTriStripSize()
```

### C++/CLI

```cpp
System.int IGetTessTriStripSize();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Size of the array

## Remarks

Tessellation information is available only when the component is loaded as lightweight.

SOLIDWORKS calculates this number as ( 3 + FaceCount + StripCount + 3 * VertexCount).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
