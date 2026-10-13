---
title: "getAttachedComponentsCount Method (IAdvancedRouteSelector)"
project: "SOLIDWORKS Routing API Help"
interface: "IAdvancedRouteSelector"
member: "getAttachedComponentsCount"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector~getAttachedComponentsCount.html"
---

# getAttachedComponentsCount Method (IAdvancedRouteSelector)

Gets the number of attached components for the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function getAttachedComponentsCount( _
   ByVal selIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedRouteSelector
Dim selIndex As System.Integer
Dim value As System.Integer

value = instance.getAttachedComponentsCount(selIndex)
```

### C#

```csharp
System.int getAttachedComponentsCount(
   System.int selIndex
)
```

### C++/CLI

```cpp
System.int getAttachedComponentsCount(
   System.int selIndex
)
```

### Parameters

- `selIndex`: Index of the component whose number of attached components you want

### Return Value

Number of attached components for the component corresponding to selIndex

## VBA Syntax

See [AdvancedRouteSelector::getAttachedComponentsCount](ms-its:routingapivb6.chm::/SWRoutingLib~AdvancedRouteSelector~getAttachedComponentsCount.html).

## Examples

See the [IAdvancedRouteSelector](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html) examples.

## See Also

[IAdvancedRouteSelector Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html)
[IAdvancedRouteSelector Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector_members.html)

## Availability

SOLIDWORKS Routing 2009 FCS
