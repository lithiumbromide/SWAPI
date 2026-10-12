---
title: "AddComponent Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "AddComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddComponent.html"
---

# AddComponent Method (IDragOperator)

Adds a component to the list of components to drag.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComponent( _
   ByVal PDisp As System.Object, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim PDisp As System.Object
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.AddComponent(PDisp, AppendFlag)
```

### C#

```csharp
System.bool AddComponent(
   System.object PDisp,
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool AddComponent(
   System.Object^ PDisp,
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDisp`: Component to add to the list
- `AppendFlag`: True to append the component to the list, false to clear the list before adding the component

### Return Value

True if successful, false for failure; fixed components always return false (see **Remarks**)

## VBA Syntax

See [DragOperator::AddComponent](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~AddComponent.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)

## Remarks

Components that are constrained via mates are not considered fixed.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::IAddComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddComponent.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
