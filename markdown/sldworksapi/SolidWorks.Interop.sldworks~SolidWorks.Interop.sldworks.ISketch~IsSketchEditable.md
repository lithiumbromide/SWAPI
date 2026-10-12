---
title: "IsSketchEditable Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IsSketchEditable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsSketchEditable.html"
---

# IsSketchEditable Method (ISketch)

Gets whether this sketch is editable.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSketchEditable() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Boolean

value = instance.IsSketchEditable()
```

### C#

```csharp
System.bool IsSketchEditable()
```

### C++/CLI

```cpp
System.bool IsSketchEditable();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this sketch is editable, false if not

## VBA Syntax

See [Sketch::IsSketchEditable](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IsSketchEditable.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::SetSketchEditable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetSketchEditable.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
