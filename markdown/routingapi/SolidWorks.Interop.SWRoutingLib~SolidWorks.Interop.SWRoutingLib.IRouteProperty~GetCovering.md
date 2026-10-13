---
title: "GetCovering Method (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "GetCovering"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~GetCovering.html"
---

# GetCovering Method (IRouteProperty)

Gets the covering for this route.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCovering() As Covering
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim value As Covering

value = instance.GetCovering()
```

### C#

```csharp
Covering GetCovering()
```

### C++/CLI

```cpp
Covering^ GetCovering();
```

### Return Value

Pointer to [ICovering](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.ICovering.html) object

## VBA Syntax

See [RouteProperty::GetCovering](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~GetCovering.html).

## Examples

See the [IRouteProperty](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html) examples.

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)
[IRouteProperty::AddCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~AddCovering.html)
[IRouteProperty::CreateCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~CreateCovering.html)
[IRouteProperty::RemoveCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~RemoveCovering.html)
[IRouteProperty::HasCovering Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~HasCovering.html)

## Availability

SOLIDWORKS Routing 2006 FCS
