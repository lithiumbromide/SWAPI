---
title: "HasCovering Property (IRouteProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteProperty"
member: "HasCovering"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~HasCovering.html"
---

# HasCovering Property (IRouteProperty)

Gets whether a covering is present on this route.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasCovering As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteProperty
Dim value As System.Boolean

value = instance.HasCovering
```

### C#

```csharp
System.bool HasCovering {get;}
```

### C++/CLI

```cpp
property System.bool HasCovering {
   System.bool get();
}
```

### Property Value

True if a covering is present, false if not

## VBA Syntax

See [RouteProperty::HasCovering](ms-its:routingapivb6.chm::/SWRoutingLib~RouteProperty~HasCovering.html).

## Examples

See the [IRouteProperty](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html) examples.

## Examples

[Edit Coverings (VBA)](Edit_Coverings_Example_VB.htm)

## See Also

[IRouteProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty.html)
[IRouteProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty_members.html)
[ICovering Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICovering.html)
[IRouteProperty::AddCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~AddCovering.html)
[IRouteProperty::CreateCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~CreateCovering.html)
[IRouteProperty::GetCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~GetCovering.html)
[IRouteProperty::RemoveCovering Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteProperty~RemoveCovering.html)

## Availability

SOLIDWORKS Routing 2006 FCS
