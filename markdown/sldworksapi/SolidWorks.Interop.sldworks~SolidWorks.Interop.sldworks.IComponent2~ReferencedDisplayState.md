---
title: "ReferencedDisplayState Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ReferencedDisplayState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState.html"
---

# ReferencedDisplayState Property (IComponent2)

Obsolete. Superseded by [IComponent2::ReferencedDisplayState2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferencedDisplayState As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.ReferencedDisplayState
```

### C#

```csharp
System.string ReferencedDisplayState {get;}
```

### C++/CLI

```cpp
property System.String^ ReferencedDisplayState {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of display state

## VBA Syntax

See [Component2::ReferencedDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Component2~ReferencedDisplayState.html).

## Examples

[Get Referenced Display State (VBA)](Get_Referenced_Display_State_Example_VB.htm)
[Get Referenced Display State (VB.NET)](Get_Referenced_Display_State_Example_VBNET.htm)
[Get Referenced Display State (C#)](Get_Referenced_Display_State_Example_CSharp.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)

## Availability

SOLIDWORKS 2011 SP02, Revision Number 19.2
