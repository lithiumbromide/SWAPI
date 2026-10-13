---
title: "UserName Property (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "UserName"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~UserName.html"
---

# UserName Property (IWire)

Gets or sets the name of the wire.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As System.String

instance.UserName = value

value = instance.UserName
```

### C#

```csharp
System.string UserName {get; set;}
```

### C++/CLI

```cpp
property System.String^ UserName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of wire

## VBA Syntax

See [Wire::UserName](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~UserName.html).

## Examples

[Swap To and From Components on Each Wire (VBA)](Swap_To_and_From_Components_on_Each_Wire_Example_VB.htm)
[Set New Route Paths for Wires (C#)](Set_New_Route_Paths_for_Wires_Example_CSharp.htm)
[Set New Route Paths for Wires (VB.NET)](Set_New_Route_Paths_for_Wires_Example_VBNET.htm)
[Set New Route Paths for Wires (VBA)](Set_New_Route_Paths_for_Wires_Example_VB.htm)

## Remarks

The wire name is a unique name for each wire or core. When naming the cores in a cable, give each core a unique name within the cable. The same names can be used in other cables.

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)
[IWire::FromPinReference Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~FromPinReference.html)
[IWire::ToPinReference Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~ToPinReference.html)

## Availability

SOLIDWORKS Routing 2006 FCS
