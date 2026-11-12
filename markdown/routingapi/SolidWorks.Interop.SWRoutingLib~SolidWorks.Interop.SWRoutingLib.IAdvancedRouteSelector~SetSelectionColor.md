---
title: "SetSelectionColor Method (IAdvancedRouteSelector)"
project: "SOLIDWORKS Routing API Help"
interface: "IAdvancedRouteSelector"
member: "SetSelectionColor"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector~SetSelectionColor.html"
---

# SetSelectionColor Method (IAdvancedRouteSelector)

Sets the color of the selected components.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSelectionColor( _
   ByVal special As System.Boolean, _
   ByVal colorIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedRouteSelector
Dim special As System.Boolean
Dim colorIndex As System.Integer

instance.SetSelectionColor(special, colorIndex)
```

### C#

```csharp
void SetSelectionColor(
   System.bool special,
   System.int colorIndex
)
```

### C++/CLI

```cpp
void SetSelectionColor(
   System.bool special,
   System.int colorIndex
)
```

### Parameters

- `special`: True uses a specific color for selections, false does not
- `colorIndex`: Integer value for RGB value

## VBA Syntax

See [AdvancedRouteSelector::SetSelectionColor](ms-its:routingapivb6.chm::/SWRoutingLib~AdvancedRouteSelector~SetSelectionColor.html).

## Examples

See the [IAdvancedRouteSelector](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html) examples.

## See Also

[IAdvancedRouteSelector Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html)
[IAdvancedRouteSelector Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector_members.html)

## Availability

SOLIDWORKS Routing 2009 FCS
