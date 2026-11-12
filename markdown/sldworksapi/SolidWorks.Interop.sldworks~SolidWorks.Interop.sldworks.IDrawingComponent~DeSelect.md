---
title: "DeSelect Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~DeSelect.html"
---

# DeSelect Method (IDrawingComponent)

Deselects this drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.Boolean

value = instance.DeSelect()
```

### C#

```csharp
System.bool DeSelect()
```

### C++/CLI

```cpp
System.bool DeSelect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to remove the component from the selection list if it is selected, false if not

## VBA Syntax

See [DrawingComponent::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~DeSelect.html).

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::Select Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Select.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
