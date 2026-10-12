---
title: "ActiveCommandTabIndex Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ActiveCommandTabIndex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTabIndex.html"
---

# ActiveCommandTabIndex Property (IModelDocExtension)

Gets and sets the index of the active SOLIDWORKS CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActiveCommandTabIndex As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

instance.ActiveCommandTabIndex = value

value = instance.ActiveCommandTabIndex
```

### C#

```csharp
System.int ActiveCommandTabIndex {get; set;}
```

### C++/CLI

```cpp
property System.int ActiveCommandTabIndex {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Index of the active tab

## VBA Syntax

See [ModelDocExtension::ActiveCommandTabIndex](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ActiveCommandTabIndex.html).

## Examples

[Activate SOLIDWORKS CommandManager Tab (VBA)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VB.htm)
[Activate SOLIDWORKS CommandManager Tab (VB.NET)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VBNET.htm)
[Activate SOLIDWORKS CommandManager Tab (C#)](Activate_SOLIDWORKS_CommandManager_Tab_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ActiveCommandTab Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTab.html)
[IModelDocExtension::CommandTabVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CommandTabVisible.html)
[IModelDocExtension::GetCommandTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCommandTabs.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
