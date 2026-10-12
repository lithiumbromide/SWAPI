---
title: "GetChildrenCount Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "GetChildrenCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildrenCount.html"
---

# GetChildrenCount Method (IDrawingComponent)

Gets the number of child components for this drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetChildrenCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.Integer

value = instance.GetChildrenCount()
```

### C#

```csharp
System.int GetChildrenCount()
```

### C++/CLI

```cpp
System.int GetChildrenCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of child components for this drawing component

## VBA Syntax

See [DrawingComponent::GetChildrenCount](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~GetChildrenCount.html).

## Examples

[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)

## Remarks

Call this method before calling [IDrawingComponent::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~IGetChildren.html).

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildren.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
