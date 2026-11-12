---
title: "GetWireProperty Method (IWire)"
project: "SOLIDWORKS Routing API Help"
interface: "IWire"
member: "GetWireProperty"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire~GetWireProperty.html"
---

# GetWireProperty Method (IWire)

Gets the properties of this wire.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWireProperty() As WireProperty
```

### Visual Basic (Usage)

```vb
Dim instance As IWire
Dim value As WireProperty

value = instance.GetWireProperty()
```

### C#

```csharp
WireProperty GetWireProperty()
```

### C++/CLI

```cpp
WireProperty^ GetWireProperty();
```

### Return Value

Pointer to the [IWireProperty](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWireProperty.html) object

## VBA Syntax

See [Wire::GetWireProperty](ms-its:routingapivb6.chm::/SWRoutingLib~Wire~GetWireProperty.html).

## Examples

[Get Cable Cores (VBA)](Get_Cores_Example_VB.htm)
[Get Cable Cores (VB.NET)](Get_Cores_Example_VBNET.htm)
[Get Cable Cores (C#)](Get_Cores_Example_CSharp.htm)

## See Also

[IWire Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire.html)
[IWire Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IWire_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
