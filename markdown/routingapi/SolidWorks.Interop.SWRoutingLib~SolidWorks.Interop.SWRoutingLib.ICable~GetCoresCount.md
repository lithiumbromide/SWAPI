---
title: "GetCoresCount Method (ICable)"
project: "SOLIDWORKS Routing API Help"
interface: "ICable"
member: "GetCoresCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCoresCount.html"
---

# GetCoresCount Method (ICable)

Gets the number of cores in this cable.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoresCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICable
Dim value As System.Integer

value = instance.GetCoresCount()
```

### C#

```csharp
System.int GetCoresCount()
```

### C++/CLI

```cpp
System.int GetCoresCount();
```

### Return Value

Number of cores in this cable

## VBA Syntax

See [Cable::GetCoresCount](ms-its:routingapivb6.chm::/SWRoutingLib~Cable~GetCoresCount.html).

## Examples

See the [ICable](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable.html) examples.

## Remarks

Call this method before calling [ICable::IGetCores](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.ICable~IGetCores.html) to determine the size of the array for the cores for that method.

## See Also

[ICable Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable.html)
[ICable Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable_members.html)
[ICable::GetCores Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCores.html)
[ICableProperty::GetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCoreProperties.html)
[ICableProperty::GetCorePropertyCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCorePropertyCount.html)
[ICableProperty::IGetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~IGetCoreProperties.html)

## Availability

SOLIDWORKS Routing 2006 FCS
