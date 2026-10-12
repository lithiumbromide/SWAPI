---
title: "ReferencedDisplayState2 Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ReferencedDisplayState2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState2.html"
---

# ReferencedDisplayState2 Property (IComponent2)

Gets or sets the active display state of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencedDisplayState2 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

instance.ReferencedDisplayState2 = value

value = instance.ReferencedDisplayState2
```

### C#

```csharp
System.string ReferencedDisplayState2 {get; set;}
```

### C++/CLI

```cpp
property System.String^ ReferencedDisplayState2 {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of display state

## VBA Syntax

See [Component2::ReferencedDisplayState2](ms-its:sldworksapivb6.chm::/sldworks~Component2~ReferencedDisplayState2.html).

## Examples

[Set Active Display State of Referenced Component (C#)](Set_Active_Display_State_of_Referenced_Component_Example_CSharp.htm)
[Set Active Display State of Referenced Component (VB.NET)](Set_Active_Display_State_of_Referenced_Component_Example_VBNET.htm)
[Set Active Display State of Referenced Component (VBA)](Set_Active_Display_State_of_Referenced_Component_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
