---
title: "PartLevel Property (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "PartLevel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~PartLevel.html"
---

# PartLevel Property (IDisplayStateSetting)

Gets or sets whether to set at the part level.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartLevel As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim value As System.Boolean

instance.PartLevel = value

value = instance.PartLevel
```

### C#

```csharp
System.bool PartLevel {get; set;}
```

### C++/CLI

```cpp
property System.bool PartLevel {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to set at the part level, false to not

## VBA Syntax

See [DisplayStateSetting::PartLevel](ms-its:sldworksapivb6.chm::/sldworks~DisplayStateSetting~PartLevel.html).

## Examples

[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
