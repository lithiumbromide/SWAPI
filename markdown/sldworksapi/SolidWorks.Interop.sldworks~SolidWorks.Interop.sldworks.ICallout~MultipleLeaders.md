---
title: "MultipleLeaders Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "MultipleLeaders"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~MultipleLeaders.html"
---

# MultipleLeaders Property (ICallout)

Gets or sets the display of multiple leaders for this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property MultipleLeaders As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As System.Boolean

instance.MultipleLeaders = value

value = instance.MultipleLeaders
```

### C#

```csharp
System.bool MultipleLeaders {get; set;}
```

### C++/CLI

```cpp
property System.bool MultipleLeaders {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display multiple leaders, false to not

## VBA Syntax

See [Callout::MultipleLeaders](ms-its:sldworksapivb6.chm::/sldworks~Callout~MultipleLeaders.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
