---
title: "GetCorePropertyCount Method (ICableProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "ICableProperty"
member: "GetCorePropertyCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCorePropertyCount.html"
---

# GetCorePropertyCount Method (ICableProperty)

Gets the number of core properties in the cable.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorePropertyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICableProperty
Dim value As System.Integer

value = instance.GetCorePropertyCount()
```

### C#

```csharp
System.int GetCorePropertyCount()
```

### C++/CLI

```cpp
System.int GetCorePropertyCount();
```

### Return Value

Number of core properties

## VBA Syntax

See [CableProperty::GetCorePropertyCount](ms-its:routingapivb6.chm::/SWRoutingLib~CableProperty~GetCorePropertyCount.html).

## Examples

See the [ICableProperty](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty.html) examples.

## Remarks

Call this method before calling [ICableProperty::IGetCoreProperties](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.ICableProperty~IGetCoreProperties.html) to determine the size of the array for the cores for that method.

## See Also

[ICableProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty.html)
[ICableProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty_members.html)
[ICableProperty::GetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCoreProperties.html)
[ICable::GetCores Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCores.html)
[ICable::GetCoresCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCoresCount.html)
[ICable::IGetCores Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~IGetCores.html)

## Availability

SOLIDWORKS Routing 2006 FCS
