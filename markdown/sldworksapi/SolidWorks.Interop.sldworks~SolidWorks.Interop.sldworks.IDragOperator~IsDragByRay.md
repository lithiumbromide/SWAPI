---
title: "IsDragByRay Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "IsDragByRay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsDragByRay.html"
---

# IsDragByRay Property (IDragOperator)

Gets or sets the drag-by-ray setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsDragByRay As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.IsDragByRay = value

value = instance.IsDragByRay
```

### C#

```csharp
System.bool IsDragByRay {get; set;}
```

### C++/CLI

```cpp
property System.bool IsDragByRay {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses drag-by-ray, false uses drag-by-transform (see **Remarks**)

## VBA Syntax

See [DragOperator::IsDragByRay](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~IsDragByRay.html).

## Remarks

- Drag-by-ray Tries to find a solution that keeps a specified geometry on, or close to, a ray (defined by a point on the ray and its direction).
- Drag-by-transform Uses a transform matrix, which is any combination of translations and rotations.

NOTE: IDragOperator does not define the drag ray; it only performs drag-by-transform. If this property is set to True, the user-interface component move honors this setting. The default mode for the user interface is drag-by-transform.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
