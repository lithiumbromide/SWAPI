---
title: "IsLinked Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "IsLinked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsLinked.html"
---

# IsLinked Property (IDisplayDimension)

Gets whether the dimension has text linked to it.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsLinked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

value = instance.IsLinked
```

### C#

```csharp
System.bool IsLinked {get;}
```

### C++/CLI

```cpp
property System.bool IsLinked {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the text is linked to the dimension, false if not

## VBA Syntax

See [DisplayDimension::IsLinked](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~IsLinked.html).

## Examples

[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLinkedText.html)
[IDisplayDimension::SetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLinkedText.html)
[IDisplayDimension::Unlink Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Unlink.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
