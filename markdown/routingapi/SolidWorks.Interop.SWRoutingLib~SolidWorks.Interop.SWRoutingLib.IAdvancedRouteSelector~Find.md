---
title: "Find Method (IAdvancedRouteSelector)"
project: "SOLIDWORKS Routing API Help"
interface: "IAdvancedRouteSelector"
member: "Find"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector~Find.html"
---

# Find Method (IAdvancedRouteSelector)

Finds the number of specified components in the assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Find( _
   ByVal connectorName As System.String, _
   ByVal searchType As System.Integer, _
   ByVal singleInstanceOnly As System.Boolean, _
   ByVal append As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedRouteSelector
Dim connectorName As System.String
Dim searchType As System.Integer
Dim singleInstanceOnly As System.Boolean
Dim append As System.Boolean
Dim value As System.Integer

value = instance.Find(connectorName, searchType, singleInstanceOnly, append)
```

### C#

```csharp
System.int Find(
   System.string connectorName,
   System.int searchType,
   System.bool singleInstanceOnly,
   System.bool append
)
```

### C++/CLI

```cpp
System.int Find(
   System.String^ connectorName,
   System.int searchType,
   System.bool singleInstanceOnly,
   System.bool append
)
```

### Parameters

- `connectorName`: Component name; can be the name of a fitting, cable, or wire; can include wild-card character (*)
- `searchType`: Search type as defined by [swRoutingSearchType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRoutingSearchType_e.html)
- `singleInstanceOnly`: True to find a single instance of connectorName, false to find all instances of connectorName
- `append`: True appends the selection to the selection list, false replaces the selection list with this selection

### Return Value

Number of components found for connectorName

## VBA Syntax

See [AdvancedRouteSelector::Find](ms-its:routingapivb6.chm::/SWRoutingLib~AdvancedRouteSelector~Find.html).

## Examples

See the [IAdvancedRouteSelector](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html) examples.

## See Also

[IAdvancedRouteSelector Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html)
[IAdvancedRouteSelector Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector_members.html)

## Availability

SOLIDWORKS Routing 2009 FCS
