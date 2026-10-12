---
title: "GetCores Method (ICable)"
project: "SOLIDWORKS Routing API Help"
interface: "ICable"
member: "GetCores"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCores.html"
---

# GetCores Method (ICable)

Gets the cores in this cable.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCores() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICable
Dim value As System.Object

value = instance.GetCores()
```

### C#

```csharp
System.object GetCores()
```

### C++/CLI

```cpp
System.Object^ GetCores();
```

### Return Value

Array of the [cores](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire.html) in this cable

## VBA Syntax

See [Cable::GetCores](ms-its:routingapivb6.chm::/SWRoutingLib~Cable~GetCores.html).

## Examples

See the [ICable](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable.html) examples.

## See Also

[ICable Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable.html)
[ICable Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable_members.html)
[ICable::IGetCores Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~IGetCores.html)
[ICable::GetCoresCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCoresCount.html)
[ICableProperty::GetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCoreProperties.html)
[ICableProperty::GetCorePropertyCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCorePropertyCount.html)
[ICableProperty::IGetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~IGetCoreProperties.html)

## Availability

SOLIDWORKS Routing 2006 FCS
