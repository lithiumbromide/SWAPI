---
title: "DynamicClearanceEnabled Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "DynamicClearanceEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.html"
---

# DynamicClearanceEnabled Property (IDragOperator)

Gets or sets the dynamic clearance setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property DynamicClearanceEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.DynamicClearanceEnabled = value

value = instance.DynamicClearanceEnabled
```

### C#

```csharp
System.bool DynamicClearanceEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool DynamicClearanceEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables the dynamic clearance option, false disables it

## VBA Syntax

See [DragOperator::DynamicClearanceEnabled](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~DynamicClearanceEnabled.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::AddDynamicClearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddDynamicClearance.html)
[IDragOperator::CollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.html)
[IDragOperator::Drag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.html)
[IDragOperator::DragAsUI Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.html)
[IDragOperator::IDrag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.html)
[IDragOperator::IAddDynamicClearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddDynamicClearance.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
