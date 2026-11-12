---
title: "ApplyToThisConfiguration Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "ApplyToThisConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ApplyToThisConfiguration.html"
---

# ApplyToThisConfiguration Property (IDragOperator)

Gets or sets the configurations to which to apply the movement of the components.

## Syntax

### Visual Basic (Declaration)

```vb
Property ApplyToThisConfiguration As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.ApplyToThisConfiguration = value

value = instance.ApplyToThisConfiguration
```

### C#

```csharp
System.bool ApplyToThisConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.bool ApplyToThisConfiguration {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True applies the movement of the components only to the active configuration, false applies it to all configurations

## VBA Syntax

See [DragOperator::ApplyToThisConfiguration](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~ApplyToThisConfiguration.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision number 10.0
