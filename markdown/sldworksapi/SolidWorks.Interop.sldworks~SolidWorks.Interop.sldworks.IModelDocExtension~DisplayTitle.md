---
title: "DisplayTitle Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DisplayTitle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayTitle.html"
---

# DisplayTitle Property (IModelDocExtension)

Gets and sets this model's title to display in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayTitle As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.String

instance.DisplayTitle = value

value = instance.DisplayTitle
```

### C#

```csharp
System.string DisplayTitle {get; set;}
```

### C++/CLI

```cpp
property System.String^ DisplayTitle {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Display title; empty string to display the model's file name

## VBA Syntax

See [ModelDocExtension::DisplayTitle](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DisplayTitle.html).

## Remarks

This property works like the **FeatureManager design tree > RMB > Rename tree item**.

To get the display title of lightweight assembly components, use [IComponent2::DisplayTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~DisplayTitle.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[DAssemblyDocEvents_RenameDisplayTitleNotifyEventHandler Delegate (IModelDocExtension)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenameDisplayTitleNotifyEventHandler.html)
[DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler Delegate (IModelDocExtension)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler.html)
[DPartDocEvents_RenameDisplayTitleNotifyEventHandler Delegate (IModelDocExtension)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenameDisplayTitleNotifyEventHandler.html)

## Availability

SOLIDWORKS 2020 SP4, Revision Number 28.4
