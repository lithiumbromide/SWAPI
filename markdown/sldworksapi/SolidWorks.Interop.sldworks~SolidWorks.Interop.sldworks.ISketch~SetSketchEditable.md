---
title: "SetSketchEditable Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "SetSketchEditable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetSketchEditable.html"
---

# SetSketchEditable Method (ISketch)

Sets whether this sketch is editable.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSketchEditable( _
   ByVal Editable As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Editable As System.Boolean

instance.SetSketchEditable(Editable)
```

### C#

```csharp
void SetSketchEditable(
   System.bool Editable
)
```

### C++/CLI

```cpp
void SetSketchEditable(
   System.bool Editable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Editable`: True to make this sketch editable, false to make it read only

## VBA Syntax

See [Sketch::SetSketchEditable](ms-its:sldworksapivb6.chm::/sldworks~Sketch~SetSketchEditable.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IsSketchEditable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsSketchEditable.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
