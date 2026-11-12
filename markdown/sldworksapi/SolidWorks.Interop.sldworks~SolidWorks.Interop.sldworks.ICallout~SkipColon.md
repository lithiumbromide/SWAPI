---
title: "SkipColon Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "SkipColon"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SkipColon.html"
---

# SkipColon Property (ICallout)

Gets and sets whether to add a colon at the end of the callout label.

## Syntax

### Visual Basic (Declaration)

```vb
Property SkipColon As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As System.Boolean

instance.SkipColon = value

value = instance.SkipColon
```

### C#

```csharp
System.bool SkipColon {get; set;}
```

### C++/CLI

```cpp
property System.bool SkipColon {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

False to add a colon, true to not

## VBA Syntax

See [Callout::SkipColon](ms-its:sldworksapivb6.chm::/sldworks~Callout~SkipColon.html).

## Examples

[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

## Remarks

This property applies only to a callout that is independent of a selection or created with [IModelDocExtension::CreateCallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateCallout.html).

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[ICallout::Label2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Label2.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
