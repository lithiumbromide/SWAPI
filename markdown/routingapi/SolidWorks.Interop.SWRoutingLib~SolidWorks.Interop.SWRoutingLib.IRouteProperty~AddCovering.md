---
title: "AddCovering Method (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "AddCovering"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~AddCovering.html"
---

# AddCovering Method (IRouteProperty)

Adds a covering to this route.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCovering( _
   ByVal Covering As Covering _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim Covering As Covering
Dim value As System.Boolean

value = instance.AddCovering(Covering)
```

### C#

```csharp
System.bool AddCovering(
   Covering Covering
)
```

### C++/CLI

```cpp
System.bool AddCovering(
   Covering^ Covering
)
```

### Parameters

- `Covering`: Pointer to [ICovering](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.ICovering.html) object

### Return Value

True if covering is added, false if not

## VBA Syntax

See [RouteProperty::AddCovering](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~AddCovering.html).

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)
[IRouteProperty::CreateCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~CreateCovering.html)
[IRouteProperty::GetCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~GetCovering.html)
[IRouteProperty::RemoveCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~RemoveCovering.html)
[IRouteProperty::HasCovering Property](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~HasCovering.html)

## Availability

SOLIDWORKS Routing 2006 FCS
