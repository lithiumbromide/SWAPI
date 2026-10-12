---
title: "AddPropertyExtension Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "AddPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~AddPropertyExtension.html"
---

# AddPropertyExtension Method (IComponent2)

Adds a property extension to this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddPropertyExtension(PropertyExtension)
```

### C#

```csharp
System.int AddPropertyExtension(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddPropertyExtension(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`: Value of the property extension to add to the component

### Return Value

1 if the property extension is added to the component, -1 if not

## VBA Syntax

See [Component2::AddPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Component2~AddPropertyExtension.html).

## Remarks

This method does not support adding multiple property extensions to the same component.

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the component.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPropertyExtension.html)
[IComponent2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ResetPropertyExtension.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
