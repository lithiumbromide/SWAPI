---
title: "CreateCovering Method (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "CreateCovering"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~CreateCovering.html"
---

# CreateCovering Method (IRouteProperty)

Creates a covering, which you can modify, for this route.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCovering() As Covering
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim value As Covering

value = instance.CreateCovering()
```

### C#

```csharp
Covering CreateCovering()
```

### C++/CLI

```cpp
Covering^ CreateCovering();
```

### Return Value

Pointer to [ICovering](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.ICovering.html) object

## VBA Syntax

See [RouteProperty::CreateCovering](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~CreateCovering.html).

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)
[IRouteProperty::AddCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~AddCovering.html)
[IRouteProperty::GetCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~GetCovering.html)
[IRouteProperty::RemoveCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~RemoveCovering.html)
[IRouteProperty::HasCovering Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~HasCovering.html)

## Availability

SOLIDWORKS Routing 2006 FCS
