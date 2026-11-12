---
title: "ActiveCommandTab Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ActiveCommandTab"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTab.html"
---

# ActiveCommandTab Property (IModelDocExtension)

Gets and sets the active SOLIDWORKS CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActiveCommandTab As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.String

instance.ActiveCommandTab = value

value = instance.ActiveCommandTab
```

### C#

```csharp
System.string ActiveCommandTab {get; set;}
```

### C++/CLI

```cpp
property System.String^ ActiveCommandTab {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Active tab name

## VBA Syntax

See [ModelDocExtension::ActiveCommandTab](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ActiveCommandTab.html).

## Examples

[Activate SOLIDWORKS CommandManager Tab (VBA)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VB.htm)
[Activate SOLIDWORKS CommandManager Tab (VB.NET)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VBNET.htm)
[Activate SOLIDWORKS CommandManager Tab (C#)](Activate_SOLIDWORKS_CommandManager_Tab_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetCommandTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCommandTabs.html)
[IModelDocExtension::ActiveCommandTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTabIndex.html)
[IModelDocExtension::CommandTabVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CommandTabVisible.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
