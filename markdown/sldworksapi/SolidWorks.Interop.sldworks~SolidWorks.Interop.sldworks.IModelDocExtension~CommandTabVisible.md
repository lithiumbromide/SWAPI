---
title: "CommandTabVisible Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CommandTabVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CommandTabVisible.html"
---

# CommandTabVisible Property (IModelDocExtension)

Gets and sets the visibility of the specified SOLIDWORKS CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Property CommandTabVisible( _
   ByVal TabIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim TabIndex As System.Integer
Dim value As System.Boolean

instance.CommandTabVisible(TabIndex) = value

value = instance.CommandTabVisible(TabIndex)
```

### C#

```csharp
System.bool CommandTabVisible(
   System.int TabIndex
) {get; set;}
```

### C++/CLI

```cpp
property System.bool CommandTabVisible {
   System.bool get(System.int TabIndex);
   void set (System.int TabIndex, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TabIndex`: Index of the tab for which to get or set visibility

### Property Value

True to make the tab visible, false to not

## VBA Syntax

See [ModelDocExtension::CommandTabVisible](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CommandTabVisible.html).

## Examples

[Activate SOLIDWORKS CommandManager Tab (VBA)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VB.htm)
[Activate SOLIDWORKS CommandManager Tab (VB.NET)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VBNET.htm)
[Activate SOLIDWORKS CommandManager Tab (C#)](Activate_SOLIDWORKS_CommandManager_Tab_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ActiveCommandTab Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTab.html)
[IModelDocExtension::ActiveCommandTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTabIndex.html)
[IModelDocExtension::GetCommandTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCommandTabs.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
