---
title: "EndEdit Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~EndEdit.html"
---

# EndEdit Method (ICWCable)

Stops editing this cable connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
Dim value As System.Integer

value = instance.EndEdit()
```

### C#

```csharp
System.int EndEdit()
```

### C++/CLI

```cpp
System.int EndEdit();
```

### Return Value

Error code as defined by [swsCableEndEditErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCableEndEditErrors_e.html)

## VBA Syntax

See [CWCable::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~EndEdit.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
