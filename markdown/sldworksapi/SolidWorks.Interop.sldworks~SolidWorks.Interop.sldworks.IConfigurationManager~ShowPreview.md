---
title: "ShowPreview Property (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "ShowPreview"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ShowPreview.html"
---

# ShowPreview Property (IConfigurationManager)

Gets or sets whether to display the preview of a selected configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowPreview As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim value As System.Boolean

instance.ShowPreview = value

value = instance.ShowPreview
```

### C#

```csharp
System.bool ShowPreview {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowPreview {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the preview, false to restore the original ConfigurationManager

## VBA Syntax

See [ConfigurationManager::ShowPreview](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~ShowPreview.html).

## Examples

[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

Before using this property, you must activate and select the configuration to preview. If multiple configurations are selected, the last one's preview is displayed. The preview displays in the configuration pane below or above the pane of the selected configuration.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
