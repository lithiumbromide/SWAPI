---
title: "SetComponentState Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetComponentState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html"
---

# SetComponentState Method (IAssemblyDoc)

Sets the suppression state for the specified components.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponentState( _
   ByVal SuppressionState As System.Integer, _
   ByVal CompArr As System.Object, _
   ByVal ConfigOption As System.Integer, _
   ByVal WhichConfig As System.String, _
   ByVal SaveClosedDocs As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim SuppressionState As System.Integer
Dim CompArr As System.Object
Dim ConfigOption As System.Integer
Dim WhichConfig As System.String
Dim SaveClosedDocs As System.Boolean
Dim value As System.Boolean

value = instance.SetComponentState(SuppressionState, CompArr, ConfigOption, WhichConfig, SaveClosedDocs)
```

### C#

```csharp
System.bool SetComponentState(
   System.int SuppressionState,
   System.object CompArr,
   System.int ConfigOption,
   System.string WhichConfig,
   System.bool SaveClosedDocs
)
```

### C++/CLI

```cpp
System.bool SetComponentState(
   System.int SuppressionState,
   System.Object^ CompArr,
   System.int ConfigOption,
   System.String^ WhichConfig,
   System.bool SaveClosedDocs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SuppressionState`: Component suppression state as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html) (see **Remarks**)
- `CompArr`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to change
- `ConfigOption`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `WhichConfig`: Name of the configuration to change
- `SaveClosedDocs`: True saves closed documents, false does not

### Return Value

True if the components were changed, false if not

## VBA Syntax

See [AssemblyDoc::SetComponentState](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetComponentState.html).

## Examples

[Set Component State (VBA)](Set_Component_State_Example_VB.htm)

## Remarks

You cannot set a component to lightweight using this method. Instead, use [IComponent::SetSuppression2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetSuppression2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
