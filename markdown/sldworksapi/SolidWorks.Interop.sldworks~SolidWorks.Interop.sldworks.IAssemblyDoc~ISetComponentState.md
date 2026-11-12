---
title: "ISetComponentState Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ISetComponentState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentState.html"
---

# ISetComponentState Method (IAssemblyDoc)

Sets the suppression state for the specified components.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetComponentState( _
   ByVal SuppressionState As System.Integer, _
   ByVal NumComps As System.Integer, _
   ByRef CompArr As Component2, _
   ByVal ConfigOption As System.Integer, _
   ByVal WhichConfig As System.String, _
   ByVal SaveClosedDocs As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim SuppressionState As System.Integer
Dim NumComps As System.Integer
Dim CompArr As Component2
Dim ConfigOption As System.Integer
Dim WhichConfig As System.String
Dim SaveClosedDocs As System.Boolean
Dim value As System.Boolean

value = instance.ISetComponentState(SuppressionState, NumComps, CompArr, ConfigOption, WhichConfig, SaveClosedDocs)
```

### C#

```csharp
System.bool ISetComponentState(
   System.int SuppressionState,
   System.int NumComps,
   ref Component2 CompArr,
   System.int ConfigOption,
   System.string WhichConfig,
   System.bool SaveClosedDocs
)
```

### C++/CLI

```cpp
System.bool ISetComponentState(
   System.int SuppressionState,
   System.int NumComps,
   Component2^% CompArr,
   System.int ConfigOption,
   System.String^ WhichConfig,
   System.bool SaveClosedDocs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SuppressionState`: Component suppression state as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html) (see **Remarks**)
- `NumComps`: Number of components to change
- `CompArr`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to change of size numComps
- `ConfigOption`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `WhichConfig`: Name of the configuration to change
- `SaveClosedDocs`: True saves closed documents, false does not

### Return Value

True if the components were changed, false if not

## VBA Syntax

See [AssemblyDoc::ISetComponentState](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ISetComponentState.html).

## Remarks

You cannot set a component to lightweight using this method. Instead, use [IComponent::SetSuppression2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetSuppression2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
