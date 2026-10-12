---
title: "UseSameElementSize2 Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "UseSameElementSize2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~UseSameElementSize2.html"
---

# UseSameElementSize2 Property (ICWMeshControl)

Gets or sets whether to use the the same element for all selected components in this mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSameElementSize2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim value As System.Boolean

instance.UseSameElementSize2 = value

value = instance.UseSameElementSize2
```

### C#

```csharp
System.bool UseSameElementSize2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseSameElementSize2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use same size for all components
- 0 or false = Use different sizes based on component mesh control

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
