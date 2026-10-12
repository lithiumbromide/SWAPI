---
title: "TargetStyle Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "TargetStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TargetStyle.html"
---

# TargetStyle Property (ICallout)

Gets or sets the type of connection at the target point for this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property TargetStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As System.Integer

instance.TargetStyle = value

value = instance.TargetStyle
```

### C#

```csharp
System.int TargetStyle {get; set;}
```

### C++/CLI

```cpp
property System.int TargetStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Connection style as defined in [swCalloutTargetStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCalloutTargetStyle_e.html)

## VBA Syntax

See [Callout::TargetStyle](ms-its:sldworksapivb6.chm::/sldworks~Callout~TargetStyle.html).

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
