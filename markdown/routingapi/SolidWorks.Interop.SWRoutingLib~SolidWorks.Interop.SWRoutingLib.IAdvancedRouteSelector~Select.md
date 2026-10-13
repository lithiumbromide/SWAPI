---
title: "Select Method (IAdvancedRouteSelector)"
project: "SOLIDWORKS Routing API Help"
interface: "IAdvancedRouteSelector"
member: "Select"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector~Select.html"
---

# Select Method (IAdvancedRouteSelector)

Gets the names of the attached components for the selected component.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal selIndex As System.Integer, _
   ByVal append As System.Boolean, _
   ByVal callbackIn As System.Object, _
   ByVal outputType As System.Integer, _
   ByRef selObjName As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedRouteSelector
Dim selIndex As System.Integer
Dim append As System.Boolean
Dim callbackIn As System.Object
Dim outputType As System.Integer
Dim selObjName As System.Object
Dim value As System.Object

value = instance.Select(selIndex, append, callbackIn, outputType, selObjName)
```

### C#

```csharp
System.object Select(
   System.int selIndex,
   System.bool append,
   System.object callbackIn,
   System.int outputType,
   out System.object selObjName
)
```

### C++/CLI

```cpp
System.Object^ Select(
   System.int selIndex,
   System.bool append,
   System.Object^ callbackIn,
   System.int outputType,
   [Out] System.Object^ selObjName
)
```

### Parameters

- `selIndex`: Index of the component (fitting, cable, or wire) to select
- `append`: True appends the selection to the selection list, false replaces the selection list with this selection
- `callbackIn`: SOLIDWORKS [SelectData](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) or NULL
- `outputType`: Output type as defined by [swAdvancedRouteSelectionOutput_e](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.swAdvancedRouteSelectionOutput_e.html)
- `selObjName`: Array of length 1; contains either the name of the selected component or an empty string (see **Remarks**)

### Return Value

Array of names of the attached components for the selected component (see **Remarks**)

## VBA Syntax

See [AdvancedRouteSelector::Select](ms-its:routingapivb6.chm::/SWRoutingLib~AdvancedRouteSelector~Select.html).

## Examples

See the [IAdvancedRouteSelector](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html) examples.

## Remarks

Both selObjName and the return value of this method are Variant SafeArrays of BSTRs. See [Passing SafeArrays in Visual Basic](sldworksapiprogguide.chm::/Overview/SafeArraysVB.htm) and [Passing SafeArrays in C++](sldworksAPIProgGuide.chm::/Overview/SafeArrays.htm) for more information.

## See Also

[IAdvancedRouteSelector Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector.html)
[IAdvancedRouteSelector Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IAdvancedRouteSelector_members.html)

## Availability

SOLIDWORKS Routing 2009 FCS
