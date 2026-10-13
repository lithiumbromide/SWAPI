---
title: "GetSmartComponentData Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetSmartComponentData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.html"
---

# GetSmartComponentData Method (IComponent2)

Gets the features, components, and feature references of a Smart Component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSmartComponentData( _
   ByRef Features As System.Object, _
   ByRef FeaturesSelected As System.Object, _
   ByRef Components As System.Object, _
   ByRef ComponentsSelected As System.Object, _
   ByRef References As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Features As System.Object
Dim FeaturesSelected As System.Object
Dim Components As System.Object
Dim ComponentsSelected As System.Object
Dim References As System.Object
Dim value As System.Boolean

value = instance.GetSmartComponentData(Features, FeaturesSelected, Components, ComponentsSelected, References)
```

### C#

```csharp
System.bool GetSmartComponentData(
   out System.object Features,
   out System.object FeaturesSelected,
   out System.object Components,
   out System.object ComponentsSelected,
   out System.object References
)
```

### C++/CLI

```cpp
System.bool GetSmartComponentData(
   [Out] System.Object^ Features,
   [Out] System.Object^ FeaturesSelected,
   [Out] System.Object^ Components,
   [Out] System.Object^ ComponentsSelected,
   [Out] System.Object^ References
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Features`: Array of [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)s that can be selected for this Smart Component (see **Remarks**)
- `FeaturesSelected`: Array of boolean values; true if the corresponding item in the Features array is selected, false if it is not selected
- `Components`: Array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)s that can be selected for this Smart Component (see **Remarks**)
- `ComponentsSelected`: Array of boolean values; true if the corresponding item in the Components array is selected, false if it is not selected
- `References`: Array of feature reference entities that are used to activate the Smart Features specified by Features and FeaturesSelected; empty if the Smart Component features have not been activated (see **Remarks**)

### Return Value

True if successful, false if not

## VBA Syntax

See [Component2::GetSmartComponentData](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetSmartComponentData.html).

## Examples

[Activate Smart Features in an Assembly (VBA)](Activate_Smart_Features_in_an_Assembly_Example_VB.htm)
[Activate Smart Features in an Assembly (VB.NET)](Activate_Smart_Features_in_an_Assembly_Example_VBNET.htm)
[Activate Smart Features in an Assembly (C#)](Activate_Smart_Features_in_an_Assembly_Example_CSharp.htm)

## Remarks

A Smart Component is defined by:

- Components
- Features
- Feature references

See the SOLIDWORKS Help for more information about Smart Components.

Use this method to get the current features, components, and feature references of a Smart Component.

Before calling this method:

1. Open an assembly that contains a Smart Component whose Smart Features are not activated.
2. Find the Smart Component in the assembly using [IComponent2::IsSmartComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IsSmartComponent.html).

After calling this method, use [IComponent2::SetSmartComponentData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetSmartComponentData.html) to change which features and components of a Smart Component to enable and which Smart Features to activate.

Use [ISmartComponentFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISmartComponentFeatureData.html) to:

- Insert new features and components into a Smart Component.
- Delete features and components from a Smart Component.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::AddSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent.html)
[IAssemblyDoc::CreateSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
